import math

def fuel_requirement(mass):
    return math.floor(mass / 3) - 2

def full_fuel_requirement(mass):
    total_fuel = 0
    fuel = fuel_requirement(mass)
    while fuel > 0:
        total_fuel += fuel
        fuel = fuel_requirement(fuel)
    return total_fuel

def first_part():
    with open('res/day01.txt') as data:
        return sum(fuel_requirement(int(datum)) for datum in data)

def second_part():
    with open('res/day01.txt') as data:
        return sum(full_fuel_requirement(int(datum)) for datum in data)

if __name__ == '__main__':
    print(first_part())
    print(second_part())