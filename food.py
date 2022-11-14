# ------------------------------------------------------------------------
# EcoFood
# Copyright (c) 2022 OpenAI-Hackathon Team 34. All Rights Reserved.
# Licensed under the MIT-style license found in the LICENSE file in the root directory
# ------------------------------------------------------------------------


import numpy as np
import pandas as pd

from mapping_data import return_mapping
from get_all_recipes_clean import get_clean_ingredients_components


def get_recipe_metric(ingredient_input, weight_input, database, keyname):

    db_final = database
    
    assert len(ingredient_input) == len(weight_input)
    ingredient_metric = np.zeros((len(ingredient_input), len(keyname)))
    for count, (ingredient, weight) in enumerate(zip(ingredient_input, weight_input)):
        assert ingredient in db_final.keys()
        for i in range(len(keyname)):
            if i == 0:
                ingredient_metric[count, i] = weight * float(db_final[ingredient][keyname[i]]) * 10
            if i != 0:
                ingredient_metric[count, i] = weight * float(db_final[ingredient][keyname[i]])

    
    return ingredient_metric.sum(0), ingredient_metric


def get_recipe_waterfootprint(ingredient_input, weight_input, database, keyname):
    
    (db_wf, db_cf) = database
    (key_wf, key_cf) = keyname
    
    # calculate food metric for given food_input
    assert len(ingredient_input) == len(weight_input)
    ingredient_footprint = np.zeros(len(ingredient_input)) # water footprint for each ingredient
    
    for count, (ingredient, weight) in enumerate(zip(ingredient_input, weight_input)):
        assert ingredient in db_wf.keys()
        ingredient_footprint[count] = weight * db_wf[ingredient][key_wf] * 10
    
    return ingredient_footprint.sum(), ingredient_footprint


def initialize_datebase_footprint():
    '''
    Initialize the database
    '''
    file_name_wf = "SuEatableLife_Food_Fooprint_database_wf.csv"
    file_name_cf = "SuEatableLife_Food_Fooprint_database_cf.csv"
    file_name_final = "Results_FINAL_20210201v4.csv"
    key_wf = 'Water Footprint liters water/kg o liter of food ITEM'
    key_cf = 'Carbon Footprint kg CO2eq/kg or l of food ITEM'
    key_final = ['Total kg CO2-eq/kg','Energi (KJ/100 g)','Fedt (g/100 g)','Kulhydrat (g/100 g)','Protein (g/100 g)']
    db_wf = pd.read_csv(file_name_wf)
    db_cf = pd.read_csv(file_name_cf)
    db_final = pd.read_csv(file_name_final)
    
    db_wf = db_wf[['Food commodity ITEM', key_wf]]
    db_cf = db_cf[['Food commodity ITEM', key_cf]]
    db_final = db_final[['Name','DSK Category', 'Total kg CO2-eq/kg','Energi (KJ/100 g)','Fedt (g/100 g)','Kulhydrat (g/100 g)','Protein (g/100 g)']]
    db_final = db_final[['Name', 'Total kg CO2-eq/kg','Energi (KJ/100 g)','Fedt (g/100 g)','Kulhydrat (g/100 g)','Protein (g/100 g)']]
    db_final = db_final.set_index('Name').T.to_dict()
    db_wf = db_wf.set_index('Food commodity ITEM').T.to_dict()
    db_cf = db_cf.set_index('Food commodity ITEM').T.to_dict()
    
    return (db_wf, db_cf, db_final), (key_wf, key_cf, key_final)


def ingredient_name_mapping(ingredient_input, fp_type):
    ingredient_map = return_mapping(fp_type)
    ingredient_output = [ingredient_map[ingred] for ingred in ingredient_input]
    return ingredient_output

def ingred2ingred(ingred_list):
    all_weight = []
    all_ingred_carbon = []
    all_ingred_water = []
    for num_recipe in range(len(ingred_list)):
        weight = []
        ingred_carbon = []
        ingred_water = []
        for num_ingred in range(len(ingred_list[num_recipe])):
            w = ingred_list[num_recipe][num_ingred][0]
            carbon_name = ingred_list[num_recipe][num_ingred][1]
            water_name = ingred_list[num_recipe][num_ingred][2]
            weight.append(w)
            ingred_carbon.append(carbon_name)
            ingred_water.append(water_name)
        all_weight.append(weight)
        all_ingred_carbon.append(ingred_carbon)
        all_ingred_water.append(ingred_water)
    
    assert len(all_weight) == len(all_ingred_carbon) == len(all_ingred_water)
    
    return all_weight, all_ingred_carbon, all_ingred_water


if __name__ == "__main__":
    
    name, clean_recipe_components = get_clean_ingredients_components("beef")
    all_weight, all_ingred_carbon, all_ingred_water = ingred2ingred(clean_recipe_components)
    (db_wf, db_cf, db_final), (key_wf, key_cf, key_final) = initialize_datebase_footprint()
    
    for i in range(len(name)):
        print(name[i])
        # print(all_weight[i], all_ingred_carbon[i], all_ingred_water[i])
        footprint,_ = get_recipe_waterfootprint(all_ingred_water[i], all_weight[i], (db_wf, db_cf), (key_wf, key_cf))
        print(footprint)

        metric,_ = get_recipe_metric(all_ingred_carbon[i], all_weight[i], db_final, key_final)
        print(metric)