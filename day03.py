def parse_path(pathspec):
    return [(segment[0], int(segment[1:])) for segment in pathspec.split(',')]

def calculate_path(pathspec):
    path = parse_path(pathspec)
    points = set()
    current_point = (0, 0)
    for direction, count in path:
        if direction == 'U':
            start = current_point[1] + 1
            segment = [(current_point[0], i) for i in range(start, start + count)]
        elif direction == 'R':
            start = current_point[0] + 1
            segment = [(i, current_point[1]) for i in range(start, start + count)]
        elif direction == 'L':
            start = current_point[0] - 1
            segment = [(i, current_point[1]) for i in range(start, start - count, -1)]
        elif direction == 'D':
            start = current_point[1] - 1
            segment = [(current_point[0], i) for i in range(start, start - count, -1)]
        points.update(segment)
        current_point = segment[-1]
    return points

def min_distance(point, *candidates):
    return min(abs(point[0] + c[0]) + abs(point[1] + c[1]) for c in candidates)

def part1():
    with open('res/day03.txt') as data:
        wire1, wire2 = data.readlines()
    wire1_points = calculate_path(wire1)
    wire2_points = calculate_path(wire2)
    intersections = wire1_points.intersection(wire2_points)
    return min_distance((0, 0), *intersections)


if __name__ == '__main__':
    print(part1())