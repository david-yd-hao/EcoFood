import os
import openai
import re

key = "Your own key"


def text_generate(ingredients, api_key):

    openai.api_key = api_key
    ingredients_str = ', '.join(ingredients)
    prompt = 'Create three different food recipes while making use of ' + ingredients_str + '.' \
             + 'Display weight of each ingredient used.' \
             + 'Follow the format of \n Name: \n Ingredients: \n Instructions: \n'
    prompt = 'Name five low-carbon-footprint recipes that use beef'

    # get response from GPT-3
    response = openai.Completion.create(
        model="davinci:ft-university-of-cambridge-2022-11-14-00-29-20",
        prompt=prompt,
        temperature=0.0,
        max_tokens=128,
        top_p=1,
        best_of=3,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    response_text = response['choices'][0]['text']
    print(response_text)
    recipe_text = response_text.split('\n\n')
    # parse the text into three separate lists
    response_list = re.split('Name:|Ingredients:|Instructions:', response_text)[1:]
    name_list = response_list[::3]
    ingredient_list = response_list[1::3]
    instruction_list = response_list[2::3]

    # ingredient detail will be of the format:
    # [first recipe:[ingredients needed in this dish:[amount, name]], second, third]

    ingredient_detail = []
    for item in ingredient_list:
        item_list = []
        ingredients = re.split('\n', item)[:-1]
        for ingre in ingredients:
            if not re.search('-', ingre):
                ingredients.remove(ingre)
        for ingredient in ingredients:
            splitted = ingredient.split()
            item_list.append([splitted[0] + ' ' + splitted[1], ' '.join(splitted[2:])])
        ingredient_detail.append(item_list)

    print(recipe_text)
    return name_list, ingredient_detail, instruction_list, recipe_text


def image_generate(recipe, api_key):
    openai.api_key = api_key
    prompt = 'Display image of food on a dish. The recipe is given as follows:' + recipe

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )

    image_url = response['data'][0]['url']

    return image_url


if __name__ == '__main__':
    key='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'
    key='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'
    name, ingredient, instruction, recipe = text_generate(['salmon', 'lettuce'], api_key=key)
    print(image_generate(recipe[0], api_key=key))




