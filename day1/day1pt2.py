#! python3

def load_input(path):
    f = open(path, 'r')
    deltas = []
    for line in f.readlines():
        deltas.append(int(line))
    return(deltas)

def first_repeated(deltas):
    current_frequency = 0
    past_frequencies = []
    loop = True
    count = 1
    while loop:
        for delta in deltas:
            past_frequencies.append(current_frequency)
            current_frequency += delta
            if current_frequency in past_frequencies:
                print(current_frequency)
                loop=False
                break
        count+=1
        print(count)
    
