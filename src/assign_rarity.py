import pandas as pd

def add_rarity_column(df):
    def assign_rarity(row):
       
        source = str(row['Source']).lower()  # Convert to strings first to avoid AttributeError
        source_notes = str(row['Source Notes']).lower()  # Convert to strings first to avoid AttributeError
        item_type = str(row['Item Type']).lower() # get Item Type and convert to lowercase
        genuine = str(row['Genuine']).lower() # Convert to strings first to avoid AttributeError
       
        # Common items
        # check if Source contains "Nook's Cranny", "Able Sisters", "DIY", or "Crafting" and if Seasonal Availability contains "All Year" or "Not Applicable"
        if pd.Series(["Nook's Cranny", 'Able Sisters', 'DIY', 'Crafting']).str.contains(source, case=False).any() and (row['Seasonal Availability'] == 'All Year' or row['Seasonal Availability'] == 'Not Applicable'):
            return 'Common'
        
        # Normal items
        # check if Source Notes contains "main storyline", "Starting items","certain numbers of flights", or if source contains"Recycle bin", "mom", "villager"
        elif (
            'villager' in source or 
            'Mom' in source or 
            'Starting items' in source or 
            'Recycle bin' in source or 
            'main storyline' in source_notes or 
            'certain numbers of flights' in source_notes or
            'No' in genuine
        ):
            return 'Normal'
       
        # Scarce items
        # Check if Source contains seasonal or chance-specific
        elif pd.Series(['Balloon', 'Birthday', 'Bug-Off', 'Flick', 'C.J.', 'Kicks', 'Labelle', 'Fishing Tourney', 'Bunny Day', 'Festival', 'Sahara', 'May Day Tour', "International Children's Day"]).str.contains(source, case=False).any() or row['Seasonal Availability'] not in ['All Year', 'Not Applicable']:
            return 'Scarce'
       
        # Rare items
        elif item_type == 'art' and genuine == 'Yes':
            return 'Rare'
        elif pd.Series(['Nook Shopping Promotion', 'Gulliver']).str.contains(source, case=False).any() or 'High Friendship' in source_notes:
            return 'Rare'

        # if item doesn't meet the above conditions - default fallback
        return 'unknown'

    df['Rarity'] = df.apply(assign_rarity, axis=1) # creates the column and assigns value across all rows
    return df

# Read in CSV from cleaned_data folder
input_file = '../cleaned_data/items.csv' # goes up a directory to the project root, then back into the cleaned data folder to access the CSV
df = pd.read_csv(input_file)

df = add_rarity_column(df) # applies the function to assign rarity & estalish the column

output_file = '../cleaned_data/items_with_rarity.csv'
df.to_csv(output_file, index=False)

print(f"File processed and saved as {output_file}")
        