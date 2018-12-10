#! python3

import part1


def parse_claims(data):
    claims_data = {}
    for line in data:
        split = line.split()
        ID = int(split[0][1:])
        coords = split[2].split(',')
        x_size, y_size = list(map(int, split[3].split('x')))
        x_pos, y_pos = int(coords[0]), int(coords[1][:-1])
        claims_data[ID] =  parse_coordinates(x_size, y_size, x_pos, y_pos)
    return claims_data

def parse_coordinates(x_size, y_size, x_pos, y_pos):
    coordinate_set = []
    for y in range(y_size):
        for x in range(x_size):
            coordinate_set.append((x + x_pos, y + y_pos))
    return coordinate_set

def populate_grid(claims_data):
    for claim in claims_data.keys():
        for coordinates in claims_data[claim]:
            grid[coordinates[1]][coordinates[0]].append(claim)

def check_claims(claims_data):
    for k in claims_data.keys():
        overlapped = False
        for coordinates in claims_data[k]:
            if len(grid[coordinates[1]][coordinates[0]]) > 1:
                overlapped=True
                break
        if overlapped == False: return k

if __name__ == '__main__':
    data = part1.load_input()
    grid = [[[] for _ in range(1000)] for _ in range(1000)]
    claims_data = parse_claims(data)
    populate_grid(claims_data)
    
    print(check_claims(claims_data))

