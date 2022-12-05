import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import os

# Read in gentrification metrics over time
df = pd.read_csv(os.getcwd() + '/analysis/gentrification_metric/2019_2011_gentrification_metrics.csv')

# Read data to be qureyed for each year
census_2011 = pd.read_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/query/census_2011.csv')
census_2012 = pd.read_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/query/census_2012.csv')
census_2013 = pd.read_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/query/census_2013.csv')
census_2014 = pd.read_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/query/census_2014.csv')
census_2015 = pd.read_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/query/census_2015.csv')
census_2016 = pd.read_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/query/census_2016.csv')
census_2017 = pd.read_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/query/census_2017.csv')
census_2018 = pd.read_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/query/census_2018.csv')
census_2019 = pd.read_csv('/home/matthewdshen/GitHub/urban_data_project/analysis/query/census_2019.csv')

# Look at astoria gentrification metrics
astoria_search = [11101,11102,11103,11105,11106]
df_astoria = df[df['NAME'].isin(astoria_search)].mean()
print('Astoria:\n',df_astoria)

# Look at upper east side gentrification metrics
ues_search = [10021, 10028, 10065, 10075,10128]
df_ues = df[df['NAME'].isin(ues_search)].mean()
print('Upper East Side:\n',df_ues)

# Look at morningside heights gentrification metrics
uws_search = [10027]
df_morningside_heights = df[df['NAME'].isin(uws_search)].mean()
print('Morningside Heights:\n',df_morningside_heights)

# Look at trump apartment buildings metrics(riverside park south)
trump = [10069]
df_trump = df[df['NAME'].isin(trump)].mean()
print('Morningside Heights:\n',df_trump)
# Subset trump zipcode data for all years
trump_census_2011 = census_2011[census_2011['NAME'].isin(trump)].mean()
trump_census_2012 = census_2012[census_2012['NAME'].isin(trump)].mean()
trump_census_2013 = census_2013[census_2013['NAME'].isin(trump)].mean()
trump_census_2014 = census_2014[census_2014['NAME'].isin(trump)].mean()
trump_census_2015 = census_2015[census_2015['NAME'].isin(trump)].mean()
trump_census_2016 = census_2016[census_2016['NAME'].isin(trump)].mean()
trump_census_2017 = census_2017[census_2017['NAME'].isin(trump)].mean()
trump_census_2018 = census_2018[census_2018['NAME'].isin(trump)].mean()
trump_census_2019 = census_2019[census_2019['NAME'].isin(trump)].mean()

# Plot houshold income in trump zipcode vs year
income = [trump_census_2011['household_income'], trump_census_2012['household_income'], trump_census_2013['household_income'], trump_census_2014['household_income'], trump_census_2015['household_income'], trump_census_2016['household_income'], trump_census_2017['household_income'], trump_census_2018['household_income'], trump_census_2019['household_income']]
year = list(range(2011,2020))
fig, ax = plt.subplots(1, 1)
plt.scatter(year,income) # plot scatter of income vs year
plt.title('Household Income over Time at ZCTA5 10069') # set title
# Set y tickmarks to money
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
plt.savefig(os.getcwd() + '/outbound/images/Household Income over Time at ZCTA5 10069.png')


