import pandas as pd

# Read in CSVs
census_2011 = pd.read_csv("/home/matthewdshen/GitHub/urban_data_project/analysis/by_year/censuse_data_2011.csv", low_memory=False)
census_2012 = pd.read_csv("/home/matthewdshen/GitHub/urban_data_project/analysis/by_year/censuse_data_2012.csv", low_memory=False)
census_2013 = pd.read_csv("/home/matthewdshen/GitHub/urban_data_project/analysis/by_year/censuse_data_2013.csv", low_memory=False)
census_2014 = pd.read_csv("/home/matthewdshen/GitHub/urban_data_project/analysis/by_year/censuse_data_2014.csv", low_memory=False)
census_2015 = pd.read_csv("/home/matthewdshen/GitHub/urban_data_project/analysis/by_year/censuse_data_2015.csv", low_memory=False)
census_2016 = pd.read_csv("/home/matthewdshen/GitHub/urban_data_project/analysis/by_year/censuse_data_2016.csv", low_memory=False)
census_2017 = pd.read_csv("/home/matthewdshen/GitHub/urban_data_project/analysis/by_year/censuse_data_2017.csv", low_memory=False)
census_2018 = pd.read_csv("/home/matthewdshen/GitHub/urban_data_project/analysis/by_year/censuse_data_2018.csv", low_memory=False)
census_2019 = pd.read_csv("/home/matthewdshen/GitHub/urban_data_project/analysis/by_year/censuse_data_2019.csv", low_memory=False)

# Change variable names to be more descriptive
for i in [census_2011, census_2012, census_2013, census_2014, census_2015, census_2016, census_2017, census_2018, census_2019]:
    i['bachelors'] = i['DP02_0064E']
    i['graduate'] = i['DP02_0065E']
    i['household'] = i['S1901_C01_012E']
    i['foreign-born-non-us'] = i['DP02_0095E']
    i['family'] = i['S1901_C02_012E']
    i['nonfamily-households'] = i['S1901_C04_012E']
    i['married-couple-families'] = i['S1901_C03_012E']
    i['ZCTA5'] = i['NAME'][-5:]

for i in [census_2011, census_2012, census_2013, census_2014, census_2015, census_2016]:
    i['white_non_hispanic'] = i['DP05_0072E']
    i['median_age'] = i['DP05_0017E']

for i in [census_2011, census_2012, census_2013, census_2014]:
    i['gross_rent'] = i['DP04_0132E']

for i in [census_2015, census_2016]:
    i['gross_rent'] = i['DP04_0134E']

for i in [census_2017, census_2018, census_2019]:
    i['gross_rent'] = i['DP04_0134E']
    i['white_non_hispanic'] = i['DP05_0077E']
    i['median_age'] = i['DP05_0018E']



# Subset data to only include information we need
census_2011 = census_2011[['ZCTA5', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2012 = census_2012[['ZCTA5', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2013 = census_2013[['ZCTA5', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2014 = census_2014[['ZCTA5', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2015 = census_2015[['ZCTA5', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2016 = census_2016[['ZCTA5', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2017 = census_2017[['ZCTA5', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2018 = census_2018[['ZCTA5', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2019 = census_2019[['ZCTA5', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]



def normalize(df):
    '''The following function makes all the data into floats or deletes it and then normalizes the data'''
    result = df.copy()
    for feature_name in df.columns:
        df[feature_name] = df[feature_name].apply(pd.to_numeric, errors='coerce')
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

# Run normalization function
census_2011 = normalize(census_2011)
census_2012 = normalize(census_2012)
census_2013 = normalize(census_2013)
census_2014 = normalize(census_2014)
census_2015 = normalize(census_2015)
census_2016 = normalize(census_2016)
census_2017 = normalize(census_2017)
census_2018 = normalize(census_2018)
census_2019 = normalize(census_2019)

# Write census data to csv
census_2011 = census_2011.to_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/normalized/census_2011.csv')
census_2012 = census_2012.to_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/normalized/census_2012.csv')
census_2013 = census_2013.to_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/normalized/census_2013.csv')
census_2014 = census_2014.to_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/normalized/census_2014.csv')
census_2015 = census_2015.to_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/normalized/census_2015.csv')
census_2016 = census_2016.to_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/normalized/census_2016.csv')
census_2017 = census_2017.to_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/normalized/census_2017.csv')
census_2018 = census_2018.to_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/normalized/census_2018.csv')
census_2019 = census_2019.to_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/normalized/census_2019.csv')




