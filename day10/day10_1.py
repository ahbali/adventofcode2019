def are_aligned(point1: tuple, point2: tuple, point3: tuple) -> bool:
    # y1 = a*x1 + b
    # y2 = a*x2 + b

    y1, x1 = point1
    y2, x2 = point2
    y3, x3 = point3
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


def aligned_asteroids(origin: tuple, tested: tuple, ast_map: set) -> tuple:
    result: set = set()
    result.add(tested)
    temp = ast_map.copy()
    temp.discard(origin)
    greater, lessthan = 0, 0
    y0, x0 = origin
    for point in temp:
        if are_aligned(origin, tested, point):
            result.add(point)
            y, x = point
            if x > x0:
                greater = 1
            elif x < x0:
                lessthan = 1
            else:
                if y > y0:
                    greater = 1
                elif y < y0:
                    lessthan = 1
    return (result, lessthan + greater)


def visible_asteroids_count(origin: tuple, ast_map: set) -> int:
    temp: set = ast_map.copy()
    temp.discard(origin)
    # y0, x0 = origin
    count = 0
    while temp:
        asteroid = temp.pop()
        # greater, lessthan = 0, 0
        alined, increment = aligned_asteroids(origin, asteroid, ast_map)
        # print(alined)
        # for node in alined:
        #     y, x = node
        #     if x > x0:
        #         greater = 1
        #     elif x < x0:
        #         lessthan = 1
        #     else:
        #         if y > y0:
        #             greater = 1
        #         elif y < y0:
        #             lessthan = 1
        temp = temp - alined
        count += increment
    return count


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
            y += 1
        x += 1
        y = 0
    return set(points)


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

    #     my_input = """.#....#####...#..
    # ##...##.#####..##
    # ##...#...#.#####.
    # ..#.....#...###..
    # ..#.#.....#....##"""

    points = asteroids(my_input)
    best_value = 0
    best_asteroid = ()
    for point in points:
        counter = visible_asteroids_count(point, points)
        if counter > best_value:
            best_value = counter
            best_asteroid = point

    print("best value", best_value, " for asteroid at ", best_asteroid)
