import pygame, sys
from pygame.locals import *
from lifehandler import *

try:
    configFile = open("config.cfg", "r").read()
except FileNotFoundError:
    print("Couldn't find the config.cfg file, aborting")
    sys.exit()

configFileArg = configFile.split(" ")

width = int(configFileArg[0])
height = int(configFileArg[1])

paused = True
isRandom = False
if int(configFileArg[4]) == 1:
    isRandom = True

print(isRandom)

rows = int(configFileArg[2])
cols = int(configFileArg[3])
cellSizeX = width / rows
cellSizeY = height / cols

drawGrid = True
if cellSizeX <= 4 or cellSizeY <= 4:
    drawGrid = False
    
if cellSizeX <= 1 or cellSizeY <= 1:
    print("Render size too small, must be 2 pixels per cell! Aborting!")
    pygame.quit()
    sys.exit()

window = pygame.display.set_mode((width, height))

print("Starting the creation of life...")
life = LifeHandler(rows, cols, isRandom)
print("Done the setup!")

while True:
    window.fill((0, 0, 0))
    pygame.display.set_caption("PyLife - Generations: " + str(life.getGenerations()))

    if not(paused):
        life.step()
        #pygame.time.delay(10)

    for x in range(rows):
        for y in range(cols):
            if life.isAlive(x, y):
                pygame.draw.rect(window, (255, 255, 255), (x * cellSizeX, y * cellSizeY, cellSizeX, cellSizeY))
            if drawGrid:
                pygame.draw.rect(window, (45, 45, 45), (x * cellSizeX, y * cellSizeY, cellSizeX, cellSizeY), 1)
                

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP and event.key == K_RIGHT:
            life.step()
        elif event.type == KEYUP and event.key == K_p:
            paused = not(paused)
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            tileX = int(x / cellSizeX)
            tileY = int(y / cellSizeY)
            life.flipAlive(tileX, tileY)

    pygame.display.update()
