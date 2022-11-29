import pandas as pd

census_2011 = pd.read_csv("inbound/census_data/by_year/censuse_data_2011.csv", low_memory=False)
census_2012 = pd.read_csv("inbound/census_data/by_year/censuse_data_2012.csv", low_memory=False)
census_2013 = pd.read_csv("inbound/census_data/by_year/censuse_data_2013.csv", low_memory=False)
census_2014 = pd.read_csv("inbound/census_data/by_year/censuse_data_2014.csv", low_memory=False)
census_2015 = pd.read_csv("inbound/census_data/by_year/censuse_data_2015.csv", low_memory=False)
census_2016 = pd.read_csv("inbound/census_data/by_year/censuse_data_2016.csv", low_memory=False)
census_2017 = pd.read_csv("inbound/census_data/by_year/censuse_data_2017.csv", low_memory=False)
census_2018 = pd.read_csv("inbound/census_data/by_year/censuse_data_2018.csv", low_memory=False)
census_2019 = pd.read_csv("inbound/census_data/by_year/censuse_data_2019.csv", low_memory=False)

for i in [census_2011, census_2012, census_2013, census_2014, census_2015, census_2016, census_2017, census_2018]:
    i['bachelors'] = i['DP02_0064E']
    i['graduate'] = i['DP02_0065E']
    i['household'] = i['S1901_C01_012E']
    i['foreign-born-non-us'] = i['DP02_0095E']
    i['family'] = i['S1901_C02_012E']
    i['nonfamily-households'] = i['S1901_C04_012E']
    i['married-couple-families'] = i['S1901_C03_012E']
    i['zip'] = i['NAME'].apply(lambda x: x.strip('ZCTA5'))

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



census_2019['bachelors'] = census_2019['DP02_0065E']
census_2019['graduate'] = census_2019['DP02_0066E']
census_2019['household'] = census_2019['S1901_C01_012E']
census_2019['foreign-born-non-us'] = census_2019['DP02_0096E']
census_2019['family'] = census_2019['S1901_C02_012E']
census_2019['nonfamily-households'] = census_2019['S1901_C04_012E']
census_2019['married-couple-families'] = census_2019['S1901_C03_012E']
census_2019['zip'] = census_2019['NAME'].apply(lambda x: x.strip('ZCTA5'))




census_2011 = census_2011[['zip', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2012 = census_2012[['zip', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2013 = census_2013[['zip', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2014 = census_2014[['zip', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2015 = census_2015[['zip', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2016 = census_2016[['zip', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2017 = census_2017[['zip', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2018 = census_2018[['zip', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]
census_2019 = census_2019[['zip', 'bachelors', 'graduate', 'household', 'foreign-born-non-us', 'family', 'nonfamily-households', 'nonfamily-households', 'married-couple-families', 'gross_rent', 'median_age', 'white_non_hispanic']]


def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        df[feature_name] = df[feature_name].apply(pd.to_numeric, errors='coerce')
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

census_2011 = normalize(census_2011)
census_2012 = normalize(census_2012)
census_2013 = normalize(census_2013)
census_2014 = normalize(census_2014)
census_2015 = normalize(census_2015)
census_2016 = normalize(census_2016)
census_2017 = normalize(census_2017)
census_2018 = normalize(census_2018)
census_2019 = normalize(census_2019)