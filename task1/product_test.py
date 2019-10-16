from random import randint, sample

import product


def brute_force(lst):
    solution = float('-inf')
    n = len(lst)
    
    if n < 3:
        print("List too short, must contain at least 3 elements")
        raise ValueError
    
    # Checks all possible products of three elements in a list, keeps the highest one
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                temp = lst[i] * lst[j] * lst[k]
                if temp > solution:
                    solution = temp
    return solution


def make_testset():
    testset = []
    n = randint(3, 10)  # How many tests will be generated. For a proper test this number would be higher
    
    for i in range(n):
        # generates a list with random numers from -1000 to 1000, length between 3 and 50
        lst = sample(range(-1000, 1001), randint(3, 50))
        
        # Adds a tuple of the newly generated list and its brute force solution to the testset
        testset.append((lst, brute_force(lst)))
    
    return testset


def one_test(lst, solution):
    print("Testing", lst)
    # Comparing to my own method of finding the highest product
    x = product.calculate_product(lst)
    return (x == solution), x


def run():
    tests = make_testset()
    validity = False
    for lst, solution in tests:
        validity, x = one_test(lst, solution)
        if not validity:
            print(f"Incorrect solution, failed with {lst}\nFound {x} but should have been {solution}")
            break
    
    if validity:
        print("All tests passed")


if __name__ == "__main__":
    run()
