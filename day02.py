import operator


class IntcodeInterpreter:

    OPERATIONS = {
        1: operator.add,
        2: operator.mul
    }

    def run(self, program):
        self.memory = program
        pointer = 0
        while True:
            # fetch next instruction
            opcode, *params = self.memory[pointer:pointer+4]
            # halt
            if opcode == 99:
                break
            # execute current instruction
            self.execute(opcode, *params)
            # move pointer to the next instruction
            pointer += 4

    def execute(self, opcode, i=0, j=0, k=0):
        a = self.memory[i]
        b = self.memory[j]
        self.memory[k] = IntcodeInterpreter.OPERATIONS[opcode](a, b)


def part1():
    with open('res/day02.txt') as data:
        program = [int(datum) for datum in data.read().split(',')]
    
    program[1] = 12
    program[2] = 2
    
    interpreter = IntcodeInterpreter()
    interpreter.run(program)
    return interpreter.memory[0]

def part2():
    with open('res/day02.txt') as data:
        program = [int(datum) for datum in data.read().split(',')]
    
    interpreter = IntcodeInterpreter()
    for noun in range(0, 100):
        for verb in range(0, 100):
            probe = program[:]
            probe[1] = noun
            probe[2] = verb
            interpreter.run(probe)
            if interpreter.memory[0] == 19690720:
                return 100 * noun + verb


if __name__ == '__main__':
    print(part1())
    print(part2())