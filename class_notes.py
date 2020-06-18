def divides_self(nums):
    numbers = str(nums)
    the_return = False
    if nums == 0:
        return False
    if len(numbers) == 1:
        the_return = True
    for i in numbers:
        i = int(i)
        if i == 0:
            return False
        if nums % i == 0:
            the_return = True
    return the_return
        
print(divides_self(0))
print()
print(divides_self(1))
print()
print(divides_self(10))


#   #lesson knapsack problem

# from itertools import combinations

# def naive_fill_knapsack(sack, items):
#     items.sort(key=lambda x: x.value, reverse=True)
#     #what is wrong with this?
#     #some items have more value than others, not necessarily the heaviest thing
#     #or a combination of smaller items 
#     sack = []
#     weight = 0
#     for i in items:
#         weight += i.weight
#         if weight > 50:
#         return sack
#         else:
#         sack.append(i)

# return sack

# def brute_force_fill_knapsack(sack, items):
#   combos = []
#   sack = []
#   for i in range(1, len(items)+1):
#     list_of_combos = list(combinations(items, i))
#     for i in list_of_combos:
#       combos.append(list(combos))

#   best_value = -1
#   for c in combos:
#     value = 0
#     weight = 0 

#     for item in c:


# def greedy_fill_knapsack(sack, items):

#   for i in items:
#     i.efficiency = i.value/i.weight

#   items.sort(key=lambda x: x.efficiency, reverse=True)

#   sack = []
#   weight = 0

#   for i in items:
#     weight += i.weight
#     if weight > 50:
#       return sack
#     else:
#       sack.append(i)

#tallest building problem 

def tallest_building_height(buildings):
    #get the length of the entire list passed
    poss_height = len(buildings)
    #count how many items in the list you go through before encountering #
    count = 0
    found = False
    while not found:
        for i in buildings:
            if i.find('#') == -1:
                count += 1
            else:
                found = True
 
    #subtract empty items from total items
    #multiply by 20 and return
    tallest_height = f'{(poss_height - count) * 20}m'

    return tallest_height


print(tallest_building_height([
	"         ",
	" ##      ",
	" ##      ",
	"###   ## ",
	"###   ## ",
	"###   ###",
	"###   ###"]))

print(tallest_building_height([
	"            ##",
	"            ##",
	"            ##",
	"###   ###   ##",
	"###   ###   ###",
	"###   ###   ###",
	"###   ###   ###"
]))

#its working