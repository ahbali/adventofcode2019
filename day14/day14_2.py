# cSpell:ignore deque
from collections import deque
from typing import Dict
from math import ceil

# from pprint import pprint


reactions: Dict[str, Dict[str, int]] = dict()
with open("day14/input.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        right, left = line.split("=>")
        _quantity, output_chemical = left.split()
        # temp = [(i, j) for i, j in [k.split() for k in right.split(",")]]
        temp = dict((j, int(i)) for i, j in [k.split() for k in right.split(",")])
        temp["quantity"] = int(_quantity)
        reactions[output_chemical] = temp
# pprint(reactions)


def ore_calculator(fuel_amount: int) -> int:
    ingredients_deque: "deque" = deque()
    node = ("FUEL", fuel_amount)
    ingredients_deque.append(node)
    ore_counter = 0
    leftovers: Dict[str, int] = dict()

    while ingredients_deque:
        chemical, wanted_quantity = ingredients_deque.pop()
        if chemical == "ORE":
            ore_counter += wanted_quantity
        else:
            chemical_dict = reactions[chemical]
            provided_quantity = chemical_dict["quantity"]
            effective_quantity = wanted_quantity - leftovers.get(chemical, 0)

            multiplier = ceil(effective_quantity / chemical_dict["quantity"])
            leftover_quantity = multiplier * provided_quantity - effective_quantity
            leftovers[chemical] = leftover_quantity

            for ingredient, coefficient in chemical_dict.items():
                if ingredient != "quantity":
                    queued_ingredient = (ingredient, coefficient * multiplier)
                    ingredients_deque.append(queued_ingredient)
    return ore_counter


goal = 1000000000000
step = 1000000
fuel_amount = 0
ore_needed = 0

while ore_needed <= goal:
    fuel_amount += step
    ore_needed = ore_calculator(fuel_amount)

maximum = fuel_amount
minimum = fuel_amount - step

while maximum - minimum > 1:
    median = (maximum + minimum) // 2
    if ore_calculator(median) < goal:
        minimum = median
    else:
        maximum = median

print("max fuel = ", median)
