import time

'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

def single_number(arr):
    #get a set of the list
    once = list(set(arr))
    #empty container to hold counts of each number
    counts = []
    for i in once:
        counts.append([i, arr.count(i)])
    
    #get the number with a single count and return it
    for i in counts:
        if i[1] == 1:
            return i[0] 


def single_number3(arr):
    # This is still not O(1) space complexity 
    # but it is the fastest 
    #first going to test the same solution as above but with a dictionary 
    #get a set of the list
    once = list(set(arr))
    #empty container to hold counts of each number
    counts = {}
    for i in once:
        counts[arr.count(i)] = i
    
    #query dictionary for key with value of one 
    return counts.get(1)

def single_number4(arr):
    return 2 * sum(set(arr)) - sum(arr)

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    start_time = time.time()
    print(f"The odd-number-out is {single_number(arr)}")
    end_time = time.time()

    print(f'First function took {end_time-start_time} seconds')

    start_time = time.time()
    print(f"The odd-number-out is {single_number3(arr)}")
    end_time = time.time()

    print(f'Third function took {end_time-start_time} seconds.')
    print('Third is fastest')

    start_time = time.time()
    print(f"The odd-number-out is {single_number4(arr)}")
    end_time = time.time()

    print(f'Fourth function took {end_time-start_time} seconds.')
    print('Fourth is O(1)')



def single_number2(arr):
    #first pass solution issues:
    #  - takes up extra space

    counts = {}

    #loop through input list O(n)
    for num in arr:
        #if item in counts
        if num in counts:
            #remove item
            del counts[num]
        #otherwise
        else:
            #add item
            counts[num] = 1
    
    #this will always be O(1) because there is always one value left
    for k, v in counts.items():
        if v == 1:
            return k

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    start_time = time.time()
    print(f"The odd-number-out is {single_number2(arr)}")
    end_time = time.time()

    print(f'Second function took {end_time-start_time} seconds')
