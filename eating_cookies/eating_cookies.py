'''
Input: an integer
Returns: an integer
'''
import time 
def eating_cookies(n):
    '''
    this method is inefficient because there is repeated work
    you are repeatedly making the same decision that with one cookie, you can only eat one cookie
    every time we get to the end of a stack

    what if we could save the answer for each subtree? getting from 1 to 0 can be saved
    a _cache_ if you will

    a dictionary could be used as our cache
    '''
    # goal is to see how many different ways the cookies can be eaten
    # I can recursively see if all the numbers in it can go into it with an int remainder

    #how many paths can we take from the cookies we start with, to get to zero cookies?

    if n == 0:
        #this means that we ended up with exactly zero cookies
        #which means we found a valid way to eat them
        return 1

    if n < 0:
        #cant have negative numbers of cookies
        return 0


    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

def eating_cookies2(n, cache=None):
    # goal is to see how many different ways the cookies can be eaten
    # I can recursively see if all the numbers in it can go into it with an int remainder

    #how many paths can we take from the cookies we start with, to get to zero cookies?

    if n == 0:
        #this means that we ended up with exactly zero cookies
        #which means we found a valid way to eat them
        return 1

    if n < 0:
        #cant have negative numbers of cookies
        return 0

    #check if cache exists
    if cache and n in cache:
    #see if n exists in the cache
        return cache[n]

    if cache is None:
    #create the cache
        cache = {}

    cache[n] = eating_cookies2(n-1, cache) + eating_cookies2(n-2, cache) + eating_cookies2(n-3, cache)

    #we need to return our cache values, they have the answers
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    start = time.time()
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    end = time.time()
    print(f'The first function takes {end-start} seconds to run. ')
    print()

    start = time.time()
    print(f"There are {eating_cookies2(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    end = time.time()
    print(f'The second function takes {end-start} seconds to run. ')
