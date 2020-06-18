'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # goal is to see how many different ways the cookies can be eaten
    # I can recursively see if all the numbers in it can go into it with an int remainder
 
    #if it is one, he can only eat one, so that is an edge case to take care of
    global count

    count = 0

    if n == 0:
        print('hit zero')
        return count
    
    # if n < 0:
    #     return count

    # if n == 1:
    #     count += 1
    #     return count
    
    # if n == 2:
    #     count += 2

    #divide n by one number less than that
    if n > 0:

        division = n - eating_cookies(n - 1)
        print('is it here')
        print('remainder:', division)
        print('count:', count)
        print('n:', n)
        print('n-1:', n-1)
        print()
        if type(division) == int:
            count += 1
    count += 1

    return count

    # if it divides easily, or divides with a whole number, that counts
    #  how to count?
    #  

    # if it is a float, that doesnt count 

    # _new plan_
    # 


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")





print(type(5))
print(type(5.5))
