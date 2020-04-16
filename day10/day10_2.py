# import pprint
from operator import itemgetter


def are_aligned(point1: tuple, point2: tuple, point3: tuple) -> bool:
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    if x1 == x2:
        if x1 == x3:
            return True
        return False
    else:
        if x1 == x3:
            return False
        a = (y1 - y2) / (x1 - x2)
        b = (y1 - y3) / (x1 - x3)
        if a == b:
            return True
        return False


def is_right(origin: tuple, point: tuple):
    x0, y0 = origin
    x, y = point
    if x > x0:
        return True
    elif x < x0:
        return False
    else:
        if y > y0:
            return False
        elif y < y0:
            return True


def aligned_asteroids(origin: tuple, tested: tuple, ast_map: set) -> tuple:
    result: set = set()
    left, right = set(), set()
    result.add(tested)
    if is_right(origin, tested):
        right.add(tested)
    else:
        left.add(tested)
    # need to add tested to right or left here
    temp = ast_map.copy()
    temp.discard(origin)
    x0, y0 = origin
    for point in temp:
        if are_aligned(origin, tested, point):
            result.add(point)
            if is_right(origin, point):
                right.add(point)
            else:
                left.add(point)
    return (result, left, right)


def visible_asteroids_count(origin: tuple, ast_map: set) -> int:
    temp: set = ast_map.copy()
    temp.discard(origin)
    count = 0
    while temp:
        asteroid = temp.pop()
        alined, increment = aligned_asteroids(origin, asteroid, ast_map)
        temp = temp - alined
        count += increment
    return count


def less_than(point1: tuple, point2: tuple) -> bool:
    x1, y1 = point1
    x2, y2 = point2
    if x1 == 0:
        return False
    if x2 == 0:
        return True
    tan1 = y1 / x1
    tan2 = y2 / x2
    if tan1 < tan2:
        return True
    return False


def tan_value(point: tuple) -> float:
    x, y = point
    if x == 0 and y > 0:
        return float("inf")
    if x == 0 and y < 0:
        return float("-inf")
    tan = y / x
    return tan


def asteroids(space_map: str) -> set:
    """
    returns a tuple of asteroids coordinates from the input string
    """
    lines = space_map.split("\n")
    x, y = 0, 0
    points = []
    for line in lines:
        for char in line:
            if char == "#":
                point = (x, y)
                points.append(point)
            x += 1
        y += 1
        x = 0
    return set(points)


# best value 341  for asteroid at  (29, 32) x and y are inversed "error"
# best value 340  for asteroid at  (29, 28) x and y are inversed
if __name__ == "__main__":

    my_input = """.#....#.###.........#..##.###.#.....##...
...........##.......#.#...#...#..#....#..
...#....##..##.......#..........###..#...
....#....####......#..#.#........#.......
...............##..#....#...##..#...#..#.
..#....#....#..#.....#.#......#..#...#...
.....#.#....#.#...##.........#...#.......
#...##.#.#...#.......#....#........#.....
....##........#....#..........#.......#..
..##..........##.....#....#.........#....
...#..##......#..#.#.#...#...............
..#.##.........#...#.#.....#........#....
#.#.#.#......#.#...##...#.........##....#
.#....#..#.....#.#......##.##...#.......#
..#..##.....#..#.........#...##.....#..#.
##.#...#.#.#.#.#.#.........#..#...#.##...
.#.....#......##..#.#..#....#....#####...
........#...##...#.....#.......#....#.#.#
#......#..#..#.#.#....##..#......###.....
............#..#.#.#....#.....##..#......
...#.#.....#..#.......#..#.#............#
.#.#.....#..##.....#..#..............#...
.#.#....##.....#......##..#...#......#...
.......#..........#.###....#.#...##.#....
.....##.#..#.....#.#.#......#...##..#.#..
.#....#...#.#.#.......##.#.........#.#...
##.........#............#.#......#....#..
.#......#.............#.#......#.........
.......#...##........#...##......#....#..
#..#.....#.#...##.#.#......##...#.#..#...
#....##...#.#........#..........##.......
..#.#.....#.....###.#..#.........#......#
......##.#...#.#..#..#.##..............#.
.......##.#..#.#.............#..#.#......
...#....##.##..#..#..#.....#...##.#......
#....#..#.#....#...###...#.#.......#.....
.#..#...#......##.#..#..#........#....#..
..#.##.#...#......###.....#.#........##..
#.##.###.........#...##.....#..#....#.#..
..........#...#..##..#..##....#.........#
..#..#....###..........##..#...#...#..#.."""

    #     my_input = """.#..##.###...#######
    # ##.############..##.
    # .#.######.########.#
    # .###.#######.####.#.
    # #####.##.#.##.###.##
    # ..#####..#.#########
    # ####################
    # #.####....###.#.#.##
    # ##.#################
    # #####.##.###..####..
    # ..######..##.#######
    # ####.##.####...##..#
    # .#####..#.######.###
    # ##...#.##########...
    # #.##########.#######
    # .####.#.###.###.#.##
    # ....##.##.###..#####
    # .#.#.###########.###
    # #.#.#.#####.####.###
    # ###.##.####.##.#..##"""

    points: set = asteroids(my_input)
    temp = points.copy()
    # print(points)
    points_map = {}
    origin = (28, 29)
    # origin = (11, 13)
    x0, y0 = origin
    temp.discard(origin)
    while temp:
        point = temp.pop()
        x, y = point
        alined_points, left, right = aligned_asteroids(origin, point, temp)
        temp = temp - alined_points
        point_to_origin_right = (1, x - x0, y0 - y)
        point_to_origin_left = (0, x - x0, y0 - y)
        if right:
            points_map[point_to_origin_right] = right
        if left:
            points_map[point_to_origin_left] = left

    # pp = pprint.PrettyPrinter(indent=4)
    # pprint.pprint(points_map)
    print(len(points_map))

    weights: dict = {}
    for entry in points_map:
        weights[entry] = len(points_map.get(entry))

    # pprint.pprint(weights)

    points_list = [key for key in weights.keys()]
    sortedlist = sorted(
        points_list, key=lambda element: tan_value(element[1:]), reverse=True
    )
    r_sortedlist = sorted(sortedlist, key=itemgetter(0), reverse=True)
    # print(sortedlist)
    # print(r_sortedlist)

    loop_counter = 0
    del_counter = 0
    solution_line: tuple
    length = len(r_sortedlist)
    while del_counter < 200:
        solution_line = r_sortedlist[loop_counter % length]
        temp_weight = weights.get(solution_line)
        loop_counter += 1
        if temp_weight == 0:
            continue
            # maybe remove from weights dict also
        else:
            weights[solution_line] = temp_weight - 1
            del_counter += 1

    right_or_left, x, y = solution_line
    possible_solution = list(points_map[solution_line])
    if right_or_left == 1:
        possible_solution.sort(key=itemgetter(0))
    else:
        possible_solution.sort(key=itemgetter(0), reverse=True)
    loops = loop_counter // length
    print(possible_solution)
    print(loops)
    solution = possible_solution[loops]
    print("solution = ", solution)
    x, y = solution
    puzzle_solution = (x * 100) + y
    print("puzzle solution = ", puzzle_solution)

# devide points from same line to right and left,
# solution: add 0 or 1 to the keys of the map
