import tkinter
from tkinter import *
import random

edge=10
r=random
thebomb=[[0 for col in range (0,edge)] for row in range (0,edge)]
bombrandomizer=[0 for col in range (0,int(edge*edge/8))]
num=1
root=Tk()

root.geometry("400x300+0+0")
loc = 0

def bombPosRandomizer():
    global r
    global bombrandomizer
    totalBomb=int(10*10/8)
    same=False
    for random in range (0,totalBomb):
        while (True):
            same=False
            randomizeNumber=r.randint(0,10*10)

            for x in range (0,totalBomb):
                if randomizeNumber== bombrandomizer[x]:
                    same=True
            if same==False:
                bombrandomizer[random]= randomizeNumber
                break
    bombrandomizer.sort()

def getCLicked(xP, yP, number):
    global root
    label = Label(root, text=number, padx=5, pady=1).place(x=xP * 25 + 5, y=yP * 25 + 2)

def SpawnButton (xP, yP ,placement,number):

    bt= Button(placement, text="  ",command=lambda:getCLicked(xP,yP,number),padx=5, pady=1).place(x=xP * 25 + 5, y=yP * 25 + 2)

def surroundChecker(x,y):
    #x=kolom y=baris
    global edge
    global thebomb
    if thebomb[x][y]==10:
        return
    elif thebomb[x][y]==0:
        # atas = y-1
        # bawah =y+1
        # kanan = x+1
        if x==0:
            if y==10:
                return
            if y==0:
                if thebomb[x][y+1]==10:
                    thebomb[x][y]+=1
                if thebomb[x+1][y+1]==10:
                    thebomb[x][y]+=1
                if thebomb[x+1][y]==10:
                    thebomb[x][y]+=1
                return 1
            elif y!=0 and y!=9:
                if thebomb[x][y+1]==10:
                    thebomb[x][y]+=1
                if thebomb[x+1][y+1]==10:
                    thebomb[x][y]+=1
                if thebomb[x+1][y]==10:
                    thebomb[x][y]+=1

                if thebomb[x][y-1] == 10:
                    thebomb[x][y] += 1
                if thebomb[x+1][y-1] == 10:
                    thebomb[x][y] += 1
                return 2
            elif y==9:

                if thebomb[x][y-1] == 10:
                    thebomb[x][y] += 1
                if thebomb[x+1][y-1] == 10:
                    thebomb[x][y] += 1
                if thebomb[x+1][y]==10:
                    thebomb[x][y]+=1
                return 3

bombPosRandomizer()
for y in range (0,10):
    for x in range (0,10):
        if num == bombrandomizer[loc]:
            thebomb[x][y]=10
            loc+=1
            if loc == int(10*10/8):
                loc=0
        else :
            thebomb[x][y]=0

        num+=1
print (bombrandomizer)
print (thebomb)
for x in range (0,10):
    for y in range (0,10):
        print(x,y,thebomb[x][y])
        surroundChecker(x,y)
        print("action :",surroundChecker(x,y))
        SpawnButton(x,y,root,thebomb[x][y])

for y in range (0,10):
    print (y)

print (thebomb)
root.mainloop()