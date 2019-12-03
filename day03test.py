from day03 import (
    calculate_path,
    min_distance
)
import unittest


class CrossedWiresTest(unittest.TestCase):

    def testExample(self):
        wire1 = 'R8,U5,L5,D3'
        wire2 = 'U7,R6,D4,L4'
        wire1_points = calculate_path(wire1)
        wire2_points = calculate_path(wire2)
        intersections = wire1_points.intersection(wire2_points)
        self.assertEqual(6, min_distance((0, 0), *intersections))

    def testAnotherExample(self):
        wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
        wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
        wire1_points = calculate_path(wire1)
        wire2_points = calculate_path(wire2)
        intersections = wire1_points.intersection(wire2_points)
        self.assertEqual(159, min_distance((0, 0), *intersections))

    def testYetAnotherExample(self):
        wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
        wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
        wire1_points = calculate_path(wire1)
        wire2_points = calculate_path(wire2)
        intersections = wire1_points.intersection(wire2_points)
        self.assertEqual(135, min_distance((0, 0), *intersections))
    

if __name__ == '__main__':
    unittest.main()