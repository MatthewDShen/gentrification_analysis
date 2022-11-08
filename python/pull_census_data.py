import pandas as pd
import glob
import os

def func_csv_file_names(path):
    csv_files = glob.glob(os.path.join(path, "*.csv"))
    
    lst_data_files = []
    for i in range(0,len(csv_files)):
        if csv_files[i].find('Data') > 0:
            lst_data_files.append(csv_files[i])
        else:
            pass
    
    return lst_data_files

def func_all_data_in_folder(lst_census_types,path):

    lst_all_data_paths = []
    for i in range(0,len(lst_census_types)):
        lst_all_data_paths = lst_all_data_paths + func_csv_file_names(path + lst_census_types[i])

    return lst_all_data_paths

def func_single_year_paths(year,lst_census_types,path):

    lst_all_data_paths = func_all_data_in_folder(lst_census_types,path)

    lst_single_year_paths = []
    for i in range(0,len(lst_all_data_paths)):
        if lst_all_data_paths[i].find(year) > 0:
            lst_single_year_paths.append(lst_all_data_paths[i])
        else:
            pass

    return lst_single_year_paths

def func_write_csv_single_year(lst_years,lst_census_types,path):
    for i in lst_years:
        lst_single_year_paths= func_single_year_paths(i,lst_census_types,path)

        df_single_year = pd.DataFrame()

        for j in lst_single_year_paths:
            df_single_dataset = pd.read_csv(j, skiprows = [1], low_memory = False)
            df_single_year = pd.concat([df_single_year, df_single_dataset])

        df_single_year.to_csv('/home/matthewdshen/GitHub/urban_data_project/inbound/census_data/by_year/censuse_data_' + i + '.csv')



lst_years = ['2010','2011','2012','2013','2014','2015','2016','2017','2018']
lst_census_types = ['DP02','DP04','DP05','S1901']
path = '/home/matthewdshen/GitHub/urban_data_project/inbound/census_data/'

func_write_csv_single_year(lst_years,lst_census_types,path)












