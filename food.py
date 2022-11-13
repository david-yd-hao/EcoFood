# ------------------------------------------------------------------------
# EcoFood
# Copyright (c) 2022 OpenAI-Hackathon Team 34. All Rights Reserved.
# Licensed under the MIT-style license found in the LICENSE file in the root directory
# ------------------------------------------------------------------------


import numpy as np
import pandas as pd

from mapping_data import return_mapping


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