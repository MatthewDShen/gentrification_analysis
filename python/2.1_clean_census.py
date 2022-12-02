import pandas as pd
import os

# Read in CSVs
lst_years = range(2011,2019) # range of years we are observing
lst_dfs = [] # initialize list of dataframes
for year in lst_years: # go through each year we are observing
    df_temp = pd.read_csv(os.getcwd() +'/analysis/by_year/census_'+ str(year) +'.csv', low_memory=False, encoding='utf-8') # read dataframe
    lst_dfs.append(df_temp) # append dataframe to list

# Strip 'ZCTA5 ' from Name columns
for i in range(0,len(lst_years)): # go through each year we are observing
    lst_dfs[i]['NAME'] = lst_dfs[i]['NAME'].str.lstrip('ZCTA5 ')

# Subset ZCTA5s in NYC
lst_nyc_zips = list(range(10001,10282)) + list(range(10301,10314)) + list(range(10451,10475)) + list(range(11004,11109)) + list(range(11351,11697)) + list(range(11201,11256)) # create list of zipcodes
for i in range(0,len(lst_years)): # go through range of years
    df_temp = lst_dfs[i] # set up temp dataframe
    lst_dfs[i] = df_temp[df_temp['NAME'].isin(lst_nyc_zips)] # remove values that are not in nyc zipcode list

# Make strings into floats
for i in range(0,len(lst_years)): # go through range of years
    lst_dfs[i] = lst_dfs[i].apply(pd.to_numeric, errors='coerce')# change as many values into float64 as possible. ignore values that cannot be changed

# Get difference in values from first and last dataframe
lst_features = list(set(lst_dfs[0]) & set(lst_dfs[-1])).remove('NAME') # get list of features that are in both dataframes and remove 'NAME' column
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








