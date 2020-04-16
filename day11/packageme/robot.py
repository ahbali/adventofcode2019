class Robot:
    def __init__(self):
        self.position = (0, 0)
        self.white = set()  # implement it as map() if needed to keep numbers
        self.black = set()
        self.direction = 0  # 0 -> Up, 1 -> right, 2 -> down, 3 -> left

    def paint(self, color: int):
        if color == 0:
            self.black.add(self.position)
            self.white.discard(self.position)
        if color == 1:
            self.white.add(self.position)
            self.black.discard(self.position)

    def go(self, right_left: int):
        """
        0 -> turn left
        1 -> turn right
        """
        if self.direction == 0:  # direction up
            if right_left == 0:
                self.direction = 3
                x, y = self.position
                self.position = (x - 1, y)
            else:
                self.direction = 1
                x, y = self.position
                self.position = (x + 1, y)

        elif self.direction == 1:  # direction right
            if right_left == 0:
                self.direction = 0
                x, y = self.position
                self.position = (x, y + 1)
            else:
                self.direction = 2
                x, y = self.position
                self.position = (x, y - 1)

        elif self.direction == 2:  # direction down
            if right_left == 0:
                self.direction = 1
                x, y = self.position
                self.position = (x + 1, y)
            else:
                self.direction = 3
                x, y = self.position
                self.position = (x - 1, y)

        elif self.direction == 3:  # direction left
            if right_left == 0:
                self.direction = 2
                x, y = self.position
                self.position = (x, y - 1)
            else:
                self.direction = 0
                x, y = self.position
                self.position = (x, y + 1)

    def get_color(self) -> int:
        if self.position in self.white:
            return 1
        return 0

    def execute(self, command: tuple):
        color, direction = command
        self.paint(color)
        self.go(direction)
