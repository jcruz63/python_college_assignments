locations = {'Florida': ['Jacksonville', 'Orlando', 'Tampa'], 'Georgia': ['Atlanta', 'Macon', 'Warner Robins'],
             'Texas': ['Houston', 'Dallas', 'Austin']}


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for local in val:
            if local not in inverse:
                inverse[local] = [key]
            else:
                inverse[local].append(key)
    return inverse


def print_cities_in_state(state):
    print(f'The cities in {state} are {locations[state]}')


def print_what_state(city):
    print(f'{city} is in the state of {invert_dict(locations)[city]}')


if __name__ == '__main__':
    print(invert_dict(locations))
    print("\n")
    print_cities_in_state('Florida')
    print("\n")
    print_what_state('Jacksonville')
