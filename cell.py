class Cell:

    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive

    def setAlive(self, state):
        self.alive = state

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def isAlive(self):
        return self.alive
