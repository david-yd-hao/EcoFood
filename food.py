# ------------------------------------------------------------------------
# EcoFood
# Copyright (c) 2022 OpenAI-Hackathon Team 34. All Rights Reserved.
# Licensed under the MIT-style license found in the LICENSE file in the root directory
# ------------------------------------------------------------------------


import numpy as np
import pandas as pd

from mapping_data import return_mapping
from get_all_recipes import get_recipe_ingredients

beef_1 = [[0.45, "Beef, T-bone steak, raw", "BEEF BONE FREE MEAT*"], [0.06, "Lime, raw", "LIME"], [0.06, "Soya sauce", "SOY SAUCE"], [0.015, "Sugar, brown", "CANE SUGAR"], [0.015, "Sunflower oil", "SUNFLOWER OIL"], [0.005, "Ginger root, raw", "GINGER"], [0.006, "Garlic, raw", "GARLIC"], [0.001, "Pepper, black", "PEPPER (PIPER SPP.)"], [0.5, "Lettuce, iceberg (incl. crisphead types), raw", "LETTUCE"], [0.2, "Cucumber, raw", "CUCUMBER"], [0.06, "Peanuts, oilroasted and salted","PEANUT"]]

beef_2 = [[0.45, "Beef, mince, 15-20% fat, raw", "BEEF BONE FREE MEAT*"], [0.06, "Onion, raw", "ONION"]]

beef_3 = [[0.45, "Beef, fillet, defatted, raw", "BEEF BONE FREE MEAT*"], [0.17, "Onion, raw", "ONION"], [0.13, "Marinated grilled peppers", "PEPPER"], [0.05, "Tomato, ripe, raw, origin unknown", "TOMATO"], [0.45, "Chickpeas, canned", "CHICKPEA"], [0.12, "Yogurt plain, whole milk", "YOGURT WHITE"]]

beef_5 = [[0.45, "Beef, T-bone steak, raw", "BEEF BONE FREE MEAT*"], [0.015, "Olive oil", "OLIVE OIL"], [0.002, "Pepper, black", "PEPPER (PIPER SPP.)"]]

chicken_2 = [[0.45, "Chicken, breast, flesh and skin, raw", "CHICKEN BONE FREE MEAT"], [0.06, "Soya sauce","SOY SAUCE"], [0.06, "Sugar, brown", "CANE SUGAR"], [0.015, "Soya sauce", "SOY SAUCE"], [0.015, "Sunflower oil", "SUNFLOWER OIL"], [0.02, "Garlic, raw", "GARLIC"], [0.002, "Pepper, sweet, red, raw", "PEPPER (PIPER SPP.)"]]

chicken_4 = [[0.45, "Chicken, breast, flesh and skin, raw", "CHICKEN BONE FREE MEAT"], [0.06, "Wheat, flour, wholemeal", "WHEAT FLOUR"], [0.03,"Olive oil", "OLIVE OIL"], [0.12, "Chicken, whole", "CHICKEN MEAT WITH BONE*"], [0.06, "Ice, popsickle, lemonade", "LEMON"], [0.001, "Pepper, black", "PEPPER (PIPER SPP.)"]]

chicken_5 = [[0.17, "Chicken, breast, flesh and skin, raw", "CHICKEN BONE FREE MEAT"], [0.25, "Tomato, ripe, raw, origin unknown", "TOMATO"], [0.001, "Garlic, raw", "GARLIC"]]

salmon_1 = [[0.68, "Salmon, Atlantic, wild, raw", "SALMON"], [0.4, "Broccoli, raw", "BROCCOLI"], [0.015, "Mustard, yellow, ready made", "MUSTARD SEED"], [0.015, "Olive oil", "OLIVE OIL"]]

salmon_2 = [[0.45, "Salmon, Atlantic, wild, raw", "SALMON"], [0.06, "Mustard, yellow, ready made", "MUSTARD SEED"], [0.001, "Pepper, black", "PEPPER (PIPER SPP.)"], [0.4, "Broccoli, raw", "BROCCOLI"], [0.015, "Olive oil", "OLIVE OIL"], [0.001, "Pepper, black", "PEPPER (PIPER SPP.)"]]

