from random import random
from math import floor

def random_reorder(l):
    # just iterate throught the list,
    # swap each item with another one in a random index and...
    # reach the end of the list, done.

    if len(l) < 2: # if length is 1 or 0, do nothing.
        return

    for i in range(0, len(l)):
        if random() > 0.1: # sometimes you skip an item to add more randomness (1/10 chance of skipping)
            random_index = floor(random() * len(l) )
            temp = l[i]
            l[i] = l[random_index]
            l[random_index] = temp
    

x = [1,2,3,4,5,6,7,8]

random_reorder(x)
print(x)