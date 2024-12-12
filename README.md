# ACNH-Aesthetic-Rarity-Guide
## Overview
This tool helps *Animal Crossing New Horizons (ACNH)* players cultivate a five-star island aesthetic by surfacing item rarity and ideal gifts for the villagers inhabiting the island.

- **Item Rarity**: Identify whether an obtainable item in the game is common, normal, scarce, or rare.
- **Villager Gift Recommendations**: Identify the best gifts for each villager based on their personality and style.

### Data Source
ACNH Aesthetic Rarity Guide leverages a public dataset found on Kaggle, [Animal Crossing New Horizon's Catalog](https://www.kaggle.com/datasets/jessicali9530/animal-crossing-new-horizons-nookplaza-dataset). The dataset contains 30 CSVs listing various items, villagers, clothing, and other collectibles from the game. 

## Capstone Project Features
**Loading data**
- Read at least two data files (CSVs).

**Clean and operate on the data while combining them**
- Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.

**Best practices: Enhance your project to a higher tier that will impress employers and help other programmers understand your project.**
- Utilize a virtual environment and include instructions in your README on how the user should set one up.
- Build a custom data dictionary and include it either in your README or as a separate document.
  
**Interpretation of your data.**
- Annotate your code with markdown cells in Jupyter Notebook, write clear code comments, and have a well-written README.md. Tidy up your notebook, and make sure you don’t have any empty cells or incomplete cells that don’t do anything. Make sure it’s all functional before your final github commit.

## Project Structure
- **data**: Contains the raw data files, as well as a data dictionary.
- **cleaned_data**: Processed versions of the data files after cleaning.
- **notebooks**: Jupyter notebooks for data exploration and visualization.
- **src**: Contains python scripts that process the data.

## Getting Started
### Prerequisites
- Python
- pandas library
- numpy
- jupyter notebook

### Installation
1. Clone this repo (https://github.com/Darcicat/ACNH-Aesthetic-Rarity-Guide.git).
2. Run initial setup and data cleaning scripts located in the src directory: initial_load.py and clean_catalogs.py
3. View results and analysis in Juypter Notebook.

## Project Summary
### Rarity Analysis
#### Pre-work
#### Setting criteria and establishing logic
##### Defining an item
I went into this project knowing that the dataset included components from the game that don't make sense to be included in this analysis. For example, *achievements* are not items. I decided to limit the scope of the analysis to cover the following item types from the dataset: accessories, art, bags, bottoms, dress-up, headwear, housewares, rugs, shoes, socks, tools, tops, umbrellas,

##### How to evaluate for rarity
I did some preliminary research on "rarity scales" and mirrored their language. I settled on a 4-point scale:
1. common
2. normal
3. scarce
4. rare

Through exploring the dataset, I determined the following criteria for the scale:

**Common Items** are easily  accessible and widely obtainable through normal gameplay without significant effort. Examples:
* Items purchasable from Nook's Cranny year-round.
* Items craftable with readily available DIY recipes (e.g. wood furniture)

**Normal Items** are tied to the main storyline or early-game progression that every player encounters. Examples:
* Items given by Tom Nook, Isabelle, or villagers as part of tutorials or early milestones.
* Items obtained by completing museum milestones.

**Scarce Items** have limited availability, and are tied to specific events or chance-based systems.
* Items from seasonal events, such as Birthday or Turkey Day.
* Items left to chance, such as rugs from Sahara or artifacts from Gulliver's travels.

**Rare Items** require significant effort, advanced progression, or special conditions to obtain. Examples:
* Items that are high-cost.
* Items requiring a 5-star island rating.
* Balloon-only DIYs.
* Friendship-level exclusives.


#### Summary of Findings
