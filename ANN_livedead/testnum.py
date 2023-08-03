import random

# Sample dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Get the keys of the dictionary as a list
keys_list = list(my_dict.keys())

# Shuffle the keys list in place
random.shuffle(keys_list)

# Access the elements of the dictionary in the shuffled order
for key in keys_list:
    print(key, my_dict[key])