import pygame
from pygame.locals import *
from time import *
import random 

pygame.init()
screen = pygame.display.set_mode((600,600))
player_x = 200
player_y = 200
keys = [False, False, False, False]
player = pygame.image.load("kirby.png")
background = pygame.image.load("background.jpeg")
coin = pygame.image.load("coin.png")
coins = []
x= random.randint(0,600)
y= random.randint(0,600)

for i in range(10):
    new_coin = (x,y)
    coins.append(new_coin)

    score = 0
    collected_coins = pygame.sprite.spritecollide(player,coin, True)

    for coin in collected_coins:
        score += 1
        print("Score: " + "score")

while player_y < 600:
    screen.blit(background, (0,0))
    screen.blit(player, (player_x,player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0]= True
            elif event.key == K_a:
                keys[1]= True
            elif event.key == K_s:
                keys[2]= True
            elif event.key == K_d:
                keys[3]= True
        
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0]= False
            elif event.key == K_a:
                keys[1]= False
            elif event.key == K_s:
                keys[2]= False
            elif event.key == K_d:
                keys[3]= False
        
    if keys [0]:
        if player_y >0:
            player_y -= 2
            
    elif keys [2]:
        if player_y >536: 
            player_y += 7 
            
    if keys [1]:
        if player_x >0: 
            player_x -= 2 
            

    elif keys [3]:
        if player_x <536:  
            player_x += 2  


            player_y +=5
            sleep(0.05)

    print("Game Over")

            

            
            
            
            
            

            

                


