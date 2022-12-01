import pandas as pd
from tabulate import tabulate
import os


# Read cleaned dataframes
census_2011 = pd.read_csv(os.getcwd()[:-6] + 'analysis/by_year/census_data_2011.csv', encoding='utf-8', low_memory = False)
census_2012 = pd.read_csv(os.getcwd()[:-6] + 'analysis/by_year/census_data_2012.csv', encoding='utf-8', low_memory = False)
census_2013 = pd.read_csv(os.getcwd()[:-6] + 'analysis/by_year/census_data_2013.csv', encoding='utf-8', low_memory = False)
census_2014 = pd.read_csv(os.getcwd()[:-6] + 'analysis/by_year/census_data_2014.csv', encoding='utf-8', low_memory = False)
census_2015 = pd.read_csv(os.getcwd()[:-6] + 'analysis/by_year/census_data_2015.csv', encoding='utf-8', low_memory = False)
census_2016 = pd.read_csv(os.getcwd()[:-6] + 'analysis/by_year/census_data_2016.csv', encoding='utf-8', low_memory = False)
census_2017 = pd.read_csv(os.getcwd()[:-6] + 'analysis/by_year/census_data_2017.csv', encoding='utf-8', low_memory = False)
census_2018 = pd.read_csv(os.getcwd()[:-6] + 'analysis/by_year/census_data_2018.csv', encoding='utf-8', low_memory = False)
census_2019 = pd.read_csv(os.getcwd()[:-6] + 'analysis/by_year/census_data_2019.csv', encoding='utf-8', low_memory = False)


# Find and rename median age columns
for df in [census_2011, census_2012, census_2013, census_2014, census_2015, census_2016]:
    df.rename(columns = {
        'DP05_0017E' : 'median_age'
    }, inplace = True)

for df in [census_2017, census_2018, census_2019]:
    df.rename(columns = {
        'DP05_0018E' : 'median_age'
    }, inplace = True)   

# Find and rename white non-hispanic
for df in [census_2011, census_2012, census_2013, census_2014, census_2015, census_2016]:
    df.rename(columns = {
        'DP05_0072E' : 'white_non-hispanic'
    }, inplace = True)

for df in [census_2017, census_2018, census_2019]:
    df.rename(columns = {
        'DP05_0077E' : 'white_non-hispanic'
    }, inplace = True)

# Find and rename income
for df in [census_2011, census_2012, census_2013, census_2014, census_2015, census_2016, census_2017, census_2018, census_2019]:
    df.rename(columns = {
        'S1901_C01_012E': 'household_income',
        'DP05_0001E': 'total_population'
    }, inplace = True)

# Find and rename number of immigrants
for df in [census_2011, census_2012, census_2013, census_2014, census_2015, census_2016, census_2017, census_2018]:
    df.rename(columns = {
        'DP02_0095E': 'foreign_born_not_a_us_citizen'
    }, inplace = True)

for df in [census_2019]:
    df.rename(columns = {
        'DP02_0097E': 'foreign_born_not_a_us_citizen'
    }, inplace = True)

# Find and rename education information
for df in [census_2011, census_2012, census_2013, census_2014, census_2015, census_2016, census_2017, census_2018]:
    df.rename(columns = {
        'DP02_0064E': 'bachelors'
    }, inplace = True)

for df in [census_2019]:
    df.rename(columns = {
        'DP02_0065E':'bachelors'
    }, inplace = True)

# Find and rename rental cost
for df in [census_2011, census_2012, census_2013, census_2014]:
    df.rename(columns = {
        'DP04_0132E': 'gross_rent_media_price'
    }, inplace = True)

for df in [census_2015, census_2016, census_2017, census_2018, census_2019]:
    df.rename(columns = {
        'DP04_0134E': 'gross_rent_media_price'
    }, inplace = True)

# Remove columns not needed
census_2011 = census_2011[['NAME','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_media_price', 'total_population']]
census_2012 = census_2012[['NAME','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_media_price', 'total_population']]
census_2013 = census_2013[['NAME','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_media_price', 'total_population']]
census_2014 = census_2014[['NAME','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_media_price', 'total_population']]
census_2015 = census_2015[['NAME','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_media_price', 'total_population']]
census_2016 = census_2016[['NAME','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_media_price', 'total_population']]
census_2017 = census_2017[['NAME','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_media_price', 'total_population']]
census_2018 = census_2018[['NAME','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_media_price', 'total_population']]
census_2019 = census_2019[['NAME','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_media_price', 'total_population']]

# Function to make all string into floats or remove the value
def func_make_float(df):
    result = df.copy()
    for feature_name in ['median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_media_price']:
        result[feature_name] = df[feature_name].apply(pd.to_numeric, errors='coerce')
    return result

census_2011 = func_make_float(census_2011)
census_2012 = func_make_float(census_2012)
census_2013 = func_make_float(census_2013)
census_2014 = func_make_float(census_2014)
census_2015 = func_make_float(census_2015)
census_2016 = func_make_float(census_2016)
census_2017 = func_make_float(census_2017)
census_2018 = func_make_float(census_2018)
census_2019 = func_make_float(census_2019)



# Write census data to csv
census_2011.to_csv(os.getcwd()[:-6] +'analysis/cleaned_features/census_2011.csv', index = False)
census_2012.to_csv(os.getcwd()[:-6] +'analysis/cleaned_features/census_2012.csv', index = False)
census_2013.to_csv(os.getcwd()[:-6] +'analysis/cleaned_features/census_2013.csv', index = False)
census_2014.to_csv(os.getcwd()[:-6] +'analysis/cleaned_features/census_2014.csv', index = False)
census_2015.to_csv(os.getcwd()[:-6] +'analysis/cleaned_features/census_2015.csv', index = False)
census_2016.to_csv(os.getcwd()[:-6] +'analysis/cleaned_features/census_2016.csv', index = False)
census_2017.to_csv(os.getcwd()[:-6] +'analysis/cleaned_features/census_2017.csv', index = False)
census_2018.to_csv(os.getcwd()[:-6] +'analysis/cleaned_features/census_2018.csv', index = False)
census_2019.to_csv(os.getcwd()[:-6] +'analysis/cleaned_features/census_2019.csv', index = False)
