# ------------------------------------------------------------------------
# EcoFood
# Copyright (c) 2022 OpenAI-Hackathon Team 34. All Rights Reserved.
# Licensed under the MIT-style license found in the LICENSE file in the root directory
# ------------------------------------------------------------------------


import numpy as np

def get_recipe_metric(food_input, weight_input, **kwargs):
    
    # generate & process the source food metric
    food_source = ["apple", "orange", "banana"]
    metric = {}
    for food in food_source:
        metric_food = np.ndarray(shape=(5), dtype=float, order='F')
        metric[food] = metric_food

    # calculate food metric for given food_input
    assert len(food_input) == len(weight_input)
    metric_output = np.zeros_like(metric_food)
    for food, weight in zip(food_input, weight_input):
        assert food in food_source
        metric_output = metric_output + weight * metric[food]
    
    print(metric)
    print(metric_output)

    return metric_output
