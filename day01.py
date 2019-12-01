def fuel_requirement(mass):
    return mass // 3 - 2

def full_fuel_requirement(mass):
    total_fuel = 0
    fuel = fuel_requirement(mass)
    while fuel > 0:
        total_fuel += fuel
        fuel = fuel_requirement(fuel)
    return total_fuel

def part1():
    with open('res/day01.txt') as data:
        return sum(fuel_requirement(int(datum)) for datum in data)

def part2():
    with open('res/day01.txt') as data:
        return sum(full_fuel_requirement(int(datum)) for datum in data)

if __name__ == '__main__':
    print(part1())
    print(part2())