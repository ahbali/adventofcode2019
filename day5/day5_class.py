class Program():
    def __init__(self, program):
        self.program = program
        self.position = 0
        self.input = 0
        self.output = []

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
        self.program[param1] = self.input
        self.position += 2
        # print("op_three : save ", self.input, " in address", param1,
        #       " next position = ", self.position)

    def opcode_four(self, mode=""):
        """
        Opcode 4 outputs the value of its only parameter
        """
        param1 = self.program[self.position + 1]
        value = param1 if mode[-1] == "1" else self.program[param1]
        self.output.append(value)
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
        # string = "".join(str(number))
        # result = string
        # for i in range(5 - len(string)):
        #     result = "0" + result
        number = str(number)
        result = "0" * (5 - len(number)) + number
        return result

    def run(self):
        while True:
            instruction = self.gen_opcode(self.program[self.position])
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
                print("output is = ", self.output)
                # print("the result is = ", result)
                return 0
            else:
                return "something went wrong"


# init_prog = [
#     1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 19, 5, 23,
#     1, 9, 23, 27, 2, 27, 6, 31, 1, 5, 31, 35, 2, 9, 35, 39, 2, 6, 39, 43, 2,
#     43, 13, 47, 2, 13, 47, 51, 1, 10, 51, 55, 1, 9, 55, 59, 1, 6, 59, 63, 2,
#     63, 9, 67, 1, 67, 6, 71, 1, 71, 13, 75, 1, 6, 75, 79, 1, 9, 79, 83, 2, 9,
#     83, 87, 1, 87, 6, 91, 1, 91, 13, 95, 2, 6, 95, 99, 1, 10, 99, 103, 2, 103,
#     9, 107, 1, 6, 107, 111, 1, 10, 111, 115, 2, 6, 115, 119, 1, 5, 119, 123, 1,
#     123, 13, 127, 1, 127, 5, 131, 1, 6, 131, 135, 2, 135, 13, 139, 1, 139, 2,
#     143, 1, 143, 10, 0, 99, 2, 0, 14, 0
# ]

# init_prog[1] = 12
# init_prog[2] = 2
# init_prog = [1, 1, 1, 4, 99, 5, 6, 0, 99]
# init_prog = [1101, 100, -1, 4, 0]
# init_prog = [3, 0, 4, 0, 99]

init_prog = [
    3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 61, 45, 225, 102,
    94, 66, 224, 101, -3854, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 7,
    224, 1, 223, 224, 223, 1101, 31, 30, 225, 1102, 39, 44, 224, 1001, 224,
    -1716, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 7, 224, 1, 224, 223, 223,
    1101, 92, 41, 225, 101, 90, 40, 224, 1001, 224, -120, 224, 4, 224, 102, 8,
    223, 223, 1001, 224, 1, 224, 1, 223, 224, 223, 1101, 51, 78, 224, 101,
    -129, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 6, 224, 1, 224, 223,
    223, 1, 170, 13, 224, 101, -140, 224, 224, 4, 224, 102, 8, 223, 223, 1001,
    224, 4, 224, 1, 223, 224, 223, 1101, 14, 58, 225, 1102, 58, 29, 225, 1102,
    68, 70, 225, 1002, 217, 87, 224, 101, -783, 224, 224, 4, 224, 102, 8, 223,
    223, 101, 2, 224, 224, 1, 224, 223, 223, 1101, 19, 79, 225, 1001, 135, 42,
    224, 1001, 224, -56, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 6, 224, 1,
    224, 223, 223, 2, 139, 144, 224, 1001, 224, -4060, 224, 4, 224, 102, 8,
    223, 223, 101, 1, 224, 224, 1, 223, 224, 223, 1102, 9, 51, 225, 4, 223, 99,
    0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227,
    247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106,
    227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274,
    1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294,
    0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225,
    225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1008, 677, 226, 224, 102,
    2, 223, 223, 1006, 224, 329, 101, 1, 223, 223, 108, 677, 677, 224, 102, 2,
    223, 223, 1005, 224, 344, 101, 1, 223, 223, 107, 677, 677, 224, 1002, 223,
    2, 223, 1005, 224, 359, 101, 1, 223, 223, 1107, 226, 677, 224, 1002, 223,
    2, 223, 1005, 224, 374, 1001, 223, 1, 223, 1008, 677, 677, 224, 102, 2,
    223, 223, 1006, 224, 389, 1001, 223, 1, 223, 1007, 677, 677, 224, 1002,
    223, 2, 223, 1006, 224, 404, 1001, 223, 1, 223, 8, 677, 226, 224, 102, 2,
    223, 223, 1005, 224, 419, 1001, 223, 1, 223, 8, 226, 226, 224, 102, 2, 223,
    223, 1006, 224, 434, 101, 1, 223, 223, 1107, 226, 226, 224, 1002, 223, 2,
    223, 1006, 224, 449, 101, 1, 223, 223, 1107, 677, 226, 224, 102, 2, 223,
    223, 1005, 224, 464, 101, 1, 223, 223, 1108, 226, 226, 224, 102, 2, 223,
    223, 1006, 224, 479, 1001, 223, 1, 223, 7, 677, 677, 224, 1002, 223, 2,
    223, 1006, 224, 494, 101, 1, 223, 223, 7, 677, 226, 224, 102, 2, 223, 223,
    1005, 224, 509, 101, 1, 223, 223, 1108, 226, 677, 224, 1002, 223, 2, 223,
    1006, 224, 524, 101, 1, 223, 223, 8, 226, 677, 224, 1002, 223, 2, 223,
    1005, 224, 539, 101, 1, 223, 223, 1007, 226, 226, 224, 102, 2, 223, 223,
    1006, 224, 554, 1001, 223, 1, 223, 108, 226, 226, 224, 1002, 223, 2, 223,
    1006, 224, 569, 1001, 223, 1, 223, 1108, 677, 226, 224, 102, 2, 223, 223,
    1005, 224, 584, 101, 1, 223, 223, 108, 226, 677, 224, 102, 2, 223, 223,
    1005, 224, 599, 101, 1, 223, 223, 1007, 226, 677, 224, 102, 2, 223, 223,
    1006, 224, 614, 1001, 223, 1, 223, 1008, 226, 226, 224, 1002, 223, 2, 223,
    1006, 224, 629, 1001, 223, 1, 223, 107, 226, 226, 224, 1002, 223, 2, 223,
    1006, 224, 644, 101, 1, 223, 223, 7, 226, 677, 224, 102, 2, 223, 223, 1005,
    224, 659, 1001, 223, 1, 223, 107, 677, 226, 224, 102, 2, 223, 223, 1005,
    224, 674, 1001, 223, 1, 223, 4, 223, 99, 226
]

# init_prog = [
#     3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106,
#     0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1,
#     46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
# ]

# init_prog = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]

# init_prog = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]

# init_prog = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]

# init_prog = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]

# init_prog = []

# init_prog = []
prog = Program(init_prog)
prog.input = 5
prog.run()

# error result = output is =  [7490147]

# number = 1
# string = "".join(str(number))
# result = string
# for i in range(5 - len(string)):
#     result = "0" + result
# print(result)

# number = str(1)
# string = "0" * (5 - len(number)) + number
# print(string)

# i = int("001")
# print(i == 1)
