import random

class Ship:
    def __init__(self, bow, horizontal, length, hit):
        self.assignmentblhh(bow, length, horizontal, hit)


    def assignmentblhh(self, b, l, ho, hi):
        self.bow = b
        self.__length = l
        self.horizontal = ho
        assert isinstance(hi, object)
        self.hit = hi
