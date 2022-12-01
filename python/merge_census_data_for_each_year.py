import pandas as pd
import glob
import os

def func_csv_file_names(path):
    '''Given the path of a folder in your system, creates a list of strings that are the paths for any csv file in the folder with the term "Data" in them'''

    # Create list of csv files from given folder path
    lst_csv_files = glob.glob(os.path.join(path, "*.csv"))
    
    # Takes and stores all csv paths with the term "Data" in them
    lst_data_files = []
    for i in range(0,len(lst_csv_files)):
        if lst_csv_files[i].find('Data') > 0:
            lst_data_files.append(lst_csv_files[i])
        else:
            pass
    
    # Return list of strings that are the paths for any csv file in the folder with the term "Data" in them
    return lst_data_files

def func_all_data_in_folder(lst_census_types,path):
    '''Given a list of the types of census data titles and the path of a folder. 
    Create a list of all csv files with the term data in them'''

    # Loop through each census type and store list of paths for each csv
    lst_all_data_paths = []
    for i in range(0,len(lst_census_types)):
        lst_all_data_paths = lst_all_data_paths + func_csv_file_names(path + lst_census_types[i])

    # Return list of all csv files with the term data in them
    return lst_all_data_paths

def func_single_year_paths(year,lst_census_types,path):
    '''Given a the year, a list of census types, and the path of a folder. 
    Create a list of paths for a single year'''
    
    # Get list of all data paths for all types
    lst_all_data_paths = func_all_data_in_folder(lst_census_types,path)

    # Loop through and store all path that match a certain year
    lst_single_year_paths = []
    for i in range(0,len(lst_all_data_paths)):
        if lst_all_data_paths[i].find(year) > 0:
            lst_single_year_paths.append(lst_all_data_paths[i])
        else:
            pass

    # Return a list of paths for a single year
    return lst_single_year_paths

def func_write_csv_single_year(lst_years,lst_census_types,path):
    '''Given a list of years, list of census types, and a folder path. Create a csv for each year containing all census data'''

    # Loop through each year of census data we are looking at
    for i in lst_years:
        
        # Get a list of paths for the year we are looking at
        lst_single_year_paths= func_single_year_paths(i,lst_census_types,path)

        # Read and store all csv into a single dataframe for the year we are looking at
        df_single_year = pd.DataFrame()
        for j in lst_single_year_paths:
            df_single_dataset = pd.read_csv(j, skiprows = [1], low_memory = False) # skip second row of data b/c contains description of column type. This messes up the dtype of the column.
            df_single_year = pd.concat([df_single_year, df_single_dataset])

        # Write a csv of all dataframe for a single year
        df_single_year.to_csv('C:\\Users\\abonc\\OneDrive\\GitHub\\urban_data_project\\analysis\\cleaned_features_test' + i + '.csv')

lst_years = ['2011','2012','2013','2014','2015','2016','2017','2018','2019']
lst_census_types = ['DP02','DP04','DP05','S1901']
path = 'C:\\Users\\abonc\\OneDrive\\Documents\\GitHub\\urban_data_project\\inbound\\census_data'

func_write_csv_single_year(lst_years,lst_census_types,path)
