#!/usr/bin/env python3
def the_sequence(length):
    sequence = [0, 1]
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def print_fibonacci(length):
    solution = the_sequence(length)
    if length == 0:
        print([])
    elif length == 1:
        print([solution[0]])
    else:
        print(solution)
    pass