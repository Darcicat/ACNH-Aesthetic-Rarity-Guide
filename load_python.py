import os
import pandas as pd

def load_data(data_folder='data'): # load all CSV files in the data folder.
    all_data = {}
    for file in os.listdir(data_folder): #loop through all files.
        if file.endswith('2.csv'):
            catalog_name = file.replace('.csv', '') #maintain file name (but drop '.csv') as the dictionary key.
            df = pd.read_csv(os.path.join(data_folder, file)) #convert csv into dataframe.
            all_data[catalog_name] = df 
            print(f'Loaded {catalog_name} with {df.shape[0]} rows and {df.shape[1]} columns.') #confirms each file loaded with its dimensions.
    return all_data
if __name__ == "__main__":
    catalogs = load_data()