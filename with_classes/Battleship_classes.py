import random
from string import ascii_lowercase, ascii_uppercase
from os import system
from time import sleep
class Ship:
    '''
    Represent ships coordinates and are they hit.
    '''

    def __init__(self, bow = (0, 0), horizontal = True, length = -1, hit = False):
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
                
    def length_horizontal_bow(self):
        '''
        return length of the ship, its coordinates and is it horizontal
        '''
        return [self.__length, self.horizontal, list(self.bow)]

class Field():
    '''
    Generete field
    '''

    def __init__(self):
        '''
        coor - tuple(int(0..9),int(0..9))
        '''
        #super().__init__()
        self.assig()


    def assig(self):
        '''
        assigment of __ships, field and coor
        :param coora:
        :return:
        '''
        self.field = []
        self.__ships = []
        self.shooted_ships_coor = []
        for i in range(10):
            self.__ships.append(10*[None])

        self.shooted = False

    def generate_field(self):
        """
        Randomly put ships on field
        """
        lmass = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        table = []
        massx = {}
        self.lFieldWithoutShips = []
        for i in range(10):
            table.append([' '] * 10)
            self.lFieldWithoutShips.append([' '] * 10)
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
                    self.__ships[y][x - i] = Ship((y, x - sizes + 1), True, sizes)
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
                    self.__ships[y - i][x] = Ship((y - sizes+1, x), False, sizes)
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
            #self.coor = (y,x)
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
        #print('self.__ships = ', self.__ships)
        #print('self.coor = ', self.coor)

    def shoot_at(self, coor):
        '''
        denend on where player shoot change field with coordinates
        :return:
        '''
        #print('self.field = ', self.field)
        self.coor = coor
        if self.__ships[self.coor[0]][self.coor[1]] != None:
            #print('self.__ships[self.coor[0]][self.coor[1]] = ', self.__ships[self.coor[0]][self.coor[1]])
            self.field[self.coor[0]][self.coor[1]] = 'X'
            self.lFieldWithoutShips[self.coor[0]][self.coor[1]] = 'X'
            self.__ships[self.coor[0]][self.coor[1]].__hit = True
            if (self.coor[0],self.coor[1]) not in self.shooted_ships_coor:
                self.shooted_ships_coor.append((self.coor[0],self.coor[1]))
            self.shooted = True
            leng, hor, fbow =  self.__ships[self.coor[0]][self.coor[1]].length_horizontal_bow()
            fb = True
            #fbow[0], fbow[1] = fbow[0]+1, fbow[1]-1
            # next lines are for the moment when you hit all ship
            if hor:
                fb = False
                for i in range(leng):
                    if self.field[fbow[0]][fbow[1]+i] != 'X':
                        fb = True
                        break
                if not fb:
                    print('self.field =', self.field)
                    print('fbow =', fbow)
                    if fbow[0] > 0:
                        for i in range(leng):
                            self.field[fbow[0]-1][fbow[1]+i] = 'o'
                            self.lFieldWithoutShips[fbow[0]-1][fbow[1]+i] = 'o'
                    if fbow[0] < 9:
                        for i in range(leng):
                            self.field[fbow[0]+1][fbow[1]+i] = 'o'
                            self.lFieldWithoutShips[fbow[0]+1][fbow[1]+i] = 'o'
                    if fbow[1] > 0:
                        if fbow[0] > 0:
                            self.field[fbow[0]-1][fbow[1]-1] = 'o'
                            self.lFieldWithoutShips[fbow[0]-1][fbow[1]-1] = 'o'
                        self.field[fbow[0]][fbow[1]-1] = 'o'
                        self.lFieldWithoutShips[fbow[0]][fbow[1]-1] = 'o'
                        if fbow[0] < 9:
                            self.field[fbow[0]+1][fbow[1]-1] = 'o'
                            self.lFieldWithoutShips[fbow[0]+1][fbow[1]-1] = 'o'
                    if fbow[1] < 9:
                        if fbow[0] > 0:
                            self.field[fbow[0]-1][fbow[1]+leng - 1] = 'o'
                            self.lFieldWithoutShips[fbow[0]-1][fbow[1]+leng-1] = 'o'
                        self.field[fbow[0]][fbow[1]+leng-1] = 'o'
                        self.lFieldWithoutShips[fbow[0]][fbow[1]+leng-1] = 'o'
                        if fbow[0] < 9:
                            self.field[fbow[0]+1][fbow[1]+1] = 'o'
                            self.lFieldWithoutShips[fbow[0]+1][fbow[1]+leng-1] = 'o'  
                
            else:
                fb = False
                for i in range(leng):
                    if self.field[fbow[0]+i][fbow[1]] != 'X':
                        fb = True
                        break
                #if not fb and leng != 1:
                    #fbow[0], fbow[1] = fbow[1], fbow[0]
                if not fb:
                    print('self.field =', self.field)
                    print('fbow =', fbow)
                    if fbow[1] > 0:
                        for i in range(leng):
                            self.field[fbow[0]+i][fbow[1]-1] = 'o'
                            self.lFieldWithoutShips[fbow[0]+i][fbow[1]-1] = 'o'
                    if fbow[1] < 9:
                        for i in range(leng):
                            self.field[fbow[0]+i][fbow[1]+1] = 'o'
                            self.lFieldWithoutShips[fbow[0]+i][fbow[1]+1]= 'o'
                    if fbow[0] > 0:
                        if fbow[1] > 0:
                            self.field[fbow[0]-1][fbow[1]-1] = 'o'
                            self.lFieldWithoutShips[fbow[0]-1][fbow[1]-1] = 'o'
                        self.field[fbow[0]-1][fbow[1]] = 'o'
                        self.lFieldWithoutShips[fbow[0]-1][fbow[1]] = 'o'
                        if fbow[1] < 9:
                            self.field[fbow[0]-1][fbow[1]+1] = 'o'
                            self.lFieldWithoutShips[fbow[0]-1][fbow[1]+1] = 'o'
                    if fbow[0] < 9:
                        if fbow[1] > 0:
                            self.field[fbow[0]+leng][fbow[1]-1] = 'o'
                            self.lFieldWithoutShips[fbow[0]+leng][fbow[1]-1] = 'o'
                        self.field[fbow[0]+leng][fbow[1]] = 'o'
                        self.lFieldWithoutShips[fbow[0]+leng][fbow[1]] = 'o'
                        if fbow[1] < 9:
                            self.field[fbow[0]+leng][fbow[1]+1] = 'o'
                            self.lFieldWithoutShips[fbow[0]+leng][fbow[1]+1] = 'o'  
                      
             
            #print('yey')
            #print(self.__ships[self.coor[0]][self.coor[1]])
            #print('self.field = ', self.field)
        else:
            self.field[self.coor[0]][self.coor[1]] = 'o'
            self.lFieldWithoutShips[self.coor[0]][self.coor[1]] = 'o'
            self.shooted = False

    def field_without_ships(self):
        '''
        return field without ships for enemy player
        :return:  list
        '''
        ResultFWOS = []

        for el in self.lFieldWithoutShips:
            stri = ''
            for lette in el:
                stri += lette
            ResultFWOS.append(stri)
        return ResultFWOS

    def field_with_ships(self):
        '''
        return field with all ships for player
        :return:
        '''
        ResultFWS = []
        for el in self.field:
            stri = ''
            for lette in el:
                stri += lette
            ResultFWS.append(stri)
        return ResultFWS


