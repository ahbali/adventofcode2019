from itertools import permutations


class Program():
    def __init__(self, program=[]):
        self.program = program
        self.program.extend([0 for i in range(6000)])
        self.position = 0
        self.relative_base = 0
        self.input = []
        self.output = 0

    # @staticmethod
    def value_from_param(self, param, mode):
        """
        returns the value from a parameter using the mode
        position mode
        immediat mode
        relative mode
        """
        if mode == "0":
            return self.program[param]
        elif mode == "1":
            return param
        elif mode == "2":
            address = self.relative_base + param
            return self.program[address]

    def opcode_one(self, mode=""):
        """
        adds together numbers read from two positions
        and stores the result in a third position
        """
        param1 = self.program[self.position + 1]
        param2 = self.program[self.position + 2]
        param3 = self.program[self.position + 3]
        val1 = self.value_from_param(param1, mode[-1])
        val2 = self.value_from_param(param2, mode[-2])
        # result_address = self.value_from_param(param3, mode[0])
        result_address = param3 if mode[
            0] == "0" else param3 + self.relative_base
        # result_address = param3
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
        param3 = self.program[self.position + 3]
        val1 = self.value_from_param(param1, mode[-1])
        val2 = self.value_from_param(param2, mode[-2])
        # result_address = self.value_from_param(param3, mode[0])
        result_address = param3 if mode[
            0] == "0" else param3 + self.relative_base
        # result_address = param3
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
        result_address = param1 if mode[
            -1] == "0" else param1 + self.relative_base
        self.program[result_address] = self.input.pop()
        self.position += 2
        # print("op_three : save ", self.input, " in address", param1,
        #       " next position = ", self.position)

    def opcode_four(self, mode=""):
        """
        Opcode 4 outputs the value of its only parameter
        """
        param1 = self.program[self.position + 1]
        value = self.value_from_param(param1, mode[-1])
        self.output = value
        self.position += 2
        print(self.output, end=",")
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
        val1 = self.value_from_param(param1, mode[-1])
        val2 = self.value_from_param(param2, mode[-2])
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
        val1 = self.value_from_param(param1, mode[-1])
        val2 = self.value_from_param(param2, mode[-2])
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
        param3 = self.program[self.position + 3]
        # result_address = self.value_from_param(param3, mode[0])
        result_address = param3 if mode[
            0] == "0" else param3 + self.relative_base
        # result_address = param3
        val1 = self.value_from_param(param1, mode[-1])
        val2 = self.value_from_param(param2, mode[-2])

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
        param3 = self.program[self.position + 3]
        # result_address = self.value_from_param(param3, mode[0])
        result_address = param3 if mode[
            0] == "0" else param3 + self.relative_base
        # result_address = param3
        val1 = self.value_from_param(param1, mode[-1])
        val2 = self.value_from_param(param2, mode[-2])

        if val1 == val2:
            self.program[result_address] = 1
        else:
            self.program[result_address] = 0

        self.position += 4

    def opcode_nine(self, mode=""):
        """
        Opcode 9 adjusts the relative base by the value of its only parameter.
        The relative base increases (or decreases, if the value is negative)
        by the value of the parameter.
        """
        param1 = self.program[self.position + 1]
        value1 = self.value_from_param(param1, mode[-1])
        self.relative_base += value1
        self.position += 2

    def opcode_99(self):
        """
        99 means that the program is finished and should immediately halt
        """
        pass

    @staticmethod
    def gen_opcode(number):
        """
        not used anymore in this program because we are using zfill() instead
        now.
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
                # print("opcode 1")
                self.opcode_one(mode)
            elif opcode == 2:
                # print("opcode 2")
                self.opcode_two(mode)
            elif opcode == 3:
                # print("opcode 3")
                self.opcode_three(mode)
            elif opcode == 4:
                # print("opcode 4")
                self.opcode_four(mode)
                # print("output = ", self.output)
                # return self.output
            elif opcode == 5:
                # print("opcode 5")
                self.opcode_five(mode)
            elif opcode == 6:
                # print("opcode 6")
                self.opcode_six(mode)
            elif opcode == 7:
                # print("opcode 7")
                self.opcode_seven(mode)
            elif opcode == 8:
                # print("opcode 8")
                self.opcode_eight(mode)
            elif opcode == 9:
                # print("opcode 9")
                self.opcode_nine(mode)
            elif opcode == 99:
                # result = self.output
                # print("input is = ", self.input)
                # print("output is = ", self.output)
                # print("the result is = ", result)
                # print("program will halt with output = ", self.output)
                print("end of the program")
                return self.output
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

    amps = [amp1, amp2, amp3, amp4, amp5]

    while amp_output is not None:
        counter = 0
        for amp in amps:
            amp.input.append(amp_output)
            amp_output = amp.run()
            # print("output of amp", counter, "is: ", amp_output)
            counter += 1

    # program = Program(init_program)
    # for i in sequence:
    #     program.input = [amp_output, i]
    #     amp_output = program.run()[-1]
    #     program.position = 0
    #     program.output = []
    return amp5.output


init_prog = [
    1102, 34463338, 34463338, 63, 1007, 63, 34463338, 63, 1005, 63, 53, 1102,
    3, 1, 1000, 109, 988, 209, 12, 9, 1000, 209, 6, 209, 3, 203, 0, 1008, 1000,
    1, 63, 1005, 63, 65, 1008, 1000, 2, 63, 1005, 63, 904, 1008, 1000, 0, 63,
    1005, 63, 58, 4, 25, 104, 0, 99, 4, 0, 104, 0, 99, 4, 17, 104, 0, 99, 0, 0,
    1101, 0, 26, 1014, 1102, 1, 30, 1013, 1101, 22, 0, 1000, 1101, 0, 35, 1015,
    1101, 0, 34, 1011, 1102, 0, 1, 1020, 1102, 1, 481, 1022, 1101, 0, 36, 1003,
    1102, 1, 28, 1005, 1101, 857, 0, 1024, 1101, 20, 0, 1008, 1101, 0, 385,
    1026, 1102, 37, 1, 1006, 1101, 33, 0, 1017, 1101, 0, 38, 1002, 1102, 23, 1,
    1007, 1102, 32, 1, 1010, 1101, 29, 0, 1016, 1102, 1, 25, 1009, 1102, 1, 27,
    1012, 1101, 24, 0, 1018, 1101, 474, 0, 1023, 1102, 1, 39, 1004, 1101, 0,
    31, 1001, 1102, 378, 1, 1027, 1101, 0, 848, 1025, 1102, 21, 1, 1019, 1102,
    760, 1, 1029, 1102, 1, 1, 1021, 1101, 769, 0, 1028, 109, -6, 2107, 21, 6,
    63, 1005, 63, 199, 4, 187, 1106, 0, 203, 1001, 64, 1, 64, 1002, 64, 2, 64,
    109, 16, 2101, 0, -6, 63, 1008, 63, 39, 63, 1005, 63, 225, 4, 209, 1106, 0,
    229, 1001, 64, 1, 64, 1002, 64, 2, 64, 109, 5, 2108, 20, -7, 63, 1005, 63,
    247, 4, 235, 1105, 1, 251, 1001, 64, 1, 64, 1002, 64, 2, 64, 109, -1, 2108,
    36, -8, 63, 1005, 63, 267, 1106, 0, 273, 4, 257, 1001, 64, 1, 64, 1002, 64,
    2, 64, 109, -13, 1201, -1, 0, 63, 1008, 63, 22, 63, 1005, 63, 299, 4, 279,
    1001, 64, 1, 64, 1106, 0, 299, 1002, 64, 2, 64, 109, 15, 2102, 1, -8, 63,
    1008, 63, 20, 63, 1005, 63, 321, 4, 305, 1106, 0, 325, 1001, 64, 1, 64,
    1002, 64, 2, 64, 109, -13, 21108, 40, 40, 8, 1005, 1011, 347, 4, 331, 1001,
    64, 1, 64, 1105, 1, 347, 1002, 64, 2, 64, 109, -2, 1207, 8, 24, 63, 1005,
    63, 363, 1105, 1, 369, 4, 353, 1001, 64, 1, 64, 1002, 64, 2, 64, 109, 35,
    2106, 0, -9, 1001, 64, 1, 64, 1106, 0, 387, 4, 375, 1002, 64, 2, 64, 109,
    -26, 21102, 41, 1, 3, 1008, 1013, 41, 63, 1005, 63, 409, 4, 393, 1106, 0,
    413, 1001, 64, 1, 64, 1002, 64, 2, 64, 109, 2, 1202, -6, 1, 63, 1008, 63,
    36, 63, 1005, 63, 433, 1106, 0, 439, 4, 419, 1001, 64, 1, 64, 1002, 64, 2,
    64, 109, -3, 21102, 42, 1, 10, 1008, 1019, 40, 63, 1005, 63, 463, 1001, 64,
    1, 64, 1106, 0, 465, 4, 445, 1002, 64, 2, 64, 109, 15, 2105, 1, -1, 1001,
    64, 1, 64, 1106, 0, 483, 4, 471, 1002, 64, 2, 64, 109, -27, 1207, 3, 23,
    63, 1005, 63, 505, 4, 489, 1001, 64, 1, 64, 1105, 1, 505, 1002, 64, 2, 64,
    109, 13, 2102, 1, -9, 63, 1008, 63, 28, 63, 1005, 63, 525, 1105, 1, 531, 4,
    511, 1001, 64, 1, 64, 1002, 64, 2, 64, 109, 1, 2101, 0, -8, 63, 1008, 63,
    35, 63, 1005, 63, 551, 1105, 1, 557, 4, 537, 1001, 64, 1, 64, 1002, 64, 2,
    64, 109, 6, 21107, 43, 44, -4, 1005, 1013, 575, 4, 563, 1106, 0, 579, 1001,
    64, 1, 64, 1002, 64, 2, 64, 109, -9, 1201, -4, 0, 63, 1008, 63, 40, 63,
    1005, 63, 599, 1105, 1, 605, 4, 585, 1001, 64, 1, 64, 1002, 64, 2, 64, 109,
    12, 1206, 1, 621, 1001, 64, 1, 64, 1106, 0, 623, 4, 611, 1002, 64, 2, 64,
    109, -22, 1202, 9, 1, 63, 1008, 63, 23, 63, 1005, 63, 649, 4, 629, 1001,
    64, 1, 64, 1105, 1, 649, 1002, 64, 2, 64, 109, 17, 1206, 5, 667, 4, 655,
    1001, 64, 1, 64, 1106, 0, 667, 1002, 64, 2, 64, 109, -3, 1205, 9, 685, 4,
    673, 1001, 64, 1, 64, 1106, 0, 685, 1002, 64, 2, 64, 109, 3, 1208, -9, 37,
    63, 1005, 63, 707, 4, 691, 1001, 64, 1, 64, 1105, 1, 707, 1002, 64, 2, 64,
    109, 7, 1205, -2, 723, 1001, 64, 1, 64, 1106, 0, 725, 4, 713, 1002, 64, 2,
    64, 109, -15, 21101, 44, 0, 8, 1008, 1015, 45, 63, 1005, 63, 745, 1105, 1,
    751, 4, 731, 1001, 64, 1, 64, 1002, 64, 2, 64, 109, 28, 2106, 0, -7, 4,
    757, 1001, 64, 1, 64, 1106, 0, 769, 1002, 64, 2, 64, 109, -12, 21101, 45,
    0, -5, 1008, 1018, 45, 63, 1005, 63, 791, 4, 775, 1105, 1, 795, 1001, 64,
    1, 64, 1002, 64, 2, 64, 109, -9, 2107, 26, -5, 63, 1005, 63, 815, 1001, 64,
    1, 64, 1106, 0, 817, 4, 801, 1002, 64, 2, 64, 109, -1, 21107, 46, 45, -3,
    1005, 1010, 833, 1105, 1, 839, 4, 823, 1001, 64, 1, 64, 1002, 64, 2, 64,
    109, 3, 2105, 1, 8, 4, 845, 1001, 64, 1, 64, 1106, 0, 857, 1002, 64, 2, 64,
    109, -9, 1208, -4, 37, 63, 1005, 63, 877, 1001, 64, 1, 64, 1105, 1, 879, 4,
    863, 1002, 64, 2, 64, 109, 8, 21108, 47, 46, 2, 1005, 1017, 895, 1106, 0,
    901, 4, 885, 1001, 64, 1, 64, 4, 64, 99, 21102, 1, 27, 1, 21102, 1, 915, 0,
    1106, 0, 922, 21201, 1, 14429, 1, 204, 1, 99, 109, 3, 1207, -2, 3, 63,
    1005, 63, 964, 21201, -2, -1, 1, 21102, 1, 942, 0, 1105, 1, 922, 21202, 1,
    1, -1, 21201, -2, -3, 1, 21101, 957, 0, 0, 1106, 0, 922, 22201, 1, -1, -2,
    1105, 1, 968, 21201, -2, 0, -2, 109, -3, 2105, 1, 0
]
# init_prog = [
#     109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99
# ]
# takes no input and produces a copy of itself as output.

# init_prog = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
# # should output a 16-digit number.

# init_prog = [104, 1125899906842624, 99]
# # should output the large number in the middle.

# print(len(init_prog))

# instruction = str("21106").zfill(5)
# opcode = int(instruction[-2:])
# mode = instruction[:-2]
# print("opcode", opcode)
# print("mode", mode[-3])

program = Program(init_prog.copy())
program.input = [2]
result = program.run()
# print("position", program.position)
print("the result is : ", result)

# max_sequence = ()
# max_value = 0
# # for sequence in phase_generator():
# my_sequence = permutations(range(5, 10))
# for sequence in my_sequence:
#     temp_value = global_runner(sequence, init_prog)
#     if temp_value > max_value:
#         max_value = temp_value
#         max_sequence = sequence

# print("max value : ", max_value, " from sequence : ", max_sequence)

# number = 3
# print(f"{number:05d}")
