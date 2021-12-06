#!/usr/bin/env python

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

sums = [0,0,0,0,0,0,0,0,0,0,0,0]
for binary in lines:
    for i in range(12):
        sums[i] += int(binary[i])

half = len(lines) // 2

gamma = ['1' if digit > half else '0' for digit in sums]
epsilon = ['1' if digit == '0' else '0' for digit in gamma]

print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))

# part 2

def most_common(numbers, position):
    initial = {'0': 0, '1': 0}
    for number in numbers:
        initial[number[position]] += 1
    if initial['0'] == initial['1']:
        return '1'
    most = max(initial, key=initial.get)
    return most


def least_common(numbers, position):
    return {'1': '0', '0': '1'}[most_common(numbers, position)]


def recurse_to_answer(numbers, position, sort_func):
    if len(numbers) == 1:
        return numbers[0]

    criteria = sort_func(numbers, position)
    filtered = list(filter(lambda x: x[position] == criteria, numbers))
    return recurse_to_answer(filtered, position + 1, sort_func)


oxygen = recurse_to_answer(lines, 0, most_common)
co2 = recurse_to_answer(lines, 0, least_common)


print(int(''.join(oxygen), 2) * int(''.join(co2), 2))


