import pandas as pd, os, sys

# Read in CSVs
census_2011 = pd.read_csv(os.getcwd() +'/analysis/by_year/census_2011.csv', low_memory=False, encoding='utf-8')
census_2019 = pd.read_csv(os.getcwd() +'/analysis/by_year/census_2019.csv', low_memory=False, encoding='utf-8')

for df in [census_2011,census_2019]:
    df.rename(columns = {
        'DP05_0001E': 'total_population',# Find and rename total population
        'S1901_C01_012E': 'household_income'# Find and rename household income
    }, inplace = True)



census_2011.rename(columns = {
        'DP05_0017E' : 'median_age',# Find and rename median age columns
        'DP05_0072E' : 'white_non-hispanic',# Find and rename percent white non-hispanic
        'DP02_0095E': 'foreign_born_not_a_us_citizen',# Find and rename immigrants
        'DP02_0064E': 'bachelors',# Find and rename number of bachelors degrees
        'DP04_0132E': 'gross_rent_median_price'# Find and rename median rent
        }, inplace = True)

census_2019.rename(columns = {
        'DP05_0018E' : 'median_age',# Find and rename median age columns
        'DP05_0077E' : 'white_non-hispanic',# Find and rename white non-hispanic
        'DP02_0097E': 'foreign_born_not_a_us_citizen',# Find and rename white
        'DP02_0065E': 'bachelors',# Find and rename number of bachelors degrees
        'DP04_0134E': 'gross_rent_median_price'# Find and rename median rent
    }, inplace = True)

# Remove columns not needed
census_2011 = census_2011[['NAME','total_population','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_median_price']]
census_2019 = census_2019[['NAME','total_population','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_median_price']]

# Function to make all string into floats or remove the value
def func_make_float(df):
    result = df.copy()
    for feature_name in ['median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_median_price']:
        result[feature_name] = df[feature_name].apply(pd.to_numeric, errors='coerce')
    return result
census_2011 = func_make_float(census_2011)
census_2019 = func_make_float(census_2019)


# strip 'ZCTA5 ' from Name columns
def func_strip_ZCTA5(df):
    df['NAME'] = df['NAME'].str.lstrip('ZCTA5 ')
    return df
census_2011 = func_strip_ZCTA5(census_2011)
census_2019 = func_strip_ZCTA5(census_2019)

# Remove ZCTA5s with a total pop of 0
def func_remove_pop_0(df):
    df = df[df['total_population'] > 0]
    return df
census_2011 = func_remove_pop_0(census_2011)
census_2019 = func_remove_pop_0(census_2019)

# Write census data to csv
census_2011 = census_2011.to_csv(os.getcwd() +'/analysis/cleaned_features/census_2011.csv', index = False)
census_2019 = census_2019.to_csv(os.getcwd() +'/analysis/cleaned_features/census_2019.csv', index = False)



