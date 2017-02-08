import random
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

def has_ship(data, coord, b = False):
    """
    (list, tuple) -> (bool)

    check is in these coordinates ship
    >>> has_ship(read_field('field.txt'), ('G', 4))
    True
    """
    #print(coord)
    #print(ord(coord[0]) - ord('A'))
    if b:
        if data[coord[0]][coord[1]] == ' ':
            return False
        else:
            return True
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

def generate_field():
    """
    () -> list
    """
    lmass = [4,3,3,2,2,2,1,1,1,1]
    table = []
    massx = {}
    for i in range(10):
        table.append([' ']*10)
        # y : suitable Xes
        massx[i] = list(range(10))
    for sizes in lmass:



        '''
        b = False

        while not b:
            if y > 0 and (x - 1 not in massx[y-1] or x + 1 not in massx[y-1]):
                b = False
            else:
                b = True
            if y < 9 and (x -1 not in massx[y +1] or x + 1 not in massx[y +1])
                b = False
            y = random.randint(0, 9)

            x = random.choice(massx[y])
        '''
        # check which direction the ship can be
        direction = []
        while direction == []:
            y = random.randint(0, 9)

            x = random.choice(massx[y])
            b = True
            if x + 1 in massx[y] :
                for i in range(sizes):
                    if x + i  not in massx[y] and b:
                        b = False

                if b:
                    direction.append(1)

            b = True
            if x - 1 in massx[y] :
                for i in range(sizes):
                    if x - i  not in massx[y] and b:
                        b = False
                if b:
                    direction.append(2)
            b = True
            if y + sizes - 1 < 10 and x in massx[y+1]:
                for i in range(sizes):
                    if x not in massx[y  + i] and b:
                        b = False
                if b:
                    direction.append(3)
            b = True
            if y - sizes + 1 > -1 and x in massx[y -1]:
                for i in range(sizes):
                    if x not in massx[y  - i] and b:
                        b = False
                if b:
                    direction.append(4)

        direct = random.choice(direction)
        if direct == 1:
            for i in range(sizes):
                table[y][x+i] = '*'
                massx[y].remove(x+i)
                if y > 0 and x + i in table[y-1]:
                    table[y-1][x+i] = 'n'
                    massx[y -1].remove(x + i)
                if y < 9 and x + i in table[y + 1]:
                    table[y+1][x+i] = 'n'
                    massx[y + 1].remove(x + i)
            if x > 0:
                if y > 0 and x - 1 in table[y - 1]:
                    table[y-1][x-1] = 'n'
                    massx[y-1].remove(x-1)
                if x -1 in table[y]:
                    table[y][x-1] = 'n'
                    massx[y].remove(x -1)
                if y < 9 and x - 1 in table[y + 1]:
                    table[y + 1][x-1] = 'n'
                    massx[y+1].remove(x-1)
            if x + sizes -1 < 9:
                c = x + sizes
                if y > 0 and c in table[y-1]:
                    table[y-1][c] = 'n'
                    massx[y-1].remove(c)
                if c in table[y]:
                    table[y][c] = 'n'
                    massx[y].remove(c)
                if y < 9 and c in table[y + 1]:
                    table[y+1][c] = 'n'
                    massx[y+1].remove(c)
        elif direct == 2:
            for i in range(sizes):
                table[y][x-i] = '*'
                massx[y].remove(x-i)
                if y > 0 and x - i in table[y-1]:
                    table[y-1][x-i] = 'n'
                    massx[y -1].remove(x - i)
                if y < 9 and x - i in table[y + 1]:
                    table[y+1][x-i] = 'n'
                    massx[y + 1].remove(x - i)

            if x < 9:
                if y > 0 and x + 1 in table[y - 1]:
                    table[y-1][x+1] = 'n'
                    massx[y-1].remove(x+1)
                if x +1 in table[y]:
                    table[y][x+1] = 'n'
                    massx[y].remove(x +1)
                if y < 9 and x + 1 in table[y + 1]:
                    table[y + 1][x+1] = 'n'
                    massx[y+1].remove(x+1)

            if x - sizes + 1 > 0:
                c = x - sizes
                if y > 0 and c in table[y-1]:
                    table[y-1][c] = 'n'
                    massx[y-1].remove(c)
                if c in table[y]:
                    table[y][c] = 'n'
                    massx[y].remove(c)
                if y < 9 and c in table[y + 1]:
                    table[y+1][c] = 'n'
                    massx[y+1].remove(c)

        elif direct == 3:
            for i in range(sizes):
                table[y+i][x] = '*'
                massx[y+i].remove(x)
                if x>0 and x-1 in table[y+i]:
                    table[y+i][x-1] = 'n'
                    massx[y + i].remove(x -1)
                if x < 9 and x + 1 in table[y + i]:
                    table[y+i][x+1] = 'n'
                    massx[y + i].remove(x + 1)

            if y > 0:
                if x > 0 and  x - 1 in table[y - 1]:
                    table[y-1][x-1] = 'n'
                    massx[y-1].remove(x-1)
                if x  in table[y -1]:
                    table[y-1][x] = 'n'
                    massx[y-1].remove(x )
                if x < 9 and x +1  in table[y - 1]:
                    table[y - 1][x+1] = 'n'
                    massx[y-1].remove(x+1)

            if y + sizes -1 < 9:
                c = y + sizes
                if x > 0 and x-1 in table[c]:
                    table[c][x-1] = 'n'
                    massx[c].remove(x-1)
                if x in table[c]:
                    table[c][x] = 'n'
                    massx[c].remove(x)
                if x < 9 and x + 1 in table[c]:
                    table[c][x+1] = 'n'
                    massx[c].remove(x+1)

        else:
            for i in range(sizes):
                table[y-i][x] = '*'
                massx[y-i].remove(x)
                if x>0 and x-1 in table[y-i]:
                    table[y-i][x-1] = 'n'
                    massx[y - i].remove(x -1)
                if x < 9 and x + 1 in table[y - i]:
                    table[y-i][x+1] = 'n'
                    massx[y - i].remove(x + 1)

            if y <  9:
                if x > 0 and  x - 1 in table[y + 1]:
                    table[y+1][x-1] = 'n'
                    massx[y+1].remove(x-1)
                if x  in table[y +1]:
                    table[y+1][x] = 'n'
                    massx[y+1].remove(x )
                if x < 9 and x +1  in table[y + 1]:
                    table[y + 1][x+1] = 'n'
                    massx[y+1].remove(x+1)

            if y - sizes +1 > 0:
                c = y - sizes
                if x > 0 and x-1 in table[c]:
                    table[c][x-1] = 'n'
                    massx[c].remove(x-1)
                if x in table[c]:
                    table[c][x] = 'n'
                    massx[c].remove(x)
                if x < 9 and x + 1 in table[c]:
                    table[c][x+1] = 'n'
                    massx[c].remove(x+1)



    gfResult = []
    for iy in range(10):
        line = ''
        for ix in range(10):
            if table[iy][ix] == 'n':
                table[iy][ix] = ' '
            line += table[iy][ix]
        gfResult.append(line)
    print(gfResult)
    return field_to_str(gfResult)









print(generate_field())