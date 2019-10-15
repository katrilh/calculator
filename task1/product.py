import numpy as np

# Assuming the input is a list and can contain several negative values
def calculate_product(lst):
    lst.sort()
    # np.product(lst[-3:]) finds the product of the highest elements
    # lst[0]*lst[1]*lst[-1] checks the two lowest entries and the highest one
    return max(np.product(lst[-3:]), lst[0]*lst[1]*lst[-1])
