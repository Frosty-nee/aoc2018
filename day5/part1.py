#! python3
import sys
import string
import time

def load_input(filepath):
    with open(filepath, 'r') as f:
        return list(f.read().strip())

def compare_letters(l1, l2):
    if switch_case(l1) == l2:
        return True
    else: return False

def switch_case(l):
    if l in string.ascii_uppercase:
        return l.lower()
    else: return l.upper()

def react_polymer(polymer):
    previous_letter = ''
    output = []
    for letter in polymer:
        if letter == switch_case(previous_letter):
            output.pop()
        else: output.append(letter)
        if len(output) > 0: previous_letter = output[-1]
    return output


if __name__ == '__main__':
    polymer = load_input('day_5_input')
    start = time.time()
    polymer = react_polymer(polymer)
    print(time.time() - start, 's')
    print(len(polymer))
