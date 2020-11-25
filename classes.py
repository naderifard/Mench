from data import *

boarddic={}
for i in mainboard:
    boarddic[i]=None

class Piece:
    def __init__(self,color):
        self.color=color
        self.place="out"

    @property
    def path(self):
        i = colors.index(self.color)
        home=Homes[i]
        path=[home]
        for j in Path[i:]:
            path+=j
        for k in Path[:i]:
            path+=k
        path+=SPECIAL[i]
        return path
    def enter(self):
        self.place=self.path[0]
        boarddic[self.place] = self.color
        print("piece entered")
    @property
    def check_enter(self):
        if boarddic[self.place] == self.color:
            return False
        else:
            return True

    def move(self,m):
        boarddic[self.place]=None
        now=self.path.index(self.place)
        now+=m
        self.place=self.path[now]
        print("piece moved to "+str(self.place))
        boarddic[self.place] = self.color

    def check_move(self,m):
        now=self.path.index(self.place)
        if boarddic[self.path[now+m]]==self.color:
            return False
        else:
            return True


###################################################################
class Person:
    def __init__(self,name,color):
        self.color=color
        self.name=name
        for i in range(4):
            Piece(self.color)
        self.pieces={}
        for i in range(4):
            x=Piece(self.color)
            self.pieces[i]=x
    @property
    def n(self):
        N=0
        for i in self.pieces:
            p=self.pieces[i]
            if p.place in p.path:
                N+=1
        return N

    @property
    def win(self):
        count = 0
        for i in self.pieces[0].path[-5:-1]:
            if boarddic[i] == self.color:
                count += 1
        if count == 4:
            return True
        else:
            return False
