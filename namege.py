from random import choice

def random_name_generator(first, second, x):
    """
        Generates random names.
        Arguments:
         - list of first names
         - list of last names
         - number of random names
    """
    names = []
    for i in range(x):
        names.append("{0} {1}".format(choice(first), choice(second)))
    return set(names)

first_names = ["Tre", "Makayla", "Kaylie", "Frances", "Janiele", "Emma", "Starshine"]
last_names = ["Gelacio", "Holbrook", "Hayashida", "Corotan", "Luab", "Torgrimson", "Chun"]
names = random_name_generator(first_names, last_names, 3)
print('\n'.join(names))