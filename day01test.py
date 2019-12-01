from day01 import (
    fuel_requirement,
    full_fuel_requirement,
    part1,
    part2
)
import unittest


class FuelRequirementTest(unittest.TestCase):

    def testFuelNotRounding(self):
        self.assertEqual(2, fuel_requirement(12))

    def testFuelRounding(self):
        self.assertEqual(2, fuel_requirement(14))
    
    def testFuel(self):
        for mass, fuel in ((1969, 654), (100756, 33583)):
            self.assertEqual(fuel, fuel_requirement(mass))


class FullFuelRequirementTest(unittest.TestCase):

    def testFullFuel(self):
        for mass, fuel in ((14, 2), (1969, 966), (100756, 50346)):
            self.assertEqual(fuel, full_fuel_requirement(mass))


class Day01Test(unittest.TestCase):

    def testPart1(self):
        answer = 3317659
        self.assertEqual(answer, part1())

    def testPart2(self):
        answer = 4973616
        self.assertEqual(answer, part2())


if __name__ == '__main__':
    unittest.main()