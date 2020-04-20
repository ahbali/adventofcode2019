from intcode_machine.intcode import Program


class Game:
    def __init__(self, program: list):
        self.program = Program(program)
        self.walls = set()
        self.blocks = set()
        self.horizontal_paddle = (0, 0)
        self.ball = (1000, 1000)
        self.score = 0

    def program_output(self) -> tuple:
        temp = [0, 0, 0]
        for i in range(3):
            temp[i] = self.program.run()
            # try:
            #     temp[i] = self.program.run()
            # except Exception:
            #     # self.program.input = [0]
            #     self.track_ball()
            #     temp[i] = self.program.run()
            if temp[i] == "end":
                return False
        return tuple(temp)

    def track_ball(self):
        ball_x, ball_y = self.ball
        paddle_x, paddle_y = self.horizontal_paddle
        diff = ball_x - paddle_x
        if paddle_x < ball_x:
            self.program.input = [1 for _ in range(abs(diff))]
        elif paddle_x > ball_x:
            self.program.input = [-1 for _ in range(abs(diff))]
        else:
            self.program.input = [0]

    def gen_paddle_movement(self, old_x: int):
        """Unused left here for future reference"""
        # print("hello")
        current_x, current_y = self.ball
        paddle_x, paddle_y = self.horizontal_paddle
        cycles_before_collision = paddle_y - current_y
        if current_x < old_x:
            collision_point_x = current_x - cycles_before_collision
        elif current_x > old_x:
            collision_point_x = current_x + cycles_before_collision
        else:
            print("should not happen")

        paddle_move = paddle_x - collision_point_x
        if paddle_move < 0:
            self.program.input = [1 for _ in range(abs(paddle_move))]
        else:
            self.program.input = [-1 for _ in range(abs(paddle_move))]
        print(self.program.input)

    def play(self):
        while True:
            old_x, old_y = self.ball
            temp = self.program_output()
            if temp is False:
                return -1
            if temp[0] == -1:
                self.score = temp[2] if temp[2] != 0 else self.score

            tile_id = temp[2]

            # if tile_id == 0:
            #     pass
            # elif tile_id == 1:
            #     self.walls.add(temp[:-1])
            # elif tile_id == 2:
            #     self.blocks.add(temp[:-1])
            if tile_id == 3:
                self.horizontal_paddle = temp[:-1]
                # print("paddle at: ", self.horizontal_paddle)
            elif tile_id == 4:
                self.ball = temp[:-1]
                self.track_ball()
                # if self.ball[1] in (21, 22):
                #     print("*************")
                #     print("ball: ", self.ball)
                #     print("paddle: ", self.horizontal_paddle)
                #     print("--------------")
                # if self.ball[1] > old_y:
                #     if 1 not in self.program.input and -1 not in self.program.input:
                #         self.gen_paddle_movement(old_x)

                # print("ball   at: ", self.ball)


program = []
with open("day13/input.txt") as file:
    program = file.read().split(",")
    program = [int(x) for x in program]

program[0] = 2
game = Game(program)
game.play()
# print(f"blocks = {len(game.blocks)}")
print(f"ball: {game.ball}")
print(f"score = {game.score}")
# print(f"walls = {game.walls}")
