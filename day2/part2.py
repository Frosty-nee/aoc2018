#! python3

import part1

if __name__=='__main__':
    data = part1.load_input('day_2_input')
    
    testword_list = []

    #for entry in data
    for entry in range(len(data)):
        #loop through every iteration of it
        #put them in a dict
        testwords = []
        for x in range(len(data[entry])):
            testwords.append(data[entry][:x]+data[entry][x+1:])
        testword_list.append(testwords) 


    for lst in range(len(testword_list)):
        for word in testword_list[lst]:
            for ex in range(lst+1, len(testword_list)):
                if word in testword_list[ex]:
                    print(word)
