# -*- coding: utf-8
head    = lambda arr: arr[0]
tail    = lambda arr: arr[1:]

class Leaf:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name

class Tree:
    def __init__(self, left = None, right = None, dleft = 1, dright = 1):
        self.left  = left
        self.right = right
        self.dleft  = dleft
        self.dright = dright
    def __repr__(self):
        s = "┬" + ("─" * int(self.dleft))
        if self.left:
            left = repr(self.left).splitlines()
            s += "" + head(left) + "\n"
            for line in tail(left):
                s += "│"  + (" " * int(self.dleft))
                s += line + "\n"
        if self.right:
            right = repr(self.right).splitlines()
            s += "└" + ("─" * int(self.dright))
            s += head(right) + "\n"
            for line in tail(right):
                s += " "  + (" " * int(self.dright))
                s += line + "\n"
        return s
    def __eq__(self, other):
        if self.left == other.left:
            return  self.left   == other.left   and \
                    self.right  == other.right  and \
                    self.dleft  == other.dleft  and \
                    self.dright == other.dright
        else:
            return  self.left   == other.right  and \
                    self.right  == other.left   and \
                    self.dleft  == other.dright and \
                    self.dright == other.dleft

