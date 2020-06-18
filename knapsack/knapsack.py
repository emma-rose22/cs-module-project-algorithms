#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here

    pass


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')


  #lesson knapsack problem

  from itertools import combinations

  def naive_fill_knapsack(sack, items):
    items.sort(key=lambda x: x.value, reverse=True)
    #what is wrong with this?
    #some items have more value than others, not necessarily the heaviest thing
    #or a combination of smaller items 
    sack = []
    weight = 0
    for i in items:
      weight += i.weight
      if weight > 50:
        return sack
      else:
        sack.append(i)

    return sack

def brute_force_fill_knapsack(sack, items):
  combos = []
  sack = []
  for i in range(1, len(items)+1):
    list_of_combos = list(combinations(items, i))
    for i in list_of_combos:
      combos.append(list(combos))

  best_value = -1
  for c in combos:
    value = 0
    weight = 0 

    for item in c:


def greedy_fill_knapsack(sack, items):

  for i in items:
    i.efficiency = i.value/i.weight

  items.sort(key=lambda x: x.efficiency, reverse=True)

  sack = []
  weight = 0

  for i in items:
    weight += i.weight
    if weight > 50:
      return sack
    else:
      sack.append(i)
