with open("day8/day8_input.txt") as file:
    image_dimention = 25 * 6
    image = file.read()
    image_layers = [
        image[i:i + image_dimention]
        for i in range(0, len(image), image_dimention)
    ]


def find_zeros_number(layer=""):
    zeros = 0
    for char in layer:
        if char == "0":
            zeros += 1
    return zeros


def find_min_zeros_index(image_layers=[]):
    index = 0
    min_zeros = float("inf")
    min_zeros_index = 0
    for layer in image_layers:
        temp_zeros = find_zeros_number(layer)
        if temp_zeros < min_zeros:
            min_zeros = temp_zeros
            min_zeros_index = index
        index += 1
    return min_zeros_index


def mult_ones_and_twos(layer=""):
    ones = 0
    twos = 0
    for i in layer:
        ones = ones + 1 if i == "1" else ones
        twos = twos + 1 if i == "2" else twos
    return ones * twos


index = find_min_zeros_index(image_layers)
print(" result = ", mult_ones_and_twos(image_layers[index]))