def same_adjacent(str_number=""):
    # str_number = str(number)
    for i in range(5):
        if str_number[i] == str_number[i + 1]:
            return True
    return False


def is_not_decreasing(str_number=""):
    # str_number = str(number)
    for i in range(5):
        if str_number[i] > str_number[i + 1]:
            return False
    return True


def new_rule(number=""):
    # str_map = []
    double = False
    count = 1
    i = 0
    while i < 5:
        pivot = number[i]
        if number[i + 1] == pivot:
            count += 1

        else:
            # str_map.append((pivot, count))
            if count == 2:
                return True
            pivot = number[i + 1]
            count = 1
        i += 1
    # str_map.append((pivot, count))
    if count == 2:
        return True
    return False


# results = []
count = 0
for element in range(372037, 905158):
    number = str(element)
    if same_adjacent(number) and is_not_decreasing(number) and new_rule(
            number):
        count += 1
        # results.append(str(number))

print("number of passwords = ", count)

# mynum = "112233"
# test = new_rule(mynum)
# print("result for ", mynum, " is = ", test)
