def read_field(file):
    """
    (str) -> (data)

    read field from input file
    >>> read_field('field.txt')
    ['   **     ', '          ', '    ***  *', ' **      *', '    ***   ', '        * ', ' ****   * ', '          ',\
    '   *      ', ' *    *  *']
    """
    with open(file, 'r') as f:
        cont = f.readlines()
        cont = [x.split('\n')[0] for x in cont]
        #print(cont)
        return cont

def has_ship(data, coord):
    """
    (list, tuple) -> (bool)

    check is in these coordinates ship
    >>> has_ship(read_field('field.txt'), ('G', 4))
    True
    """
    #print(coord)
    #print(ord(coord[0]) - ord('A'))
    if data[ord(coord[0]) - ord('A')][coord[1]-1] == '*' or data[ord(coord[0]) - ord('A')][coord[1]-1] == 'X':
        return True
    elif data[ord(coord[0]) - ord('A')][coord[1]-1] == ' ':
        return False


def ship_size(dat: object, coor: object) -> object:
    """
    (list, tuple) -> int

    check which size is ship with these coordinates
    >>> ship_size(read_field('field.txt'), ('G', 4))
    4
    """
    if has_ship(dat, coor):
        ssResult = 1
        sscoor = (ord(coor[0]) - ord('A'), coor[1]-1)
        i = 1
        #print(sscoor)
        if (sscoor[0] > 0 and (dat[sscoor[0]-1][sscoor[1]] == '*' or dat[sscoor[0]-1][sscoor[1]] == 'X')) or \
                ( sscoor[0] < 9 and (dat[sscoor[0]+1][sscoor[1]] == '*' or dat[sscoor[0]+1][sscoor[1]] == 'X')):


            while sscoor[0] - i > -1 and ( dat[sscoor[0]-i][sscoor[1]] == '*' or dat[sscoor[0]-i][sscoor[1]] == 'X'):
                ssResult += 1
                i += 1
            i = 1
            while sscoor[0] + i < 10  and ( dat[sscoor[0]+i][sscoor[1]] == '*' or  dat[sscoor[0]+i][sscoor[1]] == 'X'):
                ssResult += 1
                i += 1
        else:
            while sscoor[1] - i > -1 and  (dat[sscoor[0]][sscoor[1]-i] == '*' or dat[sscoor[0]][sscoor[1]-i] == 'X'):
                ssResult += 1
                i += 1
            i = 1
            while sscoor[1] + i < 10  and  (dat[sscoor[0]][sscoor[1]+i] == '*' or dat[sscoor[0]][sscoor[1]+i] == 'X'):
                ssResult += 1
                i += 1
        return ssResult
    else:
        return 0

def is_valid(dataiv):
    """
    (list) -> (str)

    check is field valid
    >>> is_valid(read_field('field.txt'))
    True
    """
    if len(dataiv) == 10 :
        for el in dataiv:
            if len(dataiv) != 10:
                return False
        mass = {4: 0, 3: 0, 2: 0, 1: 0}
        for let in 'ABCDEFGHIJ':
            for num in range(1, 11):
                len_ship = ship_size(dataiv, (let, num))
                if len_ship:
                    if len_ship> 4:
                        return False
                    else:
                        mass[len_ship] += 1
                        coordiv = (ord(let) - ord('A'), num-1)
                        #print(coordiv)
                        if coordiv[0] > 0 and coordiv[1] > 0 and has_ship(dataiv, (chr(ord(let)-1), num - 1)):
                            return False
                        if coordiv[0] > 0 and coordiv[1] < 9 and has_ship(dataiv, (chr(ord(let)-1), num + 1)):
                            return False
                        if coordiv[0] < 9 and coordiv[1] > 0 and has_ship(dataiv, (chr(ord(let)+1), num - 1)):
                            return False
                        if coordiv[0] < 9 and coordiv[1] < 9 and has_ship(dataiv, (chr(ord(let)+1), num + 1)):
                            return False

        if mass[4] != 4 or mass[3] != 6 or mass[2] != 8 or mass[1] != 4:
            return False
        return True
    else:
        return False

#print(is_valid(read_field('field.txt')))
#print(read_field('field.txt'))

def field_to_str(tem):
    r"""
    (list) -> str

    convert data to string, that can show.
    """
    line = [x + '\n' for x in tem]
    ftsResult = ''
    for el in line:
        ftsResult += el
    return ftsResult
#print(field_to_str(read_field('field.txt')))
