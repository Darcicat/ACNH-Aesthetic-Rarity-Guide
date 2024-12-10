# ACNH-Aesthetic-Rarity-Guide
## Overview
This tool helps *Animal Crossing New Horizons (ACNH)* players cultivate a five-star island aesthetic by cataloging (surfacing?) item rarity and ideal gifts for the villagers inhabiting the island.

## Features
- **Item Rarity**: Identify whether an obtainable item in the game is common, normal, 
- **Villager Gift Recommendations**: Identify the best gifts for each villager based on their personality and style.

### Data Source
ACNH Aesthetic Rarity Guide leverages a public dataset found on Kaggle, [Animal Crossing New Horizon's Catalog](https://www.kaggle.com/datasets/jessicali9530/animal-crossing-new-horizons-nookplaza-dataset). The dataset contains 30 CSVs listing various items, villagers, clothing, and other collectibles from the game. 

## Project Structure
- **data**: Contains the raw data files.
- **cleaned_data**: Processed versions of the data files after cleaning.
- **notebooks**: Jupyter notebooks for data exploration and visualization.

## Getting Started
### Prerequisites
- Python
- pandas library
- numpy (?)
- jupyter notebook
- matplotlib

### Installation
1. Clone this repo.
2. Run initial setup and data cleaning scripts.
3. View results and analysis.

## Project Summary
### Rarity Analysis
#### Pre-work
#### Setting criteria and establishing logic
##### Defining an item
I went into this project knowing that the dataset included components from the game that don't make sense to be included in this analysis. For example, *reactions* and *achievements* are not items. I decided to limit the scope of the analysis to cover the following item types from the dataset: accessories, art, bags, dress-up, floors, headwear, bottoms, housewares, posters, socks, shoes, rugs, tops, umbrellas, wall-mounted, wallpaper. 

##### How to evaluate for rarity
I did some preliminary research on "rarity scales" and mirrored their language. I settled on a 4-point scale:
1. common
2. normal
3. scarce
4. rare
The rarity_analysis.ipnb notebook defines critera for each tier.

#### Summary of Findings




















