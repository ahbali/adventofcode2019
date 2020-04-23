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


def find_multiplier(chemical_dict: dict, quantity_needed: int) -> int:
    """now using math.ceil() function instead of this"""
    effective_quantity = quantity_needed
    batch_size = chemical_dict["quantity"]
    temp_division = effective_quantity // batch_size
    temp_reminder = effective_quantity % batch_size
    multiplier = temp_division if temp_reminder == 0 else temp_division + 1
    return multiplier


def coefficient_from_leftovers(chemical_dict: dict, leftovers: dict) -> int:
    """unused"""
    coefficient = float("inf")
    for chemical, quantity in chemical_dict.items():
        if chemical != "quantity":
            left_quantity = leftovers.get(chemical, 0)
            if quantity > left_quantity:
                return 0
            else:
                possible = left_quantity // quantity
                coefficient = possible if possible < coefficient else coefficient
    # quantity_of_chemical = int(coefficient) * chemical_dict["quantity"]
    return int(coefficient)


ingredients_deque: "deque" = deque()
node = ("FUEL", 1)
ingredients_deque.append(node)
ore_counter = 0
single_ingredient_nodes: Dict[str, int] = dict()
leftovers: Dict[str, int] = dict()

while ingredients_deque:
    chemical, wanted_quantity = ingredients_deque.pop()
    if chemical == "ORE":
        ore_counter += wanted_quantity
    else:
        chemical_dict = reactions[chemical]
        provided_quantity = chemical_dict["quantity"]
        effective_quantity = wanted_quantity - leftovers.get(chemical, 0)
        # / after commenting this part of my code i started getting the correct answer
        # * for the third example and i don't know why :/
        # * /
        # if effective_quantity <= 0:
        #     leftovers[chemical] -= wanted_quantity
        # else:
        # multiplier = find_multiplier(chemical_dict, effective_quantity)
        multiplier = ceil(effective_quantity / chemical_dict["quantity"])
        leftover_quantity = multiplier * provided_quantity - effective_quantity
        leftovers[chemical] = leftover_quantity
        # need to find a way to deal with ORE here;
        # effective_quantity -= (
        #     coefficient_from_leftovers(chemical_dict, leftovers)
        #     * chemical_dict["quantity"]
        # )
        # if effective_quantity <= 0:
        #     pass
        for ingredient, coefficient in chemical_dict.items():
            if ingredient != "quantity":
                queued_ingredient = (ingredient, coefficient * multiplier)
                ingredients_deque.append(queued_ingredient)


print("ORE counter = ", ore_counter)
# pprint(leftovers)
