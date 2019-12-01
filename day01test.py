from day01 import fuel_requirement, full_fuel_requirement
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


if __name__ == '__main__':
    unittest.main()