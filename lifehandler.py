import random
from cell import *

class LifeHandler:
    def __init__(self, width, height, random):
        self.width = width
        self.height = height

        self.generations = 0

        self.cells = []
        if random:
            self.randinit()
        else:
            self.init(self.cells)

    def randinit(self):
        for x in range(self.width):
            for y in range(self.height):
                self.cells.append(Cell(x, y, bool(random.getrandbits(1))))

    def init(self, cells):
        for x in range(self.width):
            for y in range(self.height):
                cells.append(Cell(x, y, False))

    def step(self):
        self.generations += 1
        updatedCells = []
        self.init(updatedCells)

        for x in range(self.width):
            for y in range(self.height):
                neighbours = self.getNeighbours(x, y)

                if self.isAlive(x, y):
                    if neighbours < 2 or neighbours > 3:
                        updatedCells[x + y * self.width].setAlive(False)
                    else:
                        updatedCells[x + y * self.width].setAlive(True)
                else:
                    if neighbours == 3:
                        updatedCells[x + y * self.width].setAlive(True)
                    
        self.cells = updatedCells
        
                    

    def getNeighbours(self, x, y):
        neighbours = 0
        
        # top
        if y != 0:
            if self.isAlive(x, y - 1):
                neighbours += 1
        # top right
        if x != self.width - 1 and y != 0:
            if self.isAlive(x + 1, y - 1):
                neighbours += 1
        # right
        if x != self.width - 1:
            if self.isAlive(x + 1, y):
                neighbours += 1
        # bot right
        if x != self.width - 1 and y != self.height - 1:
            if self.isAlive(x + 1, y + 1):
                neighbours += 1
        # bot
        if y != self.height - 1:
            if self.isAlive(x, y + 1):
                neighbours += 1
        # bot left
        if x != 0 and y != self.height - 1:
            if self.isAlive(x - 1, y + 1):
                neighbours += 1
        # left
        if x != 0:
            if self.isAlive(x - 1, y):
                neighbours += 1
        # top left
        if x != 0 and y != 0:
            if self.isAlive(x - 1, y - 1):
                neighbours += 1

        return neighbours

    def flipAlive(self, x, y):
        self.setAlive(x, y, not(self.cells[x + y * self.width].isAlive()))

    def setAlive(self, x, y, alive):
        self.cells[x + y * self.width].setAlive(alive)

    def isAlive(self, x, y):
        return self.cells[x + y * self.width].isAlive()

    def getGenerations(self):
        return self.generations
