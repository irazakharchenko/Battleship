import random


class Ship:
    '''
    Represent ships coordinates and are they hit.
    '''

    def __init__(self, bow: object = (0, 0), horizontal: object = True, length: object = -1, hit: object = False) \
            -> object:
        '''
        Initialize direction of ship, its left up coordinate, its length and is it hit.
        :param bow: tuple
        :param horizontal: boolean
        :param length: int
        :param hit: boolean
        '''
        self.assignmentblhh(bow, length, horizontal, hit)

    def assignmentblhh(self, b, l, ho, hi):
        '''
        initialize self variables
        :param b: tuple (bow)
        :param l: int (length)
        :param ho: boolean (horizontal)
        :param hi: boolean (hit)
        :return:
        '''
        assert isinstance(b, object)
        self.bow = b
        assert isinstance(l, object)
        self.__length = l
        assert isinstance(ho, object)
        self.horizontal = ho
        assert isinstance(hi, object)
        self.__hit = hi

        def shoot_at_s(self):
            if not self.__hit:

                self.__hit = True

class Field():
    '''
    Generete field
    '''

    def __init__(self, coor = (0,0)):
        '''
        coor - tuple(int(0..9),int(0..9))
        '''
        #super().__init__()
        self.assig(coor)


    def assig(self, coora = (0,0)):
        self.field = []
        self.__ships = []
        for i in range(10):
            self.__ships.append(10*[None])
        self.coor = coora

    def generate_field(self):
        """
        Randomly put ships on field
        """
        lmass = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        table = []
        massx = {}
        for i in range(10):
            table.append([' '] * 10)
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
                while massx[y] == []:
                    y = random.randint(0, 9)
                x = random.choice(massx[y])
                b = True
                if x + 1 in massx[y]:
                    for i in range(sizes):
                        if x + i + 1 not in massx[y] and b:
                            b = False

                    if b:
                        direction.append(1)

                b = True
                if x - 1 in massx[y]:
                    for i in range(sizes):
                        if x - i - 1 not in massx[y] and b:
                            b = False
                    if b:
                        direction.append(2)
                b = True
                if y + sizes - 1 < 9 and x in massx[y + 1]:
                    for i in range(sizes):
                        if x not in massx[y + i] and b:
                            b = False
                    if b:
                        direction.append(3)
                b = True
                if y - sizes + 1 > 0 and x in massx[y - 1]:
                    for i in range(sizes):
                        if x not in massx[y - i] and b:
                            b = False
                    if b:
                        direction.append(4)

            direct = random.choice(direction)
            # print(direct)
            if direct == 1:
                for i in range(sizes):
                    # print('y = ', y, ' x= ', x, ' i=', i)
                    # print(massx)
                    table[y][x + i] = '*'
                    self.__ships[y][x+i] = Ship((y, x), True, sizes)
                    massx[y].remove(x + i)
                    # print(x+i, 'table', table[y-1])
                    if y > 0 and x + i in massx[y - 1]:
                        table[y - 1][x + i] = 'n'
                        massx[y - 1].remove(x + i)
                    if y < 9 and x + i in massx[y + 1]:
                        table[y + 1][x + i] = 'n'
                        massx[y + 1].remove(x + i)
                if x > 0:
                    if y > 0 and x - 1 in massx[y - 1]:
                        table[y - 1][x - 1] = 'n'
                        massx[y - 1].remove(x - 1)
                    if x - 1 in massx[y]:
                        table[y][x - 1] = 'n'
                        massx[y].remove(x - 1)
                    if y < 9 and x - 1 in massx[y + 1]:
                        table[y + 1][x - 1] = 'n'
                        massx[y + 1].remove(x - 1)
                if x + sizes - 1 < 9:
                    c = x + sizes
                    if y > 0 and c in massx[y - 1]:
                        table[y - 1][c] = 'n'
                        massx[y - 1].remove(c)
                    if c in massx[y]:
                        table[y][c] = 'n'
                        massx[y].remove(c)
                    if y < 9 and c in massx[y + 1]:
                        table[y + 1][c] = 'n'
                        massx[y + 1].remove(c)
            elif direct == 2:
                for i in range(sizes):
                    # print('y = ', y, ' x= ', x, ' i=', i)
                    # print(massx)
                    table[y][x - i] = '*'
                    self.__ships[y][x - i] = Ship((y, x - sizes), True, sizes)
                    massx[y].remove(x - i)
                    if y > 0 and x - i in massx[y - 1]:
                        table[y - 1][x - i] = 'n'
                        massx[y - 1].remove(x - i)
                    if y < 9 and x - i in massx[y + 1]:
                        table[y + 1][x - i] = 'n'
                        massx[y + 1].remove(x - i)

                if x < 9:
                    if y > 0 and x + 1 in massx[y - 1]:
                        table[y - 1][x + 1] = 'n'
                        massx[y - 1].remove(x + 1)
                    if x + 1 in massx[y]:
                        table[y][x + 1] = 'n'
                        massx[y].remove(x + 1)
                    if y < 9 and x + 1 in massx[y + 1]:
                        table[y + 1][x + 1] = 'n'
                        massx[y + 1].remove(x + 1)

                if x - sizes + 1 > 0:
                    c = x - sizes
                    if y > 0 and c in massx[y - 1]:
                        table[y - 1][c] = 'n'
                        massx[y - 1].remove(c)
                    if c in massx[y]:
                        table[y][c] = 'n'
                        massx[y].remove(c)
                    if y < 9 and c in massx[y + 1]:
                        table[y + 1][c] = 'n'
                        massx[y + 1].remove(c)

            elif direct == 3:

                for i in range(sizes):
                    # print('y = ', y, ' x= ', x, ' i=', i)
                    # print(massx)
                    table[y + i][x] = '*'
                    self.__ships[y + i][x] = Ship((y, x), False, sizes)
                    massx[y + i].remove(x)
                    if x > 0 and x - 1 in massx[y + i]:
                        table[y + i][(x - 1)] = 'n'
                        massx[y + i].remove(x - 1)
                    if x < 9 and x + 1 in massx[y + i]:
                        table[y + i][x + 1] = 'n'
                        massx[y + i].remove(x + 1)

                if y > 0:
                    if x > 0 and x - 1 in massx[y - 1]:
                        table[y - 1][x - 1] = 'n'
                        massx[y - 1].remove(x - 1)
                    if x in massx[y - 1]:
                        table[y - 1][x] = 'n'
                        massx[y - 1].remove(x)
                    if x < 9 and x + 1 in massx[y - 1]:
                        table[y - 1][x + 1] = 'n'
                        massx[y - 1].remove(x + 1)

                if y + sizes - 1 < 9:
                    c = y + sizes
                    if x > 0 and x - 1 in massx[c]:
                        table[c][x - 1] = 'n'
                        massx[c].remove(x - 1)
                    if x in massx[c]:
                        table[c][x] = 'n'
                        massx[c].remove(x)
                    if x < 9 and x + 1 in massx[c]:
                        table[c][x + 1] = 'n'
                        massx[c].remove(x + 1)

            else:

                for i in range(sizes):
                    # print('y = ', y, ' x= ', x, ' i=', i)
                    # print(massx)
                    table[y - i][x] = '*'
                    self.__ships[y - i][x] = Ship((y - sizes, x), False, sizes)
                    massx[y - i].remove(x)
                    if x > 0 and x - 1 in massx[y - i]:
                        table[y - i][x - 1] = 'n'
                        massx[y - i].remove(x - 1)
                    if x < 9 and x + 1 in massx[y - i]:
                        table[y - i][x + 1] = 'n'
                        massx[y - i].remove(x + 1)

                if y < 9:
                    if x > 0 and x - 1 in massx[y + 1]:
                        table[y + 1][x - 1] = 'n'
                        massx[y + 1].remove(x - 1)
                    if x in massx[y + 1]:
                        table[y + 1][x] = 'n'
                        massx[y + 1].remove(x)
                    if x < 9 and x + 1 in massx[y + 1]:
                        table[y + 1][x + 1] = 'n'
                        massx[y + 1].remove(x + 1)

                if y - sizes + 1 > 0:
                    c = y - sizes
                    if x > 0 and x - 1 in massx[c]:
                        table[c][x - 1] = 'n'
                        massx[c].remove(x - 1)
                    if x in massx[c]:
                        table[c][x] = 'n'
                        massx[c].remove(x)
                    if x < 9 and x + 1 in massx[c]:
                        table[c][x + 1] = 'n'
                        massx[c].remove(x + 1)
                        # for lines in table:
                        # print(lines, '\n')
                        # print('\n')
            self.coor = (y,x)
        '''
        gfResult = []
        for iy in range(10):
            line = ''
            for ix in range(10):
                if table[iy][ix] == 'n':
                    table[iy][ix] = ' '
                line += table[iy][ix]
            gfResult.append(line)
        print(gfResult)
        '''
        for iy in range(10):
            line = ''
            for ix in range(10):
                if table[iy][ix] == 'n':
                    table[iy][ix] = ' '
        self.field = table
        print('self.__ships = ', self.__ships)
        print('self.coor = ', self.coor)

    def shoot_at(self):
        #print('self.field = ', self.field)
        if self.__ships[self.coor[0]][self.coor[1]] != None:
            print('self.__ships[self.coor[0]][self.coor[1]] = ', self.__ships[self.coor[0]][self.coor[1]])
            self.field[self.coor[0]][self.coor[1]] = 'X'
            self.__ships[self.coor[0]][self.coor[1]].__hit = True
            print('yey')
            print(self.__ships[self.coor[0]][self.coor[1]])
            print('self.field = ', self.field)





n = Field()
n.generate_field()


n.shoot_at()

