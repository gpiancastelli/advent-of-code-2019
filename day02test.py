from day02 import (
    IntcodeInterpreter,
    part1,
    part2
)
import unittest


class IntcodeProgramsTest(unittest.TestCase):

    def setUp(self):
        self.interpreter = IntcodeInterpreter()

    def testExampleProgram(self):
        program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        output = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        self.interpreter.run(program)
        self.assertEqual(output, self.interpreter.memory)

    def testSmallProgram1(self):
        program = [1, 0, 0, 0, 99]
        output = [2, 0, 0, 0, 99]
        self.interpreter.run(program)
        self.assertEqual(output, self.interpreter.memory)
    
    def testSmallProgram2(self):
        program = [2, 3, 0, 3, 99]
        output = [2, 3, 0, 6, 99]
        self.interpreter.run(program)
        self.assertEqual(output, self.interpreter.memory)
    
    def testSmallProgram3(self):
        program = [2, 4, 4, 5, 99, 0]
        output = [2, 4, 4, 5, 99, 9801]
        self.interpreter.run(program)
        self.assertEqual(output, self.interpreter.memory)

    def testSmallProgram4(self):
        program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        output = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.interpreter.run(program)
        self.assertEqual(output, self.interpreter.memory)


class Day02Test(unittest.TestCase):

    def testPart1(self):
        answer = 8017076
        self.assertEqual(answer, part1())

    def testPart2(self):
        answer = 3146
        self.assertEqual(answer, part2())


if __name__ == '__main__':
    unittest.main()