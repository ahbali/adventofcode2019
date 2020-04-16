from math import gcd


class Moon:
    def __init__(self, coordinates: tuple):
        self.coordinates = coordinates
        self.velocity = [0, 0, 0]

    def gravity(self, other_moon: "Moon"):
        for i, coordinate in enumerate(self.coordinates):
            if coordinate < other_moon.coordinates[i]:
                self.velocity[i] += 1
            elif coordinate > other_moon.coordinates[i]:
                self.velocity[i] -= 1

    def apply_velocity(self):
        self.coordinates = tuple(i + j for i, j in zip(self.coordinates, self.velocity))
        # for i, value in enumerate(self.coordinates):
        #     self.coordinates[i] = value + self.velocity[i]

    def potential_energy(self):
        return sum(abs(x) for x in self.coordinates)

    def kinetic_energy(self):
        return sum(abs(x) for x in self.velocity)

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def flatten(self, i: int):
        # return list(self.coordinates) + self.velocity
        return [self.coordinates[i], self.velocity[i]]


def flatten_system(system: tuple, i: int) -> tuple:
    tmp = []
    for x in system:
        tmp.extend(x.flatten(i))
    temp_tuple = tuple(tmp)
    return temp_tuple


def print_system(system: tuple):
    for moon in system:
        print("coordinates: ", moon.coordinates, end=", ")
        print("velocity: ", moon.velocity)


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)


satellite1 = Moon((-7, -8, 9))
satellite2 = Moon((-12, -3, -4))
satellite3 = Moon((6, -17, -9))
satellite4 = Moon((4, -10, -6))

# satellite1 = Moon((-1, 0, 2))
# satellite2 = Moon((2, -10, -7))
# satellite3 = Moon((4, -8, 8))
# satellite4 = Moon((3, 5, -1))


# satellite1 = Moon((-8, -10, 0))
# satellite2 = Moon((5, 5, 10))
# satellite3 = Moon((2, -7, 3))
# satellite4 = Moon((9, -8, -3))

system = (satellite1, satellite2, satellite3, satellite4)
cycles = []

for i in range(3):
    states = set()
    steps = 0
    count = 0
    while True:
        for moon in system:
            for other_moon in system:
                if moon != other_moon:
                    moon.gravity(other_moon)
        for moon in system:
            moon.apply_velocity()
        temp_tuple = flatten_system(system, i)
        if temp_tuple not in states:
            states.add(temp_tuple)
        else:
            cycles.append(steps)
            print("steps = ", steps)
            break
            # count += 1
            # if count == 4:
            #     break
        steps += 1
# system_energie = 0
print(cycles)
multiple = lcm(cycles[0], cycles[1])
multiple = lcm(multiple, cycles[2])
print("solution = ", multiple)
# now we need to calculate the LCM(Least Common Multiple) for those numbers

# print_system(system)
#     system_energie += moon.total_energy()
#     print("total energie= ", moon.total_energy())
#
# print("total system energie = ", system_energie)
