class Program:
    def __init__(self, program=[]):
        self.program = program
        self.program.extend([0 for i in range(6000)])
        self.position = 0
        self.relative_base = 0
        self.input = []
        self.output = 0
        # self.output_counter = 0

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
        result_address = param3 if mode[0] == "0" else param3 + self.relative_base
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
        param1 = self.program[self.position + 1]
        param2 = self.program[self.position + 2]
        param3 = self.program[self.position + 3]
        val1 = self.value_from_param(param1, mode[-1])
        val2 = self.value_from_param(param2, mode[-2])
        # result_address = self.value_from_param(param3, mode[0])
        result_address = param3 if mode[0] == "0" else param3 + self.relative_base
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
        result_address = param1 if mode[-1] == "0" else param1 + self.relative_base
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
        # self.output_counter += 1
        # print(self.output, end=",")
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
        # print("op_five : jumpiftrue ", val1, " to ", val2,
        # " next position = ", self.position)

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
        result_address = param3 if mode[0] == "0" else param3 + self.relative_base
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
        result_address = param3 if mode[0] == "0" else param3 + self.relative_base
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
                # if self.output_counter == 3:
                #     self.output_counter = 0
                return self.output
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
                return "end"
            else:
                return "something went wrong"
