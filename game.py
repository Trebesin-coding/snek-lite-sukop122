import pygame as pg
from sys import exit
import random
import math

pg.init()

def image_cut(sheet, frame_x, frame_y, width, height, scale):
    img = pg.Surface((width,height)).convert_alpha()
    img.blit(sheet,(0,0),((frame_x * width), (frame_y * height), width, height))
    img = pg.transform.scale(img, (width*scale, height*scale))
    img.set_colorkey((0,0,0))
    return img
    
def random_rgood():
    global rgood_x, rgood_y, rgood_rect, player_score, rgood_counter
    
    if player_rect.colliderect(rgood_rect):
        rgood_x = random.randint(0, screen_width - rgood_img.get_width())
        rgood_y = random.randint(0, screen_height - rgood_img.get_height())
        rgood_rect = rgood_img.get_rect(midbottom=(rgood_x, rgood_y))
        player_score += 1
        rgood_counter += 1


def ggoodie_appearence():
    global ggood_rect, elapsed_time1, ggood_visibility, player_score, ggood_counter

    if elapsed_time1 > 3000:
        ggood_x = random.randint(0, screen_width - ggood_img.get_width())
        ggood_y = random.randint(0, screen_height - ggood_img.get_height())
        ggood_rect = ggood_img.get_rect(midbottom = (ggood_x, ggood_y))
        elapsed_time1 = 0
        ggood_visibility = True
    
    if elapsed_time1 > 2000 and ggood_visibility: 
        elapsed_time1 = 0
        ggood_visibility = False

    if ggood_visibility and player_rect.colliderect(ggood_rect):
        ggood_visibility = False
        elapsed_time1 = 0
        player_score += 100
        ggood_counter += 1

def ygoodie_mech():
    global elapsed_time2, ygood_visibility, ygood_rect, player_score


    random_time = random.randint(10000, 30000)
    if elapsed_time2 > random_time:
        ygood_x = random.randint(0, screen_width - ygood_img.get_width())
        ygood_y = random.randint(0, screen_height - ygood_img.get_height())
        ygood_rect = ygood_img.get_rect(midbottom = (ygood_x, ygood_y))
        elapsed_time2 = 0
        ygood_visibility = True

    if elapsed_time2 > 2000 and ygood_visibility: 
        elapsed_time2 = 0            
        ygood_visibility = False

    if ygood_visibility and player_rect.colliderect(ygood_rect):
        ygood_visibility = False
        elapsed_time2 = 0
        player_score += 1000
        
screen_height = 800
screen_width = 800

screen = pg.display.set_mode((screen_height, screen_width))


clock = pg.time.Clock()

elapsed_time = 0
elapsed_time1 = 0
elapsed_time2 = 0

running = True
#player
player_spritesheet = pg.image.load("assets/characters/player/snake_spritesheet.png").convert_alpha()
player_x = 150
player_y = 150

player_img_idle = image_cut(player_spritesheet, 0, 0 , 16, 16, 3)
player_img = player_img_idle
player_rect = player_img.get_rect(midbottom=(player_x, player_y))
player_speed = 8
#player_speed_diag = player_speed / math.sqrt(2)
player_score = 0


#red goodie
rgood_x = random.randint(0, (screen_width - 200))
rgood_y = random.randint(0, (screen_height - 100))

rgood_img = pg.image.load("assets/characters/goodies/red/rgoodie.png").convert_alpha()
rgood_rect = rgood_img.get_rect(midbottom = (rgood_x, rgood_y))
rgood_counter = 0

#green goodie

ggood_img = pg.image.load("assets/characters/goodies/green/ggoodie.png").convert_alpha()
ggood_visibility = False
ggood_counter = 0

#yellow goodie
ygood_img = pg.image.load("assets/characters/goodies/yellow/ygoodie.png")
ygood_visibility = False

#Fonts

font = pg.font.Font("assets/fonts/Jersey20-Regular.ttf", 24)
font_win = pg.font.Font("assets/fonts/Jacquard24-Regular.ttf", 120)




