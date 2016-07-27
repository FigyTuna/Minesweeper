#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from random import randint

print("Minesweeper")

A = 65

class Cell:

    def __init__(self):

        self.mine = False
        self.uncovered = False
        self.content = "_"
        
    def read(self):
        if(self.uncovered):
            return self.content
        return "#"
        
    def uncover(self):
        if not self.uncovered:
            self.uncovered = True

class Game:

    def __init__(self, numMines, length):
    
        self.numMines = numMines
        self.length = length
        self.numUncovered = 0
        self.mines = []
        for i in range(0, length):
            self.mines.append([])
            for j in range(0, length):
                self.mines[i].append(Cell())
        
        mLeft = numMines
        while mLeft > 0:
            x = randint(0, length - 1)
            y = randint(0, length - 1)
            if self.mines[x][y].content == "_":
                self.mines[x][y].content = "*"
                for i in range(0, 3):
                    for j in range(0, 3):
                        try:
                            self.incNum(x - 1 + i, y - 1 + j)
                        except:
                            pass
                    
                mLeft = mLeft - 1
                
        #for i in range(0, length):
            #for j in range(0, length):
                #self.mines[i][j].uncover()
                
    def incNum(self, x, y):
        if not x == -1 and not y == -1:
            if not self.mines[x][y].content == "*":
                if self.mines[x][y].content == "_":
                    self.mines[x][y].content = "1"
                else:
                    self.mines[x][y].content = str(int(self.mines[x][y].content) + 1)

    def read(self):
    
        p = "   "
        for i in range(0, len(self.mines)):
            p = p + chr(A + i) + " "
        print(p)
        for i in range(0, len(self.mines)):
            p = str(i + 1) + " "
            if i < 9:
                p = p + " "
            for j in range(0, len(self.mines)):
                p = p + self.mines[i][j].read() + " "
            print(p)

    def play(self):
        while self.numMines < self.length * self.length - self.numUncovered:
            self.read()
            t = input(">>")
            if len(t) > 1:
                for i in range(0, len(self.mines)):
                    if t[0] == chr(65 + i) or t[0] == chr(97 + i):
                        n = 100
                        if len(t) == 2:
                            n = int(t[1])
                        elif len(t) == 3:
                            n = int(t[1] + t[2])
                        if len(self.mines) > n-1 and not (n == 0):
                            self.uncoverCell(n-1,i)
        self.read()
        print("Game Over")
                            
    def uncoverCell(self, x, y):
        if not self.mines[x][y].uncovered and not x == -1 and not y == -1:
            self.mines[x][y].uncover()
            self.numUncovered = self.numUncovered + 1
            if self.mines[x][y].content == "*":
                self.numUncovered = self.length * self.length
            if self.mines[x][y].content == "_":
                for i in range(0, 3):
                    for j in range(0, 3):
                        try:
                            self.uncoverCell(x-1+i,y-1+j)
                        except:
                            pass
        
        

g = Game(20, 15)
g.play()









