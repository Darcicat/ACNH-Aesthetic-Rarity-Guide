import pandas as pd
from load_python import load_data
def clean_concat_data(catalogs, output_file=r'C:\Users\Code Lou\Documents\ACNH_Aesthetic_Rarity_Guide\cleaned_data\rarity.csv'):
   #list the catalogs needed for rarity analysis
    relevant_catalogs = ['accessories', 'art', 'bags', 'bottoms', 'construction', 'dress-up', 'fencing', 'floors', 'fossils', 
    'headwear', 'housewares', 'miscellaneous', 'music', 'other', 'photos', 'posters', 'reactions', 'recipes', 'rugs', 'shoes', 
    'socks', 'tools', 'tops', 'umbrellas', 'wallpaper']
    dfs = []   #will hold the cleaned dataframes
    required_columns = ['Unique Entry ID', 'Name', 'Catalog','Source', 'Source Notes', 'Seasonal Availability'] #define the columns needed for the analysis
    for catalog_name in relevant_catalogs: #loop through the list above
        if catalog_name in catalogs: #check if the given catalog exists in the catalog dictionary
            df = catalogs[catalog_name] #retrieve the df corresponding to the given catalog_name
            for column in required_columns: #make sure all requirements are present
                if column not in df.columns:
                    df.loc[:, column] = "Not Applicable" #creates the column and sets a default value if it isn't present
            df = df[required_columns] #selects only the required columns, drops everything else
            df.loc[:, 'Item Type'] = catalog_name #indicates the original source/which catalog the item came from
            dfs.append(df) #add the cleaned dataframe to the list
        concat_df = pd.concat(dfs, ignore_index=True)
        concat_df.to_csv(output_file, index=False)
if __name__ == "__main__":
    catalogs = load_data() #load it
    clean_concat_data(catalogs) #clean and concat it