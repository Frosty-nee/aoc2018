#! python3
import string

def load_input(path):
    f = open(path,'r')
    raw_lines = f.readlines()
    output = []
    for line in raw_lines:
        output.append(line.strip())
    return(output)

def count_letters(ids):
    letter_counts = {}
    for box in ids:
        output={}
        for c in string.ascii_lowercase:
            output[c] = box.count(c)
        letter_counts[box] = output
    return letter_counts

def count_multiples(data):
    doubles = 0
    triples = 0
    for entry in data.values():
        twos = False
        threes = False
        for k,v in entry.items():
            if v == 2 and twos == False:
                twos = True
                doubles +=1

            if v == 3 and threes == False:
                triples += 1
                threes = True
                
            
    print(doubles, triples)
if __name__ == '__main__':
    raw_data = load_input('day_2_input')

    data = count_letters(raw_data)
    count_multiples(data)
