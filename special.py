import pygame
from pygame.locals import *
from time import *
import random 

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Coin collection game")

#player
player = pygame.image.load("kirby.png")
player_rect= player.get_rect()
player_rect.topleft=(200,200)

background = pygame.image.load("background.jpeg")

coin_img = pygame.image.load("coin.png")
coins = []

for i in range(10):
    x= random.randint(50,550)
    y= random.randint(50,550)
    coin_rect = coin_img.get_rect(topleft =(x,y))
    coins.append(coin_rect)

score = 0
keys = [False, False, False, False]
clock = pygame.time.Clock()
  
running = True

while running:
    screen.blit(background, (0,0))
    screen.blit(player,player_rect)
    for coin in coins:
        screen.blit(coin_img,coin)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_w: keys[0]= True
            if event.key == K_a: keys[1]= True
            if event.key == K_s: keys[2]= True
            if event.key == K_d: keys[3]= True
        
        if event.type == pygame.KEYUP:
            if event.key == K_w: keys[0]= False
            if event.key == K_a: keys[1]= False
            if event.key == K_s: keys[2]= False
            if event.key == K_d: keys[3]= False
        
    if keys[0] and player_rect.top >0:
            player_rect.y -= 3
            
    if keys[2] and player_rect.bottom <600:
            player_rect.y += 3  

    if keys[1] and player_rect.left >0:
            player_rect.x -= 3 
            

    if keys[3] and player_rect.right <600: 
            player_rect.x += 3 

    for coin in coins[:]:
            if player_rect.colliderect(coin):
                 coin.remove(coin) 
                 score += 1
                 print("Score : ", score)

    clock.tick(60) 

    pygame.quit()
            

            

            
            
            
            
            

            

                


