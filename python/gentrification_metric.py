import pandas as pd
from tabulate import tabulate

# Read cleaned dataframes
census_2011 = pd.read_csv('analysis/cleaned_features/census_2011.csv')
census_2012 = pd.read_csv('analysis/cleaned_features/census_2012.csv')
census_2013 = pd.read_csv('analysis/cleaned_features/census_2013.csv')
census_2014 = pd.read_csv('analysis/cleaned_features/census_2014.csv')
census_2015 = pd.read_csv('analysis/cleaned_features/census_2015.csv')
census_2016 = pd.read_csv('analysis/cleaned_features/census_2016.csv')
census_2017 = pd.read_csv('analysis/cleaned_features/census_2017.csv')
census_2018 = pd.read_csv('analysis/cleaned_features/census_2018.csv')
census_2019 = pd.read_csv('analysis/cleaned_features/census_2019.csv')


# Group data based on zipcode
census_2011 = census_2011.groupby(['NAME'], as_index=False).mean()
census_2012 = census_2012.groupby(['NAME'], as_index=False).mean()
census_2013 = census_2013.groupby(['NAME'], as_index=False).mean()
census_2014 = census_2014.groupby(['NAME'], as_index=False).mean()
census_2015 = census_2015.groupby(['NAME'], as_index=False).mean()
census_2016 = census_2016.groupby(['NAME'], as_index=False).mean()
census_2017 = census_2017.groupby(['NAME'], as_index=False).mean()
census_2018 = census_2018.groupby(['NAME'], as_index=False).mean()
census_2019 = census_2019.groupby(['NAME'], as_index=False).mean()


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

# Get difference in values from 2011 and 2019
df_2011_2019 = pd.merge(census_2011,census_2019,how = 'inner', on = 'NAME', suffixes=['_2011','_2019'])

# Get list of values
lst_values = ['NAME','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_media_price']

# Intialize dataframe
df_delta = pd.DataFrame(df_2011_2019['NAME'])

# Go through each element of the list values
for feature in lst_values[1:]:
    df_delta[feature + '_delta'] = df_2011_2019[feature + '_2019'] - df_2011_2019[feature + '_2011'] # get the change in census tracts

# Switch signs so that gentrification can be seen as positive
df_delta['median_age_delta'] = df_delta['median_age_delta'] * -1
df_delta['foreign_born_not_a_us_citizen_delta'] = df_delta['foreign_born_not_a_us_citizen_delta'] * -1

# Normalize the data
def normalize(df):
    '''The following normalizes the data'''
    result = df.copy()
    for feature_name in df.columns[1:]:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result
df_delta_norm = normalize(df_delta)

# Get the mean of the normalized data
df_mean = df_delta_norm.mean()

# Get sum of mean values
int_gentrification_metric_mean = sum(df_mean)

# Get getrification metric for each ZCTA5
df_delta_norm['gentrification_metric'] = df_delta_norm.sum( axis = 'columns')

# Get difference between city wide gentrification metric and individual zipcode
df_delta_norm['gentrification_metric_delta'] = df_delta_norm['gentrification_metric'] - int_gentrification_metric_mean

df_delta_norm[df_delta_norm['NAME'] == 'ZCTA5 11249']

# print('unique values',len(df_delta_norm['NAME'].unique()))

# print('total values', len(df_delta_norm['NAME']))

print(df_delta_norm[df_delta_norm['NAME'] == 'ZCTA5 11249'])