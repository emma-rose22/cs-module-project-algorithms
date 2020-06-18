'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
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


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    # arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print('lengthz:', len(moving_zeroes(arr)))















    

    # moved = True
    # while moved:
    #     moved = False
    #     count = 0
    #     for i in range(len(arr)):
    #        ## moved = False
    #         count +=1
    #         if i == 0:
    #             print('count:', count)
    #             arr.pop(count - 1)
    #             arr.append(0)
    #             moved = True
    # return arr