class Player:
    '''
    have all we need from player: name and coordinates of shoot.
    '''
    def __init__(self):
        '''
        initialise name of player.
        :param name: str
        '''
        self.__name = input('Please write your name ')

    def p_name(self):
        return self.__name

    def read_position(self):
        '''
        take coordinates and change it in type we need.
        from letter number to tuple(number, number)
        :return:
        '''
        rpcoor = input('Please write coordinates as A7, J5 ')
        #print(ord(rpcoor[0].lower()))
        rpcoor = [rpcoor[0], rpcoor[1:]]
        if rpcoor[0].lower() not in ascii_lowercase[:10]:
            rpcoorconv = (-1, -1)
        else:
            rpcoor[1] = int(rpcoor[1])
            rpcoorconv = (ord(rpcoor[0].lower()) - ord('a'), rpcoor[1]-1)

        while (rpcoorconv[0] > 9 or rpcoorconv[0] < 0 ) or (rpcoorconv[1] > 9 or rpcoorconv[1] < 0):
            print("Your input is incorrect. Letter should be 'A' - 'J' and number 1 - 10 \n")
            rpcoor = input('Please write coordinates as A7, J5 ')
            if rpcoor[0].lower()  not in ascii_lowercase[:10]:
                rpcoorconv = (-1, -1)

            else:
                rpcoorconv = (ord(rpcoor[0].lower()) - ord('a'), int(rpcoor[1:]) - 1)

        return rpcoorconv



