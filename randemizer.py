import random

# Generate a random integer between a specified range
random_number = random.randint(1, 10)
print(random_number)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print(random_float)

# Generate a random floating-point number within a specified range
random_float_range = random.uniform(1.0, 5.0)
print(random_float_range)

# Generate a random element from a sequence
my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print(random_element)

# Shuffle the elements of a sequence randomly
random.shuffle(my_list)
print(my_list)