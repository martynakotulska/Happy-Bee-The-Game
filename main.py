import pygame

#Intialize the pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Happy Bee")
icon = pygame.image.load('bee.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

#Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((225, 225, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    player()
    pygame.display.update()