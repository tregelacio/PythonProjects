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

first_names = ["Liam", "Noah", "William", "James", "Logan", "Benjamin", "Mason", "Elijah", "Oliver"]
last_names = ["Johnson", "Carson", "Higa", "Lengyel", "Walter", "Thompson", "Curry"]
names = random_name_generator(first_names, last_names, 3)
print('\n'.join(names))
