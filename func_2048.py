from tkinter import *
from tkinter import messagebox
import random

class GAME_FUN:
    background={
    '2': "#eee4da", '4': "#ede0c8", '8': "#f2b179",
    '16': "#f59563", '32': "#f67c5f", '64': "#f65e3b",
    '128': "#edcf72", '256': "#edcc61", '512': "#edc850",
    '1024': "#edc53f", '2048': "#edc22e",

    '4096': "#eee4da", '8192': "#edc22e", '16384': "#f2b179",
    '32768': "#f59563", '65536': "#f67c5f"
}
    color={
    '2': '#776e65', '4': '#f9f6f2', '8': '#f9f6f2',
    '16': '#f9f6f2', '32': '#f9f6f2', '64': '#f9f6f2',
    '128': '#f9f6f2', '256': '#f9f6f2', '512': '#776e65',
    '1024': '#f9f6f2', '2048': '#f9f6f2',

    '4096': "#776e65", '8192': "#f9f6f2", '16384': "#776e65",
    '32768': "#776e65", '65536': "#f9f6f2",
}
    def __init__(self):
        self.n=4
        self.window=Tk()
        self.window.title('2048 Game')
        self.gameArea=Frame(self.window,bg= '#92877d')
        self.GAME_FUN=[]
        self.GridCell=[[0]*4 for i in range(4)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0

        for i in range(4):
            rows=[]
            for j in range(4):
                l=Label(self.gameArea,text='',bg='#BBADA0',
                font=('arial',22,'bold'),width=4,height=2)
                l.grid(row=i,column=j,padx=7,pady=7)
                rows.append(l);
            self.GAME_FUN.append(rows)
        self.gameArea.grid()

    def reverse(self):
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                self.GridCell[ind][i],self.GridCell[ind][j]=self.GridCell[ind][j],self.GridCell[ind][i]
                i+=1
                j-=1

    def transpose(self):
        self.GridCell=[list(t)for t in zip(*self.GridCell)]

    def compress_grid(self):
        self.compress=False
        temp=[[0] *4 for i in range(4)]
        for i in range(4):
            cnt=0
            for j in range(4):
                if self.GridCell[i][j]!=0:
                    temp[i][cnt]=self.GridCell[i][j]
                    if cnt!=j:
                        self.compress=True
                    cnt+=1
        self.GridCell=temp

    def merge_grid(self):
        self.merge=False
        for i in range(4):
            for j in range(4 - 1):
                if self.GridCell[i][j] == self.GridCell[i][j + 1] and self.GridCell[i][j] != 0:
                    self.GridCell[i][j] *= 2
                    self.GridCell[i][j + 1] = 0
                    self.score += self.GridCell[i][j]
                    self.merge = True

    def random_cell(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.GridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.GridCell[i][j]=2

    def merge_check(self):
        for i in range(4):
            for j in range(3):
                if self.GridCell[i][j] == self.GridCell[i][j+1]:
                    return True

        for i in range(3):
            for j in range(4):
                if self.GridCell[i+1][j] == self.GridCell[i][j]:
                    return True
        return False

    def Updategrid(self):
        for i in range(4):
            for j in range(4):
                if self.GridCell[i][j]==0:
                    self.GAME_FUN[i][j].config(text='',bg='#BBADA0')
                else:
                    self.GAME_FUN[i][j].config(text=str(self.GridCell[i][j]),
                    bg=self.background.get(str(self.GridCell[i][j])),
                    fg=self.color.get(str(self.GridCell[i][j])))
    

    def Up(self):
        self.Game_Grid.transpose()
        self.Game_Grid.compress_grid()
        self.Game_Grid.merge_grid()
        self.Game_Grid.moved = self.Game_Grid.compress or self.Game_Grid.merge
        self.Game_Grid.merge_grid()
        self.Game_Grid.transpose()


    def Down(self):
        self.Game_Grid.transpose()
        self.Game_Grid.reverse()
        self.Game_Grid.compress_grid()
        self.Game_Grid.merge_grid()
        self.Game_Grid.moved = self.Game_Grid.compress or self.Game_Grid.merge
        self.Game_Grid.compress_grid()
        self.Game_Grid.reverse()
        self.Game_Grid.transpose()

    def Left(self):
        self.Game_Grid.compress_grid()
        self.Game_Grid.merge_grid()
        self.Game_Grid.moved = self.Game_Grid.compress or self.Game_Grid.merge
        self.Game_Grid.compress_grid()

    def Right(self):
        self.Game_Grid.reverse()
        self.Game_Grid.compress_grid()
        self.Game_Grid.merge_grid()
        self.Game_Grid.moved = self.Game_Grid.compress or self.Game_Grid.merge
        self.Game_Grid.compress_grid()
        self.Game_Grid.reverse() 