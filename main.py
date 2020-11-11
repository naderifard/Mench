from toss import toss
from classes import Piece,Person
from data import colors
winner=None
player1=Person("Behdad","Blue")
player2=Person("Khashi","Red")
players=[player1,player2]

turn=None
t=toss()
print(t)
if t[0]<=3:
    T=0
else:
    T=1

turn=players[T]
print(players[T].name+" begins:")
def myfunc(t,turn):
    for i in t:
        if i==6:
            if turn.n!=4:
                tmp=input("enter or go?")
                if tmp=="enter" and turn.pieces[0].check_enter:
                    for j in turn.pieces:
                        k=turn.pieces[j]
                        if k.place=="out":
                            k.enter()
                            break
                elif tmp=="go":
                    p=int(input("choose your piece(number):"))
                    if turn.pieces[p].check_move(i):
                        turn.pieces[p].move(i)
            if turn.n==4:
                p = int(input("choose your piece(number):"))
                if turn.pieces[p].check_move(i):
                    turn.pieces[p].move(i)
        else:
            p = int(input("choose your piece(number):"))
            if turn.pieces[p].check_move(i):
                turn.pieces[p].move(i)


while not winner:
    if turn.n==0:
        for i in range(3):
            t=toss()
            print(t)
            if t[0]==6:
                turn.pieces[0].enter()
                t=t[1:]
                myfunc(t,turn)
                break

        if turn.win:
            print(players[T].name+" WON!")
            break

        T+=1
        T%=2
        turn=players[T]
        print("turn="+(players[T]).name)
    else:
        t=toss()
        print(t)
        myfunc(t,turn)

        if turn.win:
            print(players[T].name+" WON!")
            break
        T += 1
        T %= 2
        turn = players[T]
        print("turn="+(players[T]).name)

