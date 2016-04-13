import math
import random
import statistics as st
import numpy as np


def flip_it():
    return random.randint(1, 2)

def flippin_off(flips=5):
    results_list = []
    for n in range(flips + 1):
        heads = 0
        tails = 0
        for _ in range(2 ** n):
            if flip_it() == 1:
                heads += 1
            else:
                tails += 1
        results_list.append((heads, tails))
    return results_list

def show_stuff(runs):
    compiled_list = []
    while runs > 0:
        result = flippin_off()
        compiled_list.append(result)
        runs -= 1
    print(compiled_list)

show_stuff(20)
