from .intcode_machine.intcode import Program

program = []
with open("day13/input.txt") as file:
    program = file.read().split(",")
    program = [int(x) for x in program]

program = Program(program)


def program_output(program: "Program") -> tuple:
    temp = [0, 0, 0]
    for i in range(3):
        temp[i] = program.run()
    return tuple(temp)


output = 0
block_counter = 0
while output != -1:
    output = program.run()
    if output == 2:
        block_counter += 1

print(block_counter)
