import os
import pandas as pd
from pathlib import Path

def load_data(data_folder='data'): # load all CSV files in the data folder.
    all_data = {}
    notebook_dir = Path(os.getcwd()) # gets the current working directory of the jupyter notebook
    data_path = notebook_dir.parent / data_folder # move up the directory & access 'data' folder.

    if not data_path.exists(): # check if 'data' folder exists before trying to read files from it.
        raise FileNotFoundError(f"Data folder '{data_path}' not found.")

    for file in os.listdir(data_path): # loop through all files.
        if file.endswith('.csv'):
            catalog_name = file.replace('.csv', '') # maintain file name (but drop '.csv') as the dictionary key.
            df = pd.read_csv(data_path / file) # convert csv into dataframe.
            all_data[catalog_name] = df 
            print(f'Loaded {catalog_name} with {df.shape[0]} rows and {df.shape[1]} columns.') # confirms each file loaded with its dimensions.
    return all_data
if __name__ == "__main__":
    catalogs = load_data()