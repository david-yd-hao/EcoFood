# ------------------------------------------------------------------------
# EcoFood
# Copyright (c) 2022 OpenAI-Hackathon Team 34. All Rights Reserved.
# Licensed under the MIT-style license found in the LICENSE file in the root directory
# ------------------------------------------------------------------------


name_salmon = [' Salmon and Broccoli Traybake with Mustard Sauce', 
        ' Maple Mustard salmon with Roasted Broccoli', 
        ' Salmon with Steamed Beans and Broccoli with mustard sauce', 
        ' Baked Mustard-glazed Salmon with Tenderstem', 
        ' Mustard Salmon With Crushed Potatoes And Tenderstem Broccoli']
name_chicken = [' Chicken and Pesto Penne', 
        ' Thai Basil Chicken', 
        ' Chicken Stuffed with Basil and Mozzarella Cheese', 
        ' Lemon Basil Chicken', 
        ' Garlic Tomato Basil Chicken']
name_beef = [' Thai Beef Salad', 
            ' Beef Hamburger', 
            ' Beef Curry with sweet pepper', 
            ' Beef Stew with onions and mushrooms', 
            ' Beef Steak']

name_chicken_reduced = [' Thai Basil Chicken', 
                        ' Lemon Basil Chicken', 
                        ' Garlic Tomato Basil Chicken']

name_beef_reduced = [' Thai Beef Salad', 
                    ' Beef Hamburger', 
                    ' Beef Curry with sweet pepper', 
                    ' Beef Steak']

beef_1 = [['1', 'pound', 'flank steak'], ['1/4', 'cup', 'fresh lime juice'], ['1/4', 'cup', 'fish sauce'], ['1', 'tablespoon', 'brown sugar'], ['1', 'tablespoon', 'vegetable oil'], ['1', 'teaspoon', 'grated ginger'], ['1', 'garlic clove, minced'], ['1/4', 'teaspoon', 'ground black pepper'], ['1/2', 'head', 'lettuce, shredded'], ['1/2', 'cucumber, sliced'], ['1/4', 'cup', 'fresh cilantro leaves'], ['1/4', 'cup', 'chopped peanuts']]

beef_2 = [['1', 'pound', 'ground beef'], ['1/4', 'cup', 'onion, diced'], ['1', 'tablespoon', 'Worcestershire sauce'], ['1/4', 'teaspoon', 'salt']]

beef_3 = [['1', 'pound', 'beef, cut into cubes'], ['1', 'onion, chopped'], ['1', 'green pepper, chopped'], ['1', 'tablespoon', 'curry powder'], ['1', 'can (14.5 ounces) diced tomatoes, undrained'], ['1', 'can (15 ounces) chickpeas, rinsed and drained'], ['1/2', 'cup', 'raisins'], ['1/2', 'cup', 'plain yogurt'], ['1/4', 'cup', 'chopped fresh cilantro']]

beef_5 = [['1', 'pound', 'beef steak'], ['1', 'tablespoon', 'olive oil'], ['1', 'teaspoon', 'salt'], ['1/2', 'teaspoon', 'black pepper']]

chicken_2 = [['1', 'lb', 'chicken breast, thinly sliced'], ['1/2', 'cup', 'oyster sauce'], ['1/4', 'cup', 'soy sauce'], ['1/4', 'cup', 'brown sugar'], ['1', 'tbsp', 'fish sauce'], ['1', 'tbsp', 'vegetable oil'], ['4', 'cloves', 'garlic, minced'], ['1/2', 'tsp', 'crushed red pepper flakes'], ['1/4', 'cup', 'chopped Thai basil']]

chicken_4 = [['1', 'lb', 'chicken breast, cut into small strips'], ['1/4', 'cup', 'all-purpose flour'], ['2', 'tablespoons olive oil'], ['1/2', 'cup', 'chicken broth'], ['1/4', 'cup', 'lemon juice'], ['1', 'teaspoon', 'dried basil'], ['1/4', 'teaspoon', 'salt'], ['1/4', 'teaspoon', 'black pepper']]

chicken_5 = [['1', 'chicken breast'], ['1/2', 'a tomato'], ['1/4', 'teaspoon', 'garlic powder'], ['1/4', 'teaspoon', 'basil']]

salmon_1 = [['4', 'salmon fillets'], ['1', 'head', 'of broccoli, cut into florets'], ['1', 'tbsp. dijon mustard'], ['1', 'tbsp. honey'], ['1', 'tbsp. olive oil'], ['salt', 'and pepper']]

salmon_2 = [['1', 'lb', 'salmon'], ['1/4', 'cup', 'Dijon mustard'], ['1/4', 'cup', 'maple syrup'], ['1/2', 'tsp', 'smoked paprika'], ['1/4', 'tsp', 'salt'], ['1/4', 'tsp', 'black pepper'], ['1', 'head', 'broccoli, cut into florets'], ['1', 'tbsp', 'olive oil'], ['1/4', 'tsp', 'salt'], ['1/4', 'tsp', 'black pepper']]

salmon_3 = [['1', 'lb.', 'salmon'], ['1', 'cup', 'green beans'], ['1', 'cup', 'broccoli'], ['1/4', 'cup', 'Dijon mustard'], ['1/4', 'cup', 'white wine'], ['1/4', 'cup', 'olive oil'], ['salt', 'and pepper']]

salmon_4 = [['4', 'salmon fillets'], ['2', 'tablespoon', 'Dijon mustard'], ['1', 'tablespoon', 'honey'], ['1', 'tablespoon', 'olive oil'], ['1', 'bunch', 'of Tenderstem broccoli'], ['Salt', 'and pepper']]

salmon_5 = [['4', 'salmon fillets'], ['1/2', 'tablespoon', 'Dijon mustard'], ['1', 'tablespoon', 'honey'], ['1', 'tablespoon', 'olive oil'], ['Salt', 'and pepper'], ['1', 'pound', 'small Yukon Gold potatoes, halved'], ['1', 'bunch', 'tenderstem broccoli']]

def get_recipe_ingredients(key):
    keys = ["salmon", "chicken", "beef"]
    assert key in keys
    if key == "salmon":
        ingredients = [salmon_1, salmon_2, salmon_3, salmon_4, salmon_5]
        return name_salmon, ingredients
    elif key == "chicken":
        ingredients = [chicken_2, chicken_4, chicken_5]
        return name_chicken_reduced, ingredients
    elif key == "beef":
        ingredients = [beef_1, beef_2, beef_3, beef_5]
        return name_beef_reduced, ingredients
    else:
        raise NotImplementedError


if __name__ == '__main__':
    name, ingredients = get_recipe_ingredients('beef')
    print(name, len(name))
    print(ingredients, len(ingredients))