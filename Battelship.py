def read_field(file):
    '''
    (str) -> (data)
    '''
    with open(file, 'r') as f:
        cont = f.readlines()
        cont = [x[:-1] for x in cont]
        print(cont)
        return cont

def has_ship(data, coord):
    '''
    (list, tuple) -> (bool)
    '''
    if data[ord(coord[0]) - ord('A')][coord[1]-1] == '*':
        return True
    elif data[ord(coord[0]) - ord('A')][coord[1]-1] == ' ':
        return False
    else:
        return 'hurt'

def ship_size(dat, coor):
    '''
    (list, tuple) -> int
    '''
    if has_ship(dat, coor):
        ssResult = 1
        sscoor = (ord(coor[0]) - ord('A'), coor[1]-1)
        i = 1
        if (sscoor[0] > 0 and dat[sscoor[0]-1][sscoor[1]] == '*') or( sscoor[0] < 9 and dat[sscoor[0]+1][sscoor[1]] == '*'):


            while sscoor[0] - i > -1 and  dat[sscoor[0]-i][sscoor[1]] == '*':
                ssResult += 1
                i += 1
            while sscoor[0] + i < 10  and  dat[sscoor[0]+i][sscoor[1]] == '*':
                ssResult += 1
                i += 1
        else:
            while sscoor[1] - i > -1 and  dat[sscoor[0]][sscoor[1]-i] == '*':
                ssResult += 1
                i += 1
            while sscoor[1] + i < 10  and  dat[sscoor[0]][sscoor[1]+i] == '*':
                ssResult += 1
                i += 1
        return ssResult
    else:
        return 0

print(ship_size(read_field('field.txt'), ('C', 10)))