salmon_3 = [[0.45, "Salmon, Atlantic, wild, raw", "SALMON"], [0.24, "Green beans, frost", "BEAN"], [0.24, "Broccoli, raw", "BROCCOLI"], [0.06, "Mustard, yellow, ready made", "MUSTARD SEED"], [0.06, "Wine, white, average values", "WINE*"], [0.06, "Olive oil", "OLIVE OIL"]]

salmon_4 = [[0.68, "Salmon, Atlantic, wild, raw", "SALMON"], [0.03, "Mustard, yellow, ready made", "MUSTARD SEED"], [0.015, "Olive oil", "OLIVE OIL"], [0.4, "Broccoli, raw", "BROCCOLI"]]

salmon_5 = [[0.68, "Salmon, Atlantic, wild, raw", "SALMON"], [0.007, "Mustard, yellow, ready made", "MUSTARD SEED"], [0.015, "Olive oil", "OLIVE OIL"], [0.45, "Potato, raw","POTATO"], [0.4, "Broccoli, raw", "BROCCOLI"]]



## return the name of recipe and clean recipe components in the form of [weight in kilogram, ingredient name for cf, ingredient name for wf]
def get_clean_ingredients_components(key):
    keys = ["salmon", "chicken", "beef"]
    assert key in keys
    name, ingredients = get_recipe_ingredients(key)
    
    #count_unit = ["pound", "cup", "tablespoon", "teaspoon", "head", "lb", "tbsp", "cloves", "clove", "tsp", "tbsp.", "lb.", "bunch"]
    
    if key == "salmon":
        clean_recipe_components = [salmon_1, salmon_2, salmon_3, salmon_4, salmon_5]
    elif key == "chicken":
        clean_recipe_components = [chicken_2, chicken_4, chicken_5]
    elif key == "beef":
        clean_recipe_components = [beef_1, beef_2, beef_3, beef_5]
    else:
        raise NotImplementedError
                
    
    return name, clean_recipe_components

def get_recipe_metric():

    return None


def get_recipe_waterfootprint(ingredient_input, weight_input, database, keyname):
    
    (db_wf, db_cf) = database
    (key_wf, key_cf) = keyname
    
    # calculate food metric for given food_input
    assert len(ingredient_input) == len(weight_input)
    ingredient_footprint = np.zeros(len(ingredient_input)) # water footprint for each ingredient
    
    for count, (ingredient, weight) in enumerate(zip(ingredient_input, weight_input)):
        assert ingredient in db_wf.keys()
        ingredient_footprint[count] = weight * db_wf[ingredient][key_wf]/1000
    
    return ingredient_footprint.sum(), ingredient_footprint


def initialize_datebase_footprint():
    '''
    Initialize the database
    '''
    file_name_wf = "SuEatableLife_Food_Fooprint_database_wf.csv"
    file_name_cf = "SuEatableLife_Food_Fooprint_database_cf.csv"
    key_wf = 'Water Footprint liters water/kg o liter of food ITEM'
    key_cf = 'Carbon Footprint kg CO2eq/kg or l of food ITEM'
    db_wf = pd.read_csv(file_name_wf)
    db_cf = pd.read_csv(file_name_cf)
    
    db_wf = db_wf[['Food commodity ITEM', key_wf]]
    db_cf = db_cf[['Food commodity ITEM', key_cf]]
    db_wf = db_wf.set_index('Food commodity ITEM').T.to_dict()
    db_cf = db_cf.set_index('Food commodity ITEM').T.to_dict()
    
    return db_wf, db_cf, key_wf, key_cf


def ingredient_name_mapping(ingredient_input, fp_type):
    ingredient_map = return_mapping(fp_type)
    ingredient_output = [ingredient_map[ingred] for ingred in ingredient_input]
    return ingredient_output


if __name__ == "__main__":
    
    ingredient_input_test = ['seabass', 'tomato', 'coconut', 'apple juice'] # ingredients
    weight_input_test = [200, 100, 250, 80] # ingredients' weights in grams
    
    
    db_wf, db_cf, key_wf, key_cf = initialize_datebase_footprint()
    ingredient_input_mapped = ingredient_name_mapping(ingredient_input_test, 'water') # modified ingredients with mapping
    
    
    footprint = get_recipe_waterfootprint(ingredient_input_mapped, weight_input_test, (db_wf, db_cf), (key_wf, key_cf))
    print(footprint)