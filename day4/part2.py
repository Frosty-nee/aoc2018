#! python3

from part1 import load_input, parse_input

def most_asleep_on_same_minute(guards):
    guard_id = None
    guard_minute_count = 0
    guard_sleepiest_minute = 0
    for guard in guards:
        minute, sleep_count = sleepiest_minute(guards[guard])
        if sleep_count > guard_minute_count:
            guard_minute_count = sleep_count
            guard_id = guard
            guard_sleepiest_minute = minute

    return guard_id, guard_sleepiest_minute


def sleepiest_minute(guard):
    count = [0]*60
    for shift in guard.keys():
        for minute in range(len(count)):
            if guard[shift][minute]: 
                count[minute] += 1
    return count.index(max(count)), count[count.index(max(count))]

if __name__ == '__main__':
    guards = parse_input(load_input())
    guard_id, minute = most_asleep_on_same_minute(guards)
    print(guard_id * minute)
