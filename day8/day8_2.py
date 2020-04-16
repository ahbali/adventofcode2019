with open("day8/day8_input.txt") as file:
    image_dimention = 25 * 6
    # image_dimention = 2 * 2
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


# print(image_layers)
final_image = [i for i in image_layers[0]]
# print("initial state of final image: ", final_image)
for i in range(image_dimention):
    for layer in image_layers:
        if layer[i] != "2":
            final_image[i] = layer[i]
            break

# print("final image : ", final_image)
# final_image_lines = ["".join(final_image[i:i + 25]) for i in range(6)]
# image_string = "".join(final_image)
# temp_image = image_string.replace("2", " ")

# for line in final_image_lines:
#     print(line)

# for i in range(0, 25 * 6, 25):
#     print(temp_image[i:i + 26])

final_string = "".join(final_image)
final_string = final_string.replace("1", "#")
final_string = final_string.replace("0", " ")
for i in range(0, image_dimention, 25):
    print(final_string[i:i + 25])
# print(final_string)