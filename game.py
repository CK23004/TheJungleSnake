import pygame
from pygame.locals import *
import random
import os
import sys
pygame.init()
pygame.font.init()
game_display=pygame.display.set_mode((900,600))
pygame.display.set_caption("Snake Game by Chinmay")
pygame.mixer.init()
welcome_img=pygame.image.load('entry.jpg')
gameloop_img=pygame.image.load('gameloop.jpeg')
gameover_img=pygame.image.load('game_over1.jpg')
fill=pygame.surface
pygame.display.update()
clock=pygame.time.Clock()

def border(game_display,x,y):
    for i in range(8):
        pygame.draw.rect(game_display,'#002929',(x-i,y-i,852,523),1)

font=pygame.font.SysFont('comicsansms',25,'bold')
font1=pygame.font.SysFont('comicsansms',27,'bold')
font2=pygame.font.SysFont('comicsansms',25,'bold')
def winloop():
    exit_game = False
    white = 'white'
    color_light ='#8B4513'
    color_dark = '#CD853F'
    sound_entry = pygame.mixer.Sound("entry generated.mp3")
    sound_entry.play(-1)
   

    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if 100 <= mouse[0] <= 200 and 450 <= mouse[1] <= 490:
                    sound_entry.stop()
                    gameloop()
                    # start=True
                if 250 <= mouse[0] <= 350 and 450 <= mouse[1] <= 490:
                    exit_game=True

        game_display.fill('white')
        text_button1 = "Play"
        text_button2 = "Exit"
        screen_button1 = font2.render(text_button1, True, white)
        screen_button2 = font2.render(text_button2, True, white)

        mouse = pygame.mouse.get_pos()




        game_display.blit(welcome_img,[0,0])
        if 100 <= mouse[0] <= 200 and  450<= mouse[1] <=490:
            pygame.draw.rect(game_display, color_light, [100, 450, 120, 50])
        else:
            pygame.draw.rect(game_display, color_dark, [100, 450, 120, 50])
        if 250 <= mouse[0] <= 350 and 450 <= mouse[1] <= 490:
            pygame.draw.rect(game_display, color_light, [250, 450, 120, 50])
        else:
            pygame.draw.rect(game_display, color_dark, [250, 450, 120,50])
        game_display.blit(screen_button1, [130, 455])
        game_display.blit(screen_button2, [280, 455])
        pygame.display.update()
    pygame.quit()
    quit()
def screen_score(text,x,y,color):
    screen_text=font.render(text,True,color)
    game_display.blit(screen_text,[x,y])
def plot_snake(game_display,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_display,color,[x,y,snake_size,snake_size])

def gameloop():

    exit_game = False
    game_over = False
    red='red'
    black='black'
    # color_light ='#7e3934'
    color_light ='#8B4513'
    color_dark = '#CD853F'
    border_x=27
    border_y=50
    snake_x=random.randint(40,840)
    snake_y=random.randint(60,540)
    snake_l=20
    snake_size=20
    fps=30
    score=0
    food_x=random.randint(40,840)
    food_y=random.randint(60,540)
    food_r=5
    velocity_x=0
    velocity_y=0
    white='white'
    snk_list=[]
    snk_length=10
    highscore1=[]
    sound_gameplay = pygame.mixer.Sound("Ludo king game bgm.mp3")
    sound_gameover = pygame.mixer.Sound("game over new.mp3")
    sound_gameplay.play()

    spped=[]

    while not exit_game:

        if game_over:


            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if 510 <= mouse[0] <= 670 and 390 <= mouse[1] <= 540:
                        winloop()
                    if 310 <= mouse[0] <= 470 and 390 <= mouse[1] <= 540:
                        gameloop()
            text_button2 = "Play Again"
            text_button1 = "Main Menu"
            screen_button1 = font2.render(text_button1, True, white)
            screen_button2 = font2.render(text_button2, True, white)
            game_display.fill('white')
            game_display.blit(gameover_img,[0,0])

            mouse=pygame.mouse.get_pos()

            if 510 <= mouse[0] <= 670 and 390 <= mouse[1] <= 540:
                pygame.draw.rect(game_display, color_light, [490, 390, 160, 50])
             
            else:
                pygame.draw.rect(game_display, color_dark, [490, 390, 160, 50])
            if 310 <= mouse[0] <= 470 and 390 <= mouse[1] <= 540:
                pygame.draw.rect(game_display, color_light, [290, 390, 160, 50])
            else:
                pygame.draw.rect(game_display, color_dark, [290, 390, 160, 50])
            text2= f"{score}"
            text3= f"{highscore1}"
            game_display.blit(screen_button1, [500, 395])
            game_display.blit(screen_button2, [300, 395])
            
            screen_text3 = font1.render(text2, True, white)
            screen_text4 = font1.render(text3, True, white)
 
            game_display.blit(screen_text3, [415, 332])
            game_display.blit(screen_text4, [700, 332])
            pygame.display.update()



        else:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==K_RIGHT:
                        velocity_x=3
                        velocity_y=0

                    if event.key==K_LEFT:
                        velocity_x=-3
                        velocity_y=0


                    if event.key==K_DOWN:
                        velocity_y=3
                        velocity_x=0
                    if event.key == K_UP:
                        velocity_y=-3
                        velocity_x=0

            if  abs(snake_x-food_x)<20 and abs(snake_y-food_y)<20:
                score = score + 10
                food_x = random.randint(40,840)
                food_y = random.randint(60,540)
                snk_length+=1
            if not (os.path.exists("highscore.txt")):
                with open ("highscore.txt","w") as f:
                     f.write("0")
                     f.close()
            f = open("highscore.txt", "r")
            highscore1 = f.read()
            highscore2=int(highscore1)
            f.close()
            highscore = score

            if highscore2<=score:
                f = open("highscore.txt", "w")
                f.write(str(highscore))
                f.close()
            if 100>score>=30:
                snake_x = snake_x + 2 * (velocity_x)
                snake_y = snake_y + 2 * (velocity_y)
            if 200> score >= 100:
                snake_x = snake_x + 3 * (velocity_x)
                snake_y = snake_y + 3 * (velocity_y)
            if 300> score >= 200:
                snake_x = snake_x + 4 * (velocity_x)
                snake_y = snake_y + 4 * (velocity_y)
            if 500> score >= 300:
                snake_x = snake_x + 5*(velocity_x)
                snake_y = snake_y + 5*(velocity_y)
            if 750 > score >= 500:
                snake_x = snake_x + 7 * (velocity_x)
                snake_y = snake_y + 7 * (velocity_y)
            if 1000 > score >= 750:
                snake_x = snake_x + 10* (velocity_x)
                snake_y = snake_y + 10* (velocity_y)

            if score<30:
                snake_x=snake_x+velocity_x
                snake_y=snake_y+velocity_y
            game_display.fill('white')
            fill.Surface.fill(game_display, '#002929')
            game_display.blit(gameloop_img, [25, 50])

            border(game_display,border_x,border_y)

            screen_score(f"SCORE : {str(score)}   BEST : {highscore1}", 30, 10,'white')

            pygame.draw.rect(game_display, red, [food_x, food_y,snake_size-5,snake_size-5])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            for x,y in snk_list:
                if x>=850 or y>=545 or x<30 or y<50 :
                    sound_gameplay.stop()
                    sound_gameover.play()
                    game_over=True
            white='white'
            plot_snake(game_display,white,snk_list,snake_size)
            pygame.display.update()
            clock.tick(fps)




    pygame.quit()
    quit()
if __name__ == '__main__':
    winloop()
