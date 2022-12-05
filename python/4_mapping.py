import pandas as pd, geopandas as gpd, matplotlib.pyplot as plt, os

# Read in shape file with ZCTA for NYC
gdf_zip_code_map = gpd.read_file(os.getcwd() + '/inbound/shapefile/Modified Zip Code Tabulation Areas (MODZCTA).zip')

# Subset to only include ZCTA5 and geometry
gdf_zip_code_map = gdf_zip_code_map[['modzcta','geometry']]

# plot NYC zip codes on map
gdf_zip_code_map.plot(figsize=[15,15],color='#f7f1ebff',linewidth=1, edgecolor='#fe98b1').set(title='NYC Map by Zip Code')
plt.tick_params(left = False, right = False , labelleft = False, labelbottom = False, bottom = False) # remove tick marks
plt.savefig(os.getcwd() + '/outbound/images/zip_code_map.png') # save map as png

# Read in census gentrification metric csv
df_gentrification_metric = pd.read_csv(os.getcwd() + '/analysis/gentrification_metric/2019_2011_gentrification_metrics.csv')
df_gentrification_metric['NAME']=df_gentrification_metric['NAME'].astype(str)
df_gentrification_metric.rename(columns={'NAME':'Zip Code'},inplace=True)

# Merge NYC zip code shape file with gentrification metric dataframe
gdf_map_gentrification = pd.merge(gdf_zip_code_map, df_gentrification_metric, left_on='modzcta', right_on='Zip Code', how='left')

# Plot gentrification metric
gdf_map_gentrification.plot(column='gentrification_metric',legend=True,figsize=[10,10], cmap='PiYG',linewidth=0.1, edgecolor='grey').set(title='Gentrification Score from 2011 to 2019 by Zip Code')
plt.tick_params(left = False, right = False , labelleft = False, labelbottom = False, bottom = False) # remove tick marks
plt.savefig(os.getcwd() + '/outbound/images/gentrification_map.png') # save map as png

# sort by most gentrified zip codes
gdf_gentrification=gdf_map_gentrification[['Zip Code','gentrification_metric']]
gdf_gentrification.sort_values(by='gentrification_metric',ascending=False,inplace=True)
print('Most gentrified zipcodes\n',gdf_gentrification.head(10))
print('Least gentrified zipcodes:\n',gdf_gentrification.tail(10))
