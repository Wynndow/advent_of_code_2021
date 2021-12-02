#!/usr/bin/env python


with open('input.txt') as f:
    commands = [(line.split()[0][0], int(line.split()[1])) for line in f.readlines()]

aggregation = {'f': 0, 'd': 0, 'u': 0}
for command, distance in commands:
        aggregation[command] += distance

print(aggregation['f'] * (aggregation['d'] - aggregation ['u']))


# part2

horizontal = depth = aim = 0

for c, x in commands:
    if c == 'd':
        aim += x
    if c == 'u':
        aim -= x
    if c == 'f':
        horizontal += x
        depth += aim * x

print(horizontal * depth)


