
import pandas as pd
import json



# Step 1: Load the dataset
dataset = pd.read_json('intents.json')
#print(dataset.head())

# Step 2: Identify missing values
#print("Missing Values:", dataset.isnull().sum())

# Step 3: Analyze and Handle Missing Values

with open('intents.json', 'r') as file:
    data = json.load(file)

# Flatten JSON into a DataFrame
intents = data['intents']
dataset = pd.DataFrame(intents) 

#print(dataset.head()) 
 # Verify the DataFrame structure
dataset.dropna(subset=['patterns', 'responses'], inplace=True) 

# Step 4: Save the cleaned dataset
dataset.to_json('cleaned_intents.json', index=False)

# Step 5: Validate the dataset
print("Missing Values After Cleaning:", dataset.isnull().sum())
