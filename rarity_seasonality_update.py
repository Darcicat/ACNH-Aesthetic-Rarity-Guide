import pandas as pd
from rarity_concat import load_data
def clean_source_notes(rarity_df, output_file=r'C:\Users\Code Lou\Documents\ACNH_Aesthetic_Rarity_Guide\cleaned_data\rarity2.csv'):
    #handle Fall
    rarity_df.loc[rarity_df['Source Notes'] == 'only available during Fall', 'Seasonal Availability'] = 'Fall'
    rarity_df.loc[rarity_df['Source Notes'].str.contains('Mushroom Season', na=False), 'Seasonal Availability'] = 'Fall' #mushroom season is Nov 1-30
    rarity_df.loc[rarity_df['Source Notes'].str.contains('Maple Leaf Season', na=False), 'Seasonal Availability'] = 'Fall' #maple leaf season is Nov 16-25
    #handle Spring
    rarity_df.loc[rarity_df['Source Notes'] == 'only available during Spring', 'Seasonal Availability'] = 'Spring'
    rarity_df.loc[rarity_df['Source Notes'].str.contains('Cherry-Blossom Season', na=False), 'Seasonal Availability'] = 'Spring' #cherry-blossom season is April 1-10
    #handle Winter
    rarity_df.loc[rarity_df['Source Notes'] == 'only available during Winter', 'Seasonal Availability'] = 'Winter'
    rarity_df.loc[rarity_df['Source Notes'].str.contains('Festive Season', na=False), 'Seasonal Availability'] = 'Winter' #festive season is Dec 15- Jan 6
    #handle Summer
    rarity_df.loc[rarity_df['Source Notes'] == 'only available during Summer', 'Seasonal Availability'] = 'Summer'
    rarity_df.loc[rarity_df['Source Notes'].str.contains('Wedding Season', na=False), 'Seasonal Availability'] = 'Summer' #wedding season is June 1-30

    rarity_df.to_csv(output_file, index=False)
    print(f'Cleaned data saved to {output_file}')

  
if __name__ == "__main__":
    rarity_df = pd.read_csv(r'C:\Users\Code Lou\Documents\ACNH_Aesthetic_Rarity_Guide\cleaned_data\rarity.csv') #load it
    clean_source_notes(rarity_df) #clean it