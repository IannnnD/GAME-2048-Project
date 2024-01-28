from tkinter import *
from tkinter import messagebox
import func_2048
from func_2048 import GAME_FUN


class Game:
    def __init__(self,Game_Grid):
        self.Game_Grid=Game_Grid
        self.other_instance = GAME_FUN
        self.lose=False
        self.won=False

    def start(self):
        self.Game_Grid.random_cell()
        self.Game_Grid.random_cell()
        self.Game_Grid.Updategrid()
        self.Game_Grid.window.bind('<Key>', self.key_events)
        self.Game_Grid.window.mainloop()

    def key_events(self,event):
        if self.lose or self.won:
            return

        self.Game_Grid.compress = False
        self.Game_Grid.merge = False
        self.Game_Grid.moved = False

        key=event.keysym

        if key=='W' or key=='w':
            self.other_instance.Up(self)

        elif key=='S' or key=='s':
            self.other_instance.Down(self)
            

        elif key=='A' or key=='a':
            self.other_instance.Left(self)

        elif key=='D' or key=='d':
            self.other_instance.Right(self)
            
        else:
            pass

        self.Game_Grid.Updategrid()
        print(self.Game_Grid.score)

        Finalresult=0
        for i in range(4):
            for j in range(4):
                if(self.Game_Grid.GridCell[i][j]==2048):
                    Finalresult=1
                    break

        if(Finalresult==1):
            self.won=True
            messagebox.showinfo('2048', message='You Win!!')
            print("won")
            return

        for i in range(4):
            for j in range(4):
                if self.Game_Grid.GridCell[i][j]==0:
                    Finalresult=1
                    break

        if not (Finalresult or self.Game_Grid.merge_check()):
            self.lose=True
            messagebox.showinfo('2048','YOU LOSE')
            print("lose")

        if self.Game_Grid.moved:
            self.Game_Grid.random_cell()

        self.Game_Grid.Updategrid()


Game_Grid =func_2048.GAME_FUN()
game2048 = Game(Game_Grid)
game2048.start()