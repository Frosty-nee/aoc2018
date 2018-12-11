#! python3

def load_input():
    f = open('day_4_input', 'r')
    data = []
    for line in f.readlines():
        data.append(line.strip())
    return data

def parse_input(data):
    shifts = []
    current_shift = []
    for line in data:
        if 'begins' in line:
            shifts.append(current_shift)
            current_shift = []
        current_shift.append(line)
    shifts = shifts[1:]
    guards = {}
    for shift in shifts:
        guard_id = int(shift[0].split()[3][1:])
        if guard_id not in guards:
            guards[guard_id] = {}
        sleep_wake_times = shift[1:]
        date = shift[0].split()[0][1:]
        #False == Awake
        sleep_chart = [False]*60
        prior_state_time = 0
        for entry in sleep_wake_times:
            awake = True
            minute = int(entry.split()[1][3:-1])
            if 'wakes' in entry:
                awake = True
            else:
                awake = False
            for mn in range(prior_state_time, minute):
                sleep_chart[mn] = awake
            prior_state_time = minute
        guards[guard_id][date] = sleep_chart
    return guards

def count_sleeping(guard):
    minuntes_slept = 0
    for shift in guards[guard]:
        minuntes_slept += guards[guard][shift].count(True)
    return minuntes_slept

def sleepiest(guards):
    most_slept = 0
    sleeper_id = None
    for guard in guards:
        minutes_slept = count_sleeping(guard)
        if minutes_slept > most_slept:
            sleeper_id = guard
            most_slept = minutes_slept
    return sleeper_id

def sleepiest_minute(guard):
    count = [0]*60
    for shift in guards[guard]:
        for minute in range(60):
            if guards[guard][shift][minute]: 
                count[minute] += 1
    return(count.index(max(count)))

if __name__ == '__main__':
   guards =  parse_input(load_input())
   sleepiest = sleepiest(guards)
   minute = sleepiest_minute(sleepiest)
   print(sleepiest * minute)
