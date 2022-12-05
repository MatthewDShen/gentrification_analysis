import pandas as pd
from tabulate import tabulate
import os


# Read cleaned dataframes
census_2011 = pd.read_csv(os.getcwd() + '/analysis/cleaned_features/census_2011.csv', encoding='utf-8')
census_2012 = pd.read_csv(os.getcwd() + '/analysis/cleaned_features/census_2012.csv', encoding='utf-8')
census_2013 = pd.read_csv(os.getcwd() + '/analysis/cleaned_features/census_2013.csv', encoding='utf-8')
census_2014 = pd.read_csv(os.getcwd() + '/analysis/cleaned_features/census_2014.csv', encoding='utf-8')
census_2015 = pd.read_csv(os.getcwd() + '/analysis/cleaned_features/census_2015.csv', encoding='utf-8')
census_2016 = pd.read_csv(os.getcwd() + '/analysis/cleaned_features/census_2016.csv', encoding='utf-8')
census_2017 = pd.read_csv(os.getcwd() + '/analysis/cleaned_features/census_2017.csv', encoding='utf-8')
census_2018 = pd.read_csv(os.getcwd() + '/analysis/cleaned_features/census_2018.csv', encoding='utf-8')
census_2019 = pd.read_csv(os.getcwd() + '/analysis/cleaned_features/census_2019.csv', encoding='utf-8')

# Get only nyc zipcodes
lst_nyc_zips = list(range(10001-1,10282+1)) + list(range(10301-1,10314+1)) + list(range(10451-1,10475+1)) + list(range(11004-1,11109+1)) + list(range(11351-1,11697+1)) + list(range(11201-1,11256+1)) # create list of zipcodes
census_2011 = census_2011[census_2011['NAME'].isin(lst_nyc_zips)]
census_2012 = census_2012[census_2012['NAME'].isin(lst_nyc_zips)]
census_2013 = census_2013[census_2013['NAME'].isin(lst_nyc_zips)]
census_2014 = census_2014[census_2014['NAME'].isin(lst_nyc_zips)]
census_2015 = census_2015[census_2015['NAME'].isin(lst_nyc_zips)]
census_2016 = census_2016[census_2016['NAME'].isin(lst_nyc_zips)]
census_2017 = census_2017[census_2017['NAME'].isin(lst_nyc_zips)]
census_2018 = census_2018[census_2018['NAME'].isin(lst_nyc_zips)]
census_2019 = census_2019[census_2019['NAME'].isin(lst_nyc_zips)]

# Interpolate data to fill in missing values
census_2011.interpolate(inplace = True)
census_2012.interpolate(inplace = True)
census_2013.interpolate(inplace = True)
census_2014.interpolate(inplace = True)
census_2015.interpolate(inplace = True)
census_2016.interpolate(inplace = True)
census_2017.interpolate(inplace = True)
census_2018.interpolate(inplace = True)
census_2019.interpolate(inplace = True)

# Fill first value if na
census_2011.fillna(method = 'bfill', inplace = True)
census_2012.fillna(method = 'bfill', inplace = True)
census_2013.fillna(method = 'bfill', inplace = True)
census_2014.fillna(method = 'bfill', inplace = True)
census_2015.fillna(method = 'bfill', inplace = True)
census_2016.fillna(method = 'bfill', inplace = True)
census_2017.fillna(method = 'bfill', inplace = True)
census_2018.fillna(method = 'bfill', inplace = True)
census_2019.fillna(method = 'bfill', inplace = True)


# Make certain features per capita
def func_to_make_per_capita(df):
    result = df.copy()
    for feature_name in ['white_non-hispanic','foreign_born_not_a_us_citizen','bachelors']:
        result[feature_name + '_percent'] = df[feature_name]/df['total_population']
    return result

# Apply the func to make per capita to some columns in the dataframes
census_2011 = func_to_make_per_capita(census_2011)
census_2012 = func_to_make_per_capita(census_2012)
census_2013 = func_to_make_per_capita(census_2013)
census_2014 = func_to_make_per_capita(census_2014)
census_2015 = func_to_make_per_capita(census_2015)
census_2016 = func_to_make_per_capita(census_2016)
census_2017 = func_to_make_per_capita(census_2017)
census_2018 = func_to_make_per_capita(census_2018)
census_2019 = func_to_make_per_capita(census_2019)



# Get difference in values from 2011 and 2019
df_2011_2019 = pd.merge(census_2011,census_2019,how = 'inner', on = 'NAME', suffixes=['_2011','_2019'])



# Get list of values
lst_values = ['NAME','median_age','white_non-hispanic_percent','household_income','foreign_born_not_a_us_citizen_percent','bachelors_percent','gross_rent_median_price']

# Intialize dataframe
df_delta = pd.DataFrame(df_2011_2019['NAME'])

# Go through each element of the list values
for feature in lst_values[1:]:
    df_delta[feature + '_delta'] = df_2011_2019[feature + '_2019'] - df_2011_2019[feature + '_2011'] # get the change in census tracts


# Switch signs so that gentrification can be seen as positive
df_delta['median_age_delta'] = df_delta['median_age_delta'] * -1
df_delta['foreign_born_not_a_us_citizen_percent_delta'] = df_delta['foreign_born_not_a_us_citizen_percent_delta'] * -1

# Normalize the data
df_delta_norm = (df_delta-df_delta.mean())/df_delta.std()

# Create census metric
df_census_metric = pd.DataFrame(df_delta['NAME'].astype(str))
df_census_metric['gentrification_metric'] = df_delta_norm.sum(axis = 'columns')# Get getrification metric for each ZCTA5
for feature in lst_values[1:]:
    df_census_metric[feature] = df_delta_norm[feature+'_delta']

print(df_census_metric['bachelors_percent_2019']-df_census_metric['bachelors_percent_2019'])


# Write csv of census metric values
df_census_metric.to_csv(os.getcwd() + '/analysis/removena/remove_na_vals.csv', index = False)

# df_delta_norm[df_delta_norm['NAME'] == 'ZCTA5 11249']

# print('unique values',len(df_delta_norm['NAME'].unique()))

# print('total values', len(df_delta_norm['NAME']))

# print(tabulate(df_delta_norm.head(), headers='keys', tablefmt='psql'))