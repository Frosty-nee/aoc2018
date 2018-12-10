#! python3

def load_input():
    f = open('day_3_input', 'r')
    raw = f.readlines()
    output = []
    for line in raw:
        output.append(line.strip())
    return output

def get_coordinates(claims):
    claim_coordinates = []
    for claim in claims:
        data = parse_claim(claim)
        for y in range(data[1]):
            for x in range(data[0]):
                coords = ({'x':x+data[2], 'y':y+data[3]})
                claim_coordinates.append(coords)
    return claim_coordinates

def parse_claim(claim):
    split = claim.split()
    ID = split[0][1:]
    coords = split[2].split(',')
    x_pos, y_pos = int(coords[0]), int(coords[1][:-1])
    x_size, y_size = list(map(int,split[3].split('x')))
    return([x_size, y_size, x_pos, y_pos])

if __name__ == '__main__':
    grid = [[0]*1000 for _ in range(1000)]

    coordinates = get_coordinates(load_input())
    for cell in coordinates:
        grid[cell['y']][cell['x']] += 1
    
    count = 0
    for row in grid:
        for cell in row:
            if cell > 1:
                count+=1

    print(count)