class Game:
    '''
    connect all classes before and is main for playing
    '''
    def __init__(self):
        '''
        initialise players, fields, index of current player, generate field for 2 in field.
        '''

        self.__players = (Player(), Player())
        self.__field = (Field(), Field())
        self.__field[0].generate_field()
        self.__field[1].generate_field()
        #print(self.__field[0].field_with_ships(), '\n', self.__field[1].field_with_ships())
        self.__current_player = 0
        self.shoot_coord = [(0,0), (0,0)]
        self.mass = '  12345678910'
        
    def current_player(self):
        '''
        return current player
        '''
        return self.__players[self.__current_player]
        
    def end_turn(self):
        '''
        increase index of current_player
        '''
        self.__current_player = (self.__current_player + 1) % 2
        
    def name_player(self):
        return self.current_player().p_name()
        
    def G_read_position(self):
        '''
        read coordinates
        :return:
        '''
        self.shoot_coord[self.__current_player] = self.__players[self.__current_player].read_position()
        self.__field[self.__current_player].shoot_at(self.shoot_coord[self.__current_player])

    def G_field_without_ships(self):
        '''
        return field without ships other index's player
        :return:
        '''
        return self.__field[self.__current_player ].field_without_ships()

    def G_field_with_ships(self):
        '''

        :return: field with ships index's player
        '''
        return self.__field[(self.__current_player + 1) % 2].field_with_ships()


    def print_field(self):
        '''
        print fields
        :return:
        '''
        #system('cls')
        print('Game Battleship\n')
        print("It's {0}'s turn.\n ".format(self.name_player()))
        print("It's your field.")

        fws = self.G_field_with_ships()
        print(self.mass)
        for i in range(10):
            print("{0} {1}".format(ascii_uppercase[i], fws[i]))

        print("It's your enemy's field.")
        self.print_enemy_field()

    def print_enemy_field(self):
        '''
        print enemy field
        :return:
        '''
        fwos = self.G_field_without_ships()

        print(self.mass)
        for i in range(10):
            print("{0} {1}".format(ascii_uppercase[i], fwos[i]))


    def start(self):
        '''
        main function
        :return:
        '''
        self.print_field()

        self.G_read_position()
        print('Good shoot.\n')

        system('cls')

        while self.__field[self.__current_player].shooted:
            self.print_field()

            self.G_read_position()
            print('Good shoot.\n')
            system('cls')
        else:
            print("You don't hurt enemy's ship.")
            self.end_turn()

        print('Your turn is end.')
        sleep(7)
        self.print_field()

        self.G_read_position()
        
        system('cls')
        print('Good shoot.\n')

        while self.__field[self.__current_player].shooted:
            self.print_field()

            self.G_read_position()
            
            system('cls')
            print('Good shoot.\n')
        else:
            print("You don't hurt enemy's ship.")
            self.end_turn()

        print('Your turn is end.')
        sleep(7)

        while len(self.__field[self.__current_player].shooted_ships_coor) < 20:
            self.print_field()

            self.G_read_position()
            

            system('cls')
            print('Good shoot.\n')

            while self.__field[self.__current_player].shooted:
                self.print_field()

                self.G_read_position()
                
                system('cls')
                print('Good shoot.\n')
            else:
                print("You don't hurt enemy's ship.")
                self.end_turn()

            print('Your turn is end.')
            sleep(7)
        else:
            self.end_turn()
            print('Congratulations!')
            print('Player {0} win.'.format(self.name_player()))


n = Game()
n.start()


