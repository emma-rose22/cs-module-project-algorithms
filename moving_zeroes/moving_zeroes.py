'''
Input: a List of integers
Returns: a List of integers
'''
import time

def moving_zeroes(arr):
    arr = arr[:]
    zeroes = 0
    #loop through the list
    while arr.count(0) > 0:
        for i in arr:
        #if there is a zero pop it out
            if i == 0:
                arr.remove(0)
                # count how many zeros are taken out
                zeroes += 1

    to_add = [0] * zeroes
    #when we are done, append them all to a list
    arr = arr + to_add

    return arr

def moving_zeroes2(arr):
    #what if we had two pointers that move towards each other?
    # if the left pointer "sees" a zero and the right sees a non zero
    # swap!
    #if the left sees a non zero, increment
    #if right sees a zero, increment

    #left pointer at beginning
    left = 0
    #right pointer at end
    right = len(arr) -1

    # loop until left and right pointers meet or right passes the left

    '''This is O(1) space complexity'''
    while left != right and right > left:
        # swap situation:
        # left sees zero, right sees non-zero
        if arr[left] == 0 and arr[right] !=0:
            # swap the items 
            arr[left], arr[right] = arr[right], arr[left]
            # increment left
            left += 1
            # decrement right
            right -= 1
        #non swap situation:
        if arr[left] != 0:
            # if left sees non-zero
            left += 1
                # increment left
        if arr[right] == 0:
            # if right sees zero:
            right -= 1
                #decrement right
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    # arr = [0, 0, 0, 0, 3, 2, 1]

    start = time.time()
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    end = time.time()
    print(f'The first function takes {end - start} seconds.')

    start = time.time()
    print(f"The resulting of moving_zeroes is: {moving_zeroes2(arr)}")
    end = time.time()
    print(f'The second function takes {end - start} seconds.')