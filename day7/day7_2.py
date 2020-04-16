from itertools import permutations


class Program():
    def __init__(self, program):
        self.program = program
        self.position = 0
        self.input = []
        self.output = 0

    def opcode_one(self, mode=""):
        """
        adds together numbers read from two positions
        and stores the result in a third position
        """
        param1 = self.program[self.position + 1]
        param2 = self.program[self.position + 2]
        val1 = param1 if mode[-1] == "1" else self.program[param1]
        val2 = param2 if mode[-2] == "1" else self.program[param2]
        result_address = self.program[self.position + 3]
        self.program[result_address] = val1 + val2
        self.position += 4
        # print("op_one : sum ", val1, " and ", val2, "result address = ",
        #       result_address, " next position = ", self.position)

    def opcode_two(self, mode=""):
        """
        works exactly like opcode 1, except it
        multiplies the two inputs instead of adding them
        """
        # val1, val2, result = self.program[self.position + 1:self.position + 4]
        # self.program[result] = self.program[val1] * self.program[val2]
        param1 = self.program[self.position + 1]
        param2 = self.program[self.position + 2]
        val1 = param1 if mode[-1] == "1" else self.program[param1]
        val2 = param2 if mode[-2] == "1" else self.program[param2]
        result_address = self.program[self.position + 3]
        self.program[result_address] = val1 * val2
        self.position += 4
        # print("op_two : multiply ", val1, " and ", val2, "result address = ",
        #       result_address, " next position = ", self.position)

    def opcode_three(self, mode=""):
        """
        Opcode 3 takes a single integer as input and saves
        it to the position given by its only parameter
        """
        param1 = self.program[self.position + 1]
        self.program[param1] = self.input.pop()
        self.position += 2
        # print("op_three : save ", self.input, " in address", param1,
        #       " next position = ", self.position)

    def opcode_four(self, mode=""):
        """
        Opcode 4 outputs the value of its only parameter
        """
        param1 = self.program[self.position + 1]
        value = param1 if mode[-1] == "1" else self.program[param1]
        self.output = value
        self.position += 2
        # print("op_four : output value", value, " next position = ",
        #       self.position)

    def opcode_five(self, mode=""):
        """
        Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets
        the instruction pointer to the value from the second parameter.
        Otherwise, it does nothing.
        """
        param1 = self.program[self.position + 1]
        param2 = self.program[self.position + 2]
        val1 = param1 if mode[-1] == "1" else self.program[param1]
        val2 = param2 if mode[-2] == "1" else self.program[param2]
        if val1 == 0:
            self.position += 3
        else:
            self.position = val2
        # print("op_five : jumpiftrue ", val1, " to ", val2, " next position = ",
        #       self.position)

    def opcode_six(self, mode=""):
        """
        Opcode 6 is jump-if-false: if the first parameter is zero, it sets
        the instruction pointer to the value from the second parameter.
        Otherwise, it does nothing.
        """
        param1 = self.program[self.position + 1]
        param2 = self.program[self.position + 2]
        val1 = param1 if mode[-1] == "1" else self.program[param1]
        val2 = param2 if mode[-2] == "1" else self.program[param2]
        if val1 == 0:
            self.position = val2
        else:
            self.position += 3

    def opcode_seven(self, mode=""):
        """
        Opcode 7 is less than: if the first parameter is less than the second
        parameter, it stores 1 in the position given by the third parameter.
        Otherwise, it stores 0.
        """
        param1 = self.program[self.position + 1]
        param2 = self.program[self.position + 2]
        result_address = self.program[self.position + 3]
        # result_address = self.program[param3]
        val1 = param1 if mode[-1] == "1" else self.program[param1]
        val2 = param2 if mode[-2] == "1" else self.program[param2]

        if val1 < val2:
            self.program[result_address] = 1
        else:
            self.program[result_address] = 0

        self.position += 4

    def opcode_eight(self, mode=""):
        """
        Opcode 8 is equals: if the first parameter is equal to the second
        parameter, it stores 1 in the position given by the third parameter.
        Otherwise, it stores 0.
        """
        param1 = self.program[self.position + 1]
        param2 = self.program[self.position + 2]
        result_address = self.program[self.position + 3]
        # result_address = self.program[param3]
        val1 = param1 if mode[-1] == "1" else self.program[param1]
        val2 = param2 if mode[-2] == "1" else self.program[param2]

        if val1 == val2:
            self.program[result_address] = 1
        else:
            self.program[result_address] = 0

        self.position += 4

    def opcode_99(self):
        """
        99 means that the program is finished and should immediately halt
        """
        pass

    @staticmethod
    def gen_opcode(number):
        """
        not used anymore in this program because we are using zfill() instead now.
        left here on purpose :)
        """
        # string = "".join(str(number))
        # result = string
        # for i in range(5 - len(string)):
        #     result = "0" + result
        number = str(number)
        result = "0" * (5 - len(number)) + number
        return result

    def run(self):
        while True:
            # instruction = self.gen_opcode(self.program[self.position])
            instruction = str(self.program[self.position]).zfill(5)
            opcode = int(instruction[-2:])
            mode = instruction[:-2]
            if opcode == 1:
                self.opcode_one(mode)
            elif opcode == 2:
                self.opcode_two(mode)
            elif opcode == 3:
                self.opcode_three(mode)
            elif opcode == 4:
                self.opcode_four(mode)
                # print("output = ", self.output)
                return self.output
            elif opcode == 5:
                self.opcode_five(mode)
            elif opcode == 6:
                self.opcode_six(mode)
            elif opcode == 7:
                self.opcode_seven(mode)
            elif opcode == 8:
                self.opcode_eight(mode)
            elif opcode == 99:
                # result = self.output
                # print("input is = ", self.input)
                # print("output is = ", self.output)
                # print("the result is = ", result)
                # print("program will halt with output = ", self.output)
                return None
            else:
                return "something went wrong"


def global_runner(sequence=[], init_program=[]):
    amp1 = Program(init_prog.copy())
    amp2 = Program(init_prog.copy())
    amp3 = Program(init_prog.copy())
    amp4 = Program(init_prog.copy())
    amp5 = Program(init_prog.copy())

    # initial run of the program
    amp1.input = [0, sequence[0]]
    amp2.input = [amp1.run(), sequence[1]]
    amp3.input = [amp2.run(), sequence[2]]
    amp4.input = [amp3.run(), sequence[3]]
    amp5.input = [amp4.run(), sequence[4]]
    amp_output = amp5.run()
    # amp_output = amp1.run()
    # amp2.input = [amp_output, sequence[1]]
    # amp_output = amp2.run()
    # amp3.input = [amp_output, sequence[2]]
    # amp_output = amp3.run()
    # amp4.input = [amp_output, sequence[3]]
    # amp_output = amp4.run()
    # amp5.input = [amp_output, sequence[4]]
    # amp_output = amp5.run()

    amps = [amp1, amp2, amp3, amp4, amp5]

    while amp_output != None:
        counter = 0
        for amp in amps:
            amp.input.append(amp_output)
            amp_output = amp.run()
            # print("output of amp", counter, "is: ", amp_output)
            counter += 1
        # amp1.input.append(amp_output)
        # amp_output = amp1.run()
        # amp2.input.append(amp_output)
        # amp_output = amp2.run()
        # amp3.input.append(amp_output)
        # amp_output = amp3.run()
        # amp4.input.append(amp_output)
        # amp_output = amp4.run()
        # amp5.input.append(amp_output)
        # amp_output = amp5.run()

    # program = Program(init_program)
    # for i in sequence:
    #     program.input = [amp_output, i]
    #     amp_output = program.run()[-1]
    #     program.position = 0
    #     program.output = []
    return amp5.output


def phase_generator():
    sequence_set = set()
    for i in range(5, 10):
        sequence_set.add(i)

    temp_set = set()
    for phase_one in sequence_set:
        temp_set.add(phase_one)
        for phase_two in sequence_set.difference(temp_set):
            temp_set.add(phase_two)
            for phase_three in sequence_set.difference(temp_set):
                temp_set.add(phase_three)
                for phase_four in sequence_set.difference(temp_set):
                    temp_set.add(phase_four)
                    for phase_five in sequence_set.difference(temp_set):
                        sequence = (phase_one, phase_two, phase_three,
                                    phase_four, phase_five)
                        yield sequence
                        temp_set.discard(phase_five)
                    temp_set.discard(phase_four)
                temp_set.discard(phase_three)
            temp_set.discard(phase_two)
        temp_set.discard(phase_one)


# init_prog = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]

# this is my input:
init_prog = [
    3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 42, 67, 84, 109, 126, 207, 288,
    369, 450, 99999, 3, 9, 102, 4, 9, 9, 1001, 9, 4, 9, 102, 2, 9, 9, 101, 2,
    9, 9, 4, 9, 99, 3, 9, 1001, 9, 5, 9, 1002, 9, 5, 9, 1001, 9, 5, 9, 1002, 9,
    5, 9, 101, 5, 9, 9, 4, 9, 99, 3, 9, 101, 5, 9, 9, 1002, 9, 3, 9, 1001, 9,
    2, 9, 4, 9, 99, 3, 9, 1001, 9, 2, 9, 102, 4, 9, 9, 101, 2, 9, 9, 102, 4, 9,
    9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 101, 5, 9, 9, 1002, 9, 2,
    9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9,
    1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3,
    9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4,
    9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 99, 3, 9, 1001, 9,
    2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9,
    1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3,
    9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4,
    9, 3, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9,
    1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002,
    9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9,
    101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99,
    3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4,
    9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1,
    9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2,
    9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9,
    1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9,
    3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9,
    4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2,
    9, 4, 9, 99
]
# init_prog = [
#     3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27,
#     1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5
# ]
# 139629729
# sequence = [9, 8, 7, 6, 5]

# init_prog = [
#     3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55,
#     26, 1001, 54, -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001,
#     55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0,
#     0, 0, 10
# ]
# # 18216
# sequence = [9, 7, 8, 5, 6]
# temp_value = global_runner(sequence, init_prog)

# print("global output: ", temp_value)
max_sequence = ()
max_value = 0
my_sequence = permutations(range(5, 10))
for sequence in my_sequence:
    temp_value = global_runner(sequence, init_prog)
    if temp_value > max_value:
        max_value = temp_value
        max_sequence = sequence

print("max value : ", max_value, " from sequence : ", max_sequence)

# number = 3
# print(f"{number:05d}")
