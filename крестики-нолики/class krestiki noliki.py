import tkinter as tk


class Players:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
        self.field = [['-', '-', '-'] for i in range(3)]

    def who_go(self):
        return f'{self.name1} - X, {self.name2} - 0'

    def make_move(self, player, pos_strok, pos_stolb):
        if player == self.name1:
            self.field[pos_strok][pos_stolb] = 'x'
        else:
            self.field[pos_strok][pos_stolb] = '0'

    def get_field(self):
        return self.field

    def new_game(self):
        self.field = [['-', '-', '-'] for i in range(3)]

    def who_win(self):
        res = 'draw'
        lst = self.field
        for i in range(3):
            if len(set(set(lst[i]))) == 1:
                res = lst[i][0]
        lst = [el for i in lst for el in i]
        f, f1 = lst[0], True
        for i in range(0, 9, 3):
            if lst[i] == f:
                f = lst[i]
            else:
                f1 = False
        if f1:
            res = f
        f, f1 = lst[1], True
        for i in range(1, 9, 3):
            if lst[i] == f:
                f = lst[i]
            else:
                f1 = False
        if f1:
            res = f
        f, f1 = lst[2], True
        for i in range(2, 9, 3):
            if lst[i] == f:
                f = lst[i]
            else:
                f1 = False
        if f1:
            res = f
        f, f1 = lst[0], True
        for i in range(0, 3):
            if lst[i] != f:
                f1 = False
        if f1:
            res = f
        f, f1 = lst[3], True
        for i in range(3, 6):
            if lst[i] != f:
                f1 = False
        if f1:
            res = f
        f, f1 = lst[6], True
        for i in range(6, 9):
            if lst[i] != f:
                f1 = False
        if f1:
            res = f
        f, f1 = lst[0], True
        for i in range(0, 9, 4):
            if lst[i] != f:
                f1 = False
        if f1:
            res = f
        f, f1 = lst[2], True
        for i in range(2, 7, 2):
            if lst[i] != f:
                f1 = False
        if f1:
            res = f
        return res