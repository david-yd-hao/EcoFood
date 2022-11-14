import json

ds = []

for i in range(500):
    ds.append(
        {
            'prompt': 'Name five low-carbon-footprint recipes that use chicken and basil',
            'completion': '''
            1. Chicken and Pesto Penne
            2. Thai Basil Chicken
            3. Chicken Stuffed with Basil and Mozzarella Cheese
            4. Lemon Basil Chicken
            5. Garlic Tomato Basil Chicken
            '''
        }
    )

    ds.append(
        {
            'prompt': 'Name five low-carbon-footprint recipes that use salmon, mustard and broccoli',
            'completion': '''
            1. Salmon and Broccoli Traybake with Mustard Sauce
            2. Maple Mustard salmon with Roasted Broccoli
            3. Salmon with Steamed Beans and Broccoli with mustard sauce
            4. Baked Mustard-glazed Salmon with Tenderstem
            5. Mustard Salmon With Crushed Potatoes And Tenderstem Broccoli
            '''
        }
    )

    ds.append(
        {
            'prompt': 'Name five low-carbon-footprint recipes that use beef',
            'completion': '''
            1. Thai Beef Salad
            2. Beef Hamburger
            3. Beef Curry with sweet pepper
            4. Beef Stew with onions and mushrooms
            5. Beef Steak
            '''
        }
    )

if __name__ == '__main__':
    with open("train_data.json", 'w') as f:
        for item in ds:
            f.write(json.dumps(item) + "\n")