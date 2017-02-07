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
        if (sscoor[0] > 0 and dat[sscoor[0]-1][sscoor[1]] == '*' or dat[sscoor[0]-1][sscoor[1]] == 'X') or \
                ( sscoor[0] < 9 and dat[sscoor[0]+1][sscoor[1]] == '*' or dat[sscoor[0]+1][sscoor[1]] == 'X'):


            while sscoor[0] - i > -1 and  dat[sscoor[0]-i][sscoor[1]] == '*' or dat[sscoor[0]-i][sscoor[1]] == 'X':
                ssResult += 1
                i += 1
            while sscoor[0] + i < 10  and  dat[sscoor[0]+i][sscoor[1]] == '*' or  dat[sscoor[0]+i][sscoor[1]] == 'X':
                ssResult += 1
                i += 1
        else:
            while sscoor[1] - i > -1 and  dat[sscoor[0]][sscoor[1]-i] == '*' or dat[sscoor[0]][sscoor[1]-i] == 'X':
                ssResult += 1
                i += 1
            while sscoor[1] + i < 10  and  dat[sscoor[0]][sscoor[1]+i] == '*' or dat[sscoor[0]][sscoor[1]+i] == 'X':
                ssResult += 1
                i += 1
        return ssResult
    else:
        return 0

def is_valid(dataiv):
    '''
    (list) -> (str)
    :return:
    '''
    if len(dataiv) == 10 :
        for el in dataiv:
            if len(dataiv) != 10:
                return False

    else:
        return False
print(ship_size(read_field('field.txt'), ('C', 10)))