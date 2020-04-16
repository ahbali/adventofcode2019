from .intcode_machine.intcode import Program

program = []
with open("day13/input.txt") as file:
    program = file.read().split(",")
    program = [int(x) for x in program]

program = Program(program)
program.program[0] = 2


def program_output(program: "Program") -> tuple:
    temp = [0, 0, 0]
    for i in range(3):
        try:
            temp[i] = program.run()
        except Exception:
            program.input = [1, 1, 1]
            temp[i] = program.run()
        if temp[i] == "end":
            return False
    return tuple(temp)


temp = True
while temp:
    temp = program_output(program)
    if temp[0] == -1:
        print(temp)

# print(program.input)
