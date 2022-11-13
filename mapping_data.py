def return_mapping(type):
    '''
    return mapping from a certrain type
    type: str ('water' or 'carbon')
    '''
    # initialize mapping
    if type == 'water':
        ingredient_map = {'seabass': 'SEABASS', 
                            'tomato': 'TOMATO', 
                            'coconut': 'COCONUTS', 
                            'apple juice': 'APPLE JUICE'}
    elif type == 'carbon':
        ingredient_map = {'seabass': 'SEABASS', 
                            'tomato': 'TOMATO', 
                            'coconut': 'COCONUTS', 
                            'apple juice': 'APPLE JUICE'}
    else:
        raise NotImplementedError('Invalid Mapping Type')
    
    return ingredient_map