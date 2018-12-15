#! python3
import sys
import string
import time
from part1 import react_polymer, switch_case, compare_letters, load_input

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


def remove_letter(letter, polymer):
    
    out = list(polymer)
    try:
        while True:
            out.remove(letter)
    except ValueError:
        pass
    try: 
        while True:
            out.remove(switch_case(letter))
    except ValueError:
        pass
    return out

if __name__ == '__main__':
    polymer = load_input('day_5_input')
    results = {}
    for letter in string.ascii_lowercase:
        results[len(react_polymer(remove_letter(letter, polymer)))] = letter
    print(results[min(results.keys())], min(results.keys()))
