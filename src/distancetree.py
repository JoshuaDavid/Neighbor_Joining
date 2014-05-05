# -*- coding: utf-8
head    = lambda arr: arr[0]
tail    = lambda arr: arr[1:]

class Tree:
    parent = None
    def __init__(self, left = None, right = None, dleft = 1, dright = 1):
        self.left  = left
        left.parent = self
        self.right = right
        left.dparent = dleft
        right.parent = self
        self.dleft  = dleft
        right.dparent = dright
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
        if other.__class__.__name__ != "Tree":
            return False
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
    def contains(self, other):
        if id(self) == id(other):
            return True
        else:
            if other.parent == None:
                return False
            else:
                return self.contains(other.parent)
    def distanceTo(self, other):
        if id(self) == id(other):
            return 0
        elif self.contains(other):
            return other.dparent + self.distanceTo(other.parent)
        elif other.contains(self):
            return self.dparent + other.distanceTo(self.parent)
        elif self.parent and other.parent:
            return self.dparent + other.dparent + self.parent.distanceTo(other.parent)
        else:
            raise LookupError("Nodes are not in the same tree!")

class Leaf(Tree):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
