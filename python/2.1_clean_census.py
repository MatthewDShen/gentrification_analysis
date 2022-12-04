import pandas as pd, sys
import os

# Read in CSVs
lst_years = range(2011,2019+1) # range of years we are observing
lst_dfs = [] # initialize list of dataframes
for year in lst_years: # go through each year we are observing
    df_temp = pd.read_csv(os.getcwd() +'/analysis/by_year/census_'+ str(year) +'.csv', low_memory=False, encoding='utf-8') # read dataframe
    lst_dfs.append(df_temp) # append dataframe to list

# Strip 'ZCTA5 ' from Name columns
for i in range(0,len(lst_years)): # go through each year we are observing
    lst_dfs[i]['NAME'] = lst_dfs[i]['NAME'].str.lstrip('ZCTA5 ')

print(lst_dfs[0])

# Subset ZCTA5s in NYC
lst_nyc_zips = list(range(10001,10282)) + list(range(10301,10314)) + list(range(10451,10475)) + list(range(11004,11109)) + list(range(11351,11697)) + list(range(11201,11256)) # create list of zipcodes
for i in range(0,len(lst_years)): # go through range of years
    lst_dfs[i]['NAME'] = lst_dfs[i][lst_dfs[i]['NAME'].isin(lst_nyc_zips)]

# Rename variables we want to look at
for i in range(0,len(lst_dfs)): # loop through all years
    lst_dfs[i] = lst_dfs[i].rename(columns = {
        'DP05_0001E': 'total_population', # find and rename total population
        'S1901_C01_012E': 'household_income', # find and rename household income
        'NAME': 'Zipcode' # change column name to zipcode
    }).copy()
for i in range(0,6): # loop through dataframes for 2011 to 2016
    lst_dfs[i] = lst_dfs[i].rename(columns = {
        'DP05_0017E' : 'median_age',# find and rename median age columns
        'DP05_0072E' : 'white_non-hispanic'# find and rename white non-hispanic
    }).copy()
for i in range(6,len(lst_dfs)): # loop through dataframes for 2017 to 2019
    lst_dfs[i] = lst_dfs[i].rename(columns = {
        'DP05_0018E' : 'median_age',# find and rename median age columns
        'DP05_0072E' : 'white_non-hispanic'# find and rename white non-hispanic
    }).copy()


# for i in range(0,len(lst_dfs)):
#     if 'white_non-hispanic' in lst_dfs[i].columns:
#         print(lst_years[i],i,'True')
#     else:
#         print(lst_years[i],i,'False')

# Subset to variables that we want to look at
# lst_features = ['Zipcode','total_population','median_age','white_non-hispanic','household_income'] # list of features we want to look at
# for i in range(0,len(lst_dfs)):
#     df_temp = lst_dfs[i]
#     lst_dfs[i] = df_temp[lst_features]

# print(lst_dfs[0]['Zipcode'])



for i in range(0,7): # loop through dataframes for 2011 to 2018
        lst_dfs[i] = lst_dfs[i].rename(columns = { 
        'DP02_0095E': 'foreign_born_not_a_us_citizen', # find and rename foreign born none us citizens
    }).copy()
lst_dfs[-1].rename(columns = {
    'DP02_0097E': 'foreign_born_not_a_us_citizen', # find and rename foreign born none us citizens
    'DP02_0065E': 'bachelors', # find and rename bachelors degrees
    }).copy()
for i in range(0,5):# loop through dataframes for 2011 to 2014
    lst_dfs[i] = lst_dfs[i].rename(columns = {
        'DP04_0132E': 'gross_rent_median_price'# find and rename rental cost
    }).copy()
for i in range(5,len(lst_dfs)):# loop through dataframes for 2015 to 2019
    lst_dfs[i] = lst_dfs[i].rename(columns = {
        'DP04_0134E': 'gross_rent_median_price'# find and rename rental cost
    }).copy()



# Subset to variables that we want to look at
lst_features = ['Zipcode','total_population','median_age','white_non-hispanic','household_income','foreign_born_not_a_us_citizen','bachelors','gross_rent_median_price'] # list of features we want to look at
for df in lst_dfs:
    df = df.loc[lst_features]

sys.exit(0)

for i in range(0,len(lst_dfs)):
    print(i)
    lst_dfs[i] = lst_dfs[i][lst_features]

sys.exit(0)


# Make strings into floats
for i in range(0,len(lst_years)): # go through range of years
    lst_dfs[i] = lst_dfs[i].apply(pd.to_numeric, errors='coerce')# change as many values into float64 as possible. ignore values that cannot be changed

# Get difference in values from first and last dataframe
lst_merged_zips = list(set(lst_dfs[0]) & set(lst_dfs[-1])).remove('NAME') # get list of features that are in both dataframes and remove 'NAME' column
df_merged = pd.merge(lst_dfs[0],lst_dfs[-1],how = 'inner', on = 'NAME', suffixes=['_start','_end'])# merge dataframes
df_delta = pd.DataFrame(df_merged['NAME'])# intialize dataframe
# for feature in df_merged.columns[1:]:# Go through each element of the list values
#     df_delta[feature] = df_merged[feature + '_start'] - df_merged[feature + '_end'] # get the change in census tracts

print(df_merged['GEO_ID_start_start'])


# # Remove NaN values if over 80% threshold
# int_thresh = round(len(df_data) * 0.8) # Get threshold to drop a row
# df_data = df_data.dropna(axis = 'columns', thresh = int_thresh) # Drop column if number of NAs exceeds threshold

# # Replace NA values with mean of column
# df_data = df_data.apply(lambda x: x.fillna(x.mean()),axis=0)