while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            exit()
    if player_score < 1000:
        key = pg.key.get_pressed()

        moved = False
        # W up
        if key[pg.K_w]:
            player_img = image_cut(player_spritesheet, 0, 2, 16, 16, 3)
            player_rect.top -= player_speed
            moved = True

        # S down
        if key[pg.K_s]:
            player_img = image_cut(player_spritesheet, 1, 0, 16, 16, 3)
            player_rect.bottom += player_speed
            moved = True

        # A left
        if key[pg.K_a]:
            player_img = image_cut(player_spritesheet, 0, 1, 16, 16, 3)
            player_rect.left -= player_speed
            moved = True

        # D right
        if key[pg.K_d]:
            player_img = image_cut(player_spritesheet, 1, 1, 16, 16, 3)
            player_rect.right += player_speed
            moved = True

#        # W A up left
#        if key[pg.K_w] and key[pg.K_a]:
#            player_img = image_cut(player_spritesheet, 0, 1, 16, 16, 3)
#            player_rect.left -= player_speed_diag
#            player_rect.top -= player_speed_diag
#            moved =  True
#   
#        # W D up right
#        if key[pg.K_w] and key[pg.K_d]:
#            player_img = image_cut(player_spritesheet, 1, 1, 16, 16, 3)
#            player_rect.top -= player_speed_diag
#            player_rect.right += player_speed_diag
#            moved = True
#   
#        # S A down left
#        if key[pg.K_s] and key[pg.K_a]:
#            player_img = image_cut(player_spritesheet, 0, 1, 16, 16, 3)
#            player_rect.bottom += player_speed_diag
#            player_rect.left -= player_speed_diag
#            moved = True
#   
#        # S D down right
#        if key[pg.K_s] and key[pg.K_d]:
#            player_img = image_cut(player_spritesheet, 1, 1, 16, 16, 3)
#            player_rect.right += player_speed_diag
#            player_rect.bottom += player_speed_diag
#            moved = True

        if not moved:
            player_img = player_img_idle


        if player_rect.left > screen_width:
            player_rect.right = 0
        if player_rect.right < 0:
            player_rect.left = screen_width

        if player_rect.top > screen_height:
            player_rect.bottom = 0
        if player_rect.bottom < 0:
            player_rect.top = screen_height

    player_x, player_y = player_rect.centerx, player_rect.centery

    elapsed_time += clock.get_time()
    elapsed_time1 += clock.get_time()
    elapsed_time2 += clock.get_time()

    if player_score < 1000:
        random_rgood()

        ggoodie_appearence()

        ygoodie_mech()
    
    
    screen.fill("white")

    text_score = font.render(f"Score: {player_score}", False, "#000000")
    text_X = font.render(f"X: {player_x}", False, "#000000")
    text_Y = font.render(f"Y: {player_y}", False, "#000000")
    text_time = font.render(f"time: {elapsed_time}", False, "#000000")
    text_rcounter = font.render(f"Red: {rgood_counter}", False,"#000000")
    text_gcounter = font.render(f"Green: {ggood_counter}", False,"#000000")
    text_win = font_win.render("!WIN!", False, "#000000")

    screen.blit(text_score, (screen_width-100, 10))
    screen.blit(text_X, (screen_width-100, 30))
    screen.blit(text_Y, (screen_width-100, 50))
    screen.blit(text_time, (screen_width-100, 70))
    screen.blit(text_rcounter, (screen_width-200, 10))
    screen.blit(text_gcounter, (screen_width-200, 30))

    screen.blit(player_img, player_rect)
    screen.blit(rgood_img, rgood_rect)

    if ggood_visibility:
        screen.blit(ggood_img, ggood_rect)

    if ygood_visibility:
        screen.blit(ygood_img, ygood_rect)

   
    if player_score >= 1000:
        player_img = image_cut(player_spritesheet, 1, 2, 16, 16, 6)
        screen.blit(text_win, (screen_width // 2 - 70 , 200))





    pg.display.update()

    clock.tick(60)



