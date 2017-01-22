
from __future__ import print_function
import pygame, sys
from pygame.locals import *
from random import randint
import random



pygame.init()

fpsClock = pygame.time.Clock()
fps = 60

black = (0, 0, 0)
white = (255, 255,  255)
red = (255, 0, 0)
gold = (255, 180, 0)
aqua = (0, 255, 246)
navy = (16, 0, 255)
green = (0, 255, 0)
colourList = [white, red, gold, aqua, navy, green]


font = pygame.font.SysFont("Calibri", 25, True, False)
text = font.render("My text", True, black)

size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Test")

lightList = []
def shootLight():
    lightx = spaceShipx + 32
    lighty = spaceShipy + 10
    lightList.append([lightx, lighty])
lightList1 = []
def spawnLight(n):
    for i5 in range(n):
        lightx1 = randint(10, 790); lighty1 = randint(10, 590)
        lightList1.append([lightx1, lighty1])

starList = []
for i in range(50):
    starx = randint(3, 797); stary = randint(3, 597)
    starList.append([starx, stary])


spaceShip = pygame.image.load("spaceShip.png")
meteor = pygame.image.load("meteor.png")
shootSound = pygame.mixer.Sound("laser.ogg")
theme = pygame.mixer.Sound("spaceGameTheme.ogg")

meteorx = randint(0, 734)
meteory = randint(0, 534)



jsCount = pygame.joystick.get_count()
if jsCount >= 1:
    js = pygame.joystick.Joystick(0)
    js.init()
else:
    print("No joystick detected.")
spaceShipx = 368; spaceShipy = 520
theme.play(-1)

while True:


    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == JOYAXISMOTION:
            if js.get_axis(2) < -0.85:
                shootSound.play()
                shootLight()
        elif e.type == JOYBUTTONDOWN:
            if js.get_button(4) == 1 and js.get_button(5) == 1:
                spawnLight(10)




    screen.fill(black) # Clears the screen

    for i1 in range(len(starList)):
        pygame.draw.circle(screen, white, starList[i1], 3)
    for i2 in range(len(lightList)):
        pygame.draw.circle(screen, colourList[randint(0, 3)], lightList[i2], 8)
        lightList[i2][1] -= 4
    for i6 in range(len(lightList1)):
        pygame.draw.circle(screen, colourList[randint(0, 3)], lightList1[i6], 12)
        lightList1[i6][1] -= 4
    if len(lightList) > 500:
        del lightList[0:430]
    if len(lightList1) > 500:
        del lightList1[0:430]

    meteorxSpeed = int(js.get_axis(4)*3); meteorx += meteorxSpeed
    meteorySpeed = int(js.get_axis(3)*3); meteory += meteorySpeed
    screen.blit(meteor, (meteorx, meteory))



    spaceShipxSpeed = int(js.get_axis(0)*5); spaceShipx += spaceShipxSpeed
    spaceShipySpeed = int(js.get_axis(1)*5); spaceShipy += spaceShipySpeed
    screen.blit(spaceShip, (spaceShipx, spaceShipy))
    if spaceShipx >= 734:
        spaceShipx = 734
    elif spaceShipx <= 0:
        spaceShipx = 0
    if spaceShipy >= 534:
        spaceShipy = 534
    if spaceShipy <= 0:
        spaceShipy = 0





    pygame.display.flip()
    fpsClock.tick(fps)
