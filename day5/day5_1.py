# prog = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

# prog = [1, 1, 1, 4, 99, 5, 6, 0, 99]
init_prog = [
    1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 19, 5, 23,
    1, 9, 23, 27, 2, 27, 6, 31, 1, 5, 31, 35, 2, 9, 35, 39, 2, 6, 39, 43, 2,
    43, 13, 47, 2, 13, 47, 51, 1, 10, 51, 55, 1, 9, 55, 59, 1, 6, 59, 63, 2,
    63, 9, 67, 1, 67, 6, 71, 1, 71, 13, 75, 1, 6, 75, 79, 1, 9, 79, 83, 2, 9,
    83, 87, 1, 87, 6, 91, 1, 91, 13, 95, 2, 6, 95, 99, 1, 10, 99, 103, 2, 103,
    9, 107, 1, 6, 107, 111, 1, 10, 111, 115, 2, 6, 115, 119, 1, 5, 119, 123, 1,
    123, 13, 127, 1, 127, 5, 131, 1, 6, 131, 135, 2, 135, 13, 139, 1, 139, 2,
    143, 1, 143, 10, 0, 99, 2, 0, 14, 0
]


def sum_prog(program=[], position=0):
    pos1, pos2, result = program[position + 1:position + 4]
    program[result] = program[pos1] + program[pos2]
    return program


def multiply_prog(program=[], position=0):
    pos1, pos2, result = program[position + 1:position + 4]
    program[result] = program[pos1] * program[pos2]
    return program


def opcode_three(program=[], position=0, input_param=0):
    parameter = program[position + 1]
    program[parameter] = input_param
    return program


def opcode_four(program=[], position=0):
    return (program, program[position + 1])


def execute_prog(program=[], position=0):
    opcode = program[position]
    if opcode == 1:
        return (sum_prog(program, position), True)
    elif opcode == 2:
        return (multiply_prog(program, position), True)
    elif opcode == 3:
        return (opcode_three(program, position), True)
    elif opcode == 4:
        return (opcode_four(program, position), True)
    elif opcode == 99:
        return (program, False)
    return ("something went wrong", False)


noun = 0
verb = 0
output = 19690720
prog = init_prog.copy()

while prog[0] != output:
    prog = init_prog.copy()
    prog[1] = noun
    prog[2] = verb

    for position in range(0, len(prog), 4):
        (prog, is_ok) = execute_prog(prog, position)
        if not is_ok:
            break

    if prog[0] == 19690720:
        print("noun = ", noun, "verb = ", verb, "prog[0] = ", prog[0])
        print("result = ", ((100 * noun) + verb))
        break

    if noun == 99:
        verb += 1
    noun = (noun + 1) % 100

    if verb == 100:
        print("verb == 100")
        break

# print("noun = ", noun, "verb = ", verb)
# print("result = ", ((100 * noun) + verb))
