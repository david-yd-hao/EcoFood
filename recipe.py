import os
import openai
import re

key = 'Your own key'


def generate(ingredients, api_key):

    openai.api_key = api_key
    ingredients_str = ', '.join(ingredients)
    prompt = 'Create three different food recipes while making use of ' + ingredients_str + '.' \
             + 'Display weight of each ingredient used.' \
             + 'Follow the format of \n Name: \n Ingredients: \n Instructions: \n'

    # get response from GPT-3
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.0,
        max_tokens=2048,
        top_p=1,
        best_of=3,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    response_text = response['choices'][0]['text']

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

    return name_list, ingredient_detail, instruction_list


if __name__ == '__main__':
    generate(['salmon', 'lettuce'], api_key=key)



