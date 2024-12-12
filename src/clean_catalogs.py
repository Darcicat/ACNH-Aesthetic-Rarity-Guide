import pandas as pd
from initial_load import load_data
from pathlib import Path
import os

def clean_catalog(df, catalog_name, required_columns):
    """Cleans a single catalog DataFrame."""
    df = df.copy()
    for column in required_columns:
        if column not in df.columns:
            df.loc[:, column] = "Not Applicable"  # Add missing columns with default value
    df = df[required_columns]  # Select only the required columns
    df.loc[:, 'Item Type'] = catalog_name  # Add a column to indicate the catalog source
    return df

def clean_and_concat_catalogs(catalogs):
    """Cleans and concatenates all relevant catalogs into a single DataFrame."""
    relevant_catalogs = [
        'accessories', 'art', 'bags', 'bottoms', 'dress-up', 'headwear', 'housewares', 'rugs', 'shoes', 'socks', 'tools', 'tops', 'umbrellas'
    ]
    required_columns = [
        'Unique Entry ID', 'Name', 'Catalog', 'Source', 'Source Notes', 
        'Seasonal Availability', 'Buy'
    ]
    dfs = []
    for catalog_name in relevant_catalogs:
        if catalog_name in catalogs:
            df = catalogs[catalog_name].copy()
            cleaned_df = clean_catalog(df, catalog_name, required_columns)
            dfs.append(cleaned_df)
    concat_df = pd.concat(dfs, ignore_index=True)
    return concat_df

def update_seasonal_availability(rarity_df):
    """Updates the 'Seasonal Availability' column based on 'Source' and 'Source Notes'."""
    # Define exact match
    seasonal_mapping = {
        'only available during Winter': 'Winter',
        'only available during Fall': 'Fall',
        'only available during Summer': 'Summer',
        'only available during Spring': 'Spring'
    }
    for column in ['Source Notes', 'Source']:
        for source_value, season in seasonal_mapping.items():
            rarity_df.loc[rarity_df[column] == source_value, 'Seasonal Availability'] = season

    # Define partial match
    partial_mapping = {
        'Festive Season': 'Winter', 
        'January 20 - February 18': 'Winter',
        'Dec 22 - Jan 19': 'Winter',
        'February 19 - March 20': 'Winter',
        'Winter': 'Winter',
        'Mushroom Season': 'Fall',
        'Maple Leaf Season': 'Fall',
        'September 23 - October 22': 'Fall',
        'November 22 - December 21': 'Fall',
        'October 23 - November 21': 'Fall',
        'Fall': 'Fall',
        'Wedding Season': 'Summer',
        'June 21 - July 22': 'Summer',
        'May 21 - June 20': 'Summer',
        'July 23 - August 22': 'Summer', 
        'August 23 - September 22': 'Summer',
        'Summer': 'Summer',
        'Cherry-Blossom Season': 'Spring',
        'March 21 - April 19': 'Spring',
        'April 20 - May 20': 'Spring',
        'Spring': 'Spring'
    }
    for column in ['Source Notes', 'Source']:
        for partial_value, season in partial_mapping.items():
            rarity_df.loc[rarity_df[column].str.contains(partial_value, na=False), 'Seasonal Availability'] = season
    return rarity_df

def save_to_csv(df, filename, folder='cleaned_data'):
    """Saves the DataFrame to a specified folder and filename."""
    src_dir = Path(os.getcwd())
    project_root = src_dir.parent
    output_path = project_root / folder / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}.")

def load_cleaned_data():
    """Loads the cleaned, concatenated catalog csv."""
    src_dir = Path(__file__).resolve().parent #locate directory
    project_root = src_dir.parent #move up to project root
    cleaned_csv_path = project_root / 'cleaned_data' / 'items_for_rarity.csv'

    if not cleaned_csv_path.exists():
        raise FileNotFoundError(f"Cleaned data file not found: {cleaned_csv_path}")
    return pd.read_csv(cleaned_csv_path)

def main():
    catalogs = load_data()
    print("Catalogs loaded successfully.")
    
    # Step 1: Clean and concatenate catalogs
    concat_df = clean_and_concat_catalogs(catalogs)
    print(f"Concatenated DataFrame shape: {concat_df.shape}")
    
    # Step 2: Update Seasonal Availability
    updated_df = update_seasonal_availability(concat_df)
    print(f"Updated Seasonal Availability for {updated_df.shape[0]} rows.")
    
    # Step 3: Save to CSV
    save_to_csv(updated_df, filename='items_for_rarity.csv')

if __name__ == "__main__":
    main()