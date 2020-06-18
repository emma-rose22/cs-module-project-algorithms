'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    #keep the max numbers
    max_nums = [] # O(1) space
    #loop through all the numbers, but dont send the window
    #into space outside the array
    for i in range(len(nums)-(k-1)): #O(n) time
        #set the window to the radius of the current number
        #by the current number plus the window size
        window = nums[i:i+k]
        #get the max of the window and append it to our list
        max_nums.append(max(window))

    return max_nums



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")


    # max_nums = []
    # for i in range(len(nums)-(k-1)):
    #     window = []
    #     for z in range(k):
    #         window.append(i)
    #         print(window)
    #     print()
    #     max_nums.append(max(window))

    # return max_nums
