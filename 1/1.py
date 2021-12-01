#!/usr/bin/env python

with open('input.txt') as f:
    input = [int(line.strip()) for line in f.readlines()]

print(len([v for i, v in enumerate(input[1:], start=1) if v > input[i-1]]))

print(len([i for i in range(1, len(input)-2) if sum(input[i:i+3]) > sum(input[i-1:i+2])]))
