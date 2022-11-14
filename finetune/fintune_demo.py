import json

ds = []


ds.append(
    {
        'prompt': 'Name five low-carbon-footprint recipes that use A and B',
        'completion': '''
        1. Recipe A
        2. Recipe B
        3. Recipe C
        4. Recipe D
        5. Recipe E
        '''
    }
)


if __name__ == '__main__':
    with open("train_data.json", 'w') as f:
        for item in ds:
            f.write(json.dumps(item) + "\n")