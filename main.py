import pygame 
import time

pygame.init()
screen = pygame.display.set_mode((500,500))



player = pygame.image.load(r"C:\Users\Admin\Desktop\Python\Games\images\rocket.png")
bg = pygame.image.load(r"Games\images\backgroundSpace.png")


playerX= 100
playerY= 10

keys = [False,False,False,False]

while playerY < 400:
    screen.blit(bg, (0,0))
    screen.blit(player, (playerX, playerY))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            if event.key == pygame.K_LEFT:
                keys[1] = True
            if event.key == pygame.K_DOWN:
                keys[2] = True
            if event.key == pygame.K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_LEFT:
                keys[1] = False
            if event.key == pygame.K_DOWN:
                keys[2] = False
            if event.key == pygame.K_RIGHT:
                keys[3] = False   
    if keys[0]:
        if playerY> 0:
            playerY -= 7 
    if keys[1]:
        if playerX> 0:
            playerX -= 7 
    if keys[2]:
        if playerY< 400:
            playerY += 7 
    if keys[3]:
        
        if playerX< 400:
            playerX += 7
    playerY += 5 
    time.sleep(0.05)

print("game over")
