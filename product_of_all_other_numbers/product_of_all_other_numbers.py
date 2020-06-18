'''
Input: a List of integers
Returns: a List of integers
'''
import numpy as np
import time


def product_of_all_other_numbers(arr):
    # I believe this already reaches the goal of O(n) for space and time complexity
    # O(2n) ---> O(n)
    answer = [] #O(n) space
    for i in arr: #O(n) time
        arr2 = arr[:] #O(n) space/time
        arr2.remove(i)
        result = np.prod(np.array(arr2))
        answer.append(result)
    return answer
    #first run, product of all numbers
    # second, change product of number/the number, therefore giving the answer

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]

    start = time.time()
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
    end = time.time()
    print(f'Original function takes {end - start} seconds to run.')
