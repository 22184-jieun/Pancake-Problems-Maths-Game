import pygame
import time
import sys

#initialising pygame
pygame.init()

#Creating a screen / display and setting its size
screen = pygame.display.set_mode((1200,675))

#Setting display name to 'Maths Game'
pygame.display.set_caption('Maths Game')

#Changing the display's icon to icon.png
pygame.display.set_icon(pygame.image.load('icon.png').convert_alpha())

title = pygame.image.load('temptitle.png').convert_alpha()
title = pygame.transform.scale(title,
                               (title.get_width()/1.2,
                                title.get_height()/1.2))


header_font = pygame.font.Font('MonsterFriendFore.otf', size =20)
header_font_lrg = pygame.font.Font('MonsterFriendFore.otf', size =22)
sub_font = pygame.font.Font('monoMMM_5.ttf',size =24)

x=0
clock = pygame.time.Clock()
delta_time = 0.1

current_screen = "menu"     

running = True 
while running:
    
    
    x+= 50*delta_time 
    fill = pygame.Rect(0,0,1200,675)
    screen_fill = pygame.Surface((fill.width, fill.height), pygame.SRCALPHA)
    screen_col = (255,237,203,255)
    screen_fill.fill((255,237,203,255))
    
    

    screen.fill((255,237,203))
    
    screen.blit(title,(50, 70))

    #getting cursor position
    mpos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()


    #defining button coordinates and sizes
    start_button = pygame.Rect(800 ,200,280,50)
    Leaderboard = pygame.Rect(800,300,280,50)
    quit_button = pygame.Rect(800,400,280,50)

    text_col = (115,70,55)
    text = header_font.render('START', True, text_col,)
    
    text2 = header_font.render('LEADERBOARD', True, text_col)
    text3 = header_font.render('QUIT', True, text_col)

    text_xy = (890,220)
    text2_xy = (830,320)
    text3_xy = (900,420)


    #defining when cursor collides with 'buttons'
    m_collision = start_button.collidepoint(mpos)
    m_collision2 =Leaderboard.collidepoint(mpos)
    m_collision3 = quit_button.collidepoint(mpos)

    if m_collision == True:
        start_button = pygame.Rect(795,195, 290,60)
        text = header_font_lrg.render('START', True, text_col,)
        text_xy = (885,215)

    if m_collision2 == True:
        Leaderboard = pygame.Rect(795,295, 290,60)
        text2 = header_font_lrg.render('LEADERBOARD', True, text_col,)
        text2_xy = (825,315)

    if m_collision3 == True:
        quit_button = pygame.Rect(795,395, 290,60)
        text3 = header_font_lrg.render('QUIT', True, text_col,)
        text3_xy = (895,415)

    #creating the buttons on the screen
    pygame.draw.rect(screen,(209, 162, 109),(800 ,210,280,50),border_radius=12)
    pygame.draw.rect(screen,(209, 162, 109),(800,310,280,50),border_radius=12)
    pygame.draw.rect(screen,(209, 162, 109),(800,410,280,50),border_radius=12)

    button_col =(230,188,140)
    pygame.draw.rect(screen,button_col,start_button,border_radius=12)
    pygame.draw.rect(screen,button_col,Leaderboard,border_radius=12)
    pygame.draw.rect(screen,button_col,quit_button,border_radius=12)
    
    
    screen.blit(text,text_xy)
    screen.blit(text2,text2_xy)
    screen.blit(text3,text3_xy)


    if left_click[0] and m_collision:
        current_screen = "start_page"

    if left_click[0] and m_collision2:
        current_screen = "leaderboard_page"

    if left_click[0] and m_collision3:
        running = False

    if current_screen == "start_page":
        time.sleep(0.2)
        screen.blit(screen_fill, fill)

        pickchara = sub_font.render('Pick a Character!', True, text_col)
        screen.blit(pickchara,(500,50))

        girl_sprite = pygame.image.load('temp1.png').convert_alpha()
        girl_width =534
        girl_height =520
  
        girl_hitbox = pygame.Rect(200,200,girl_sprite.get_width()/3, girl_sprite.get_height()/3)
        
        
        girl_collis = girl_hitbox.collidepoint(mpos)

        if girl_collis == True:

            girl_width =584
            girl_height =570

        girl_sprite = pygame.transform.scale(girl_sprite,
                               (girl_width/3,
                                girl_height/3))
        
        screen.blit(girl_sprite,(200,200))


        boy_sprite = pygame.image.load('temp2.png').convert_alpha()
        boy_sprite = pygame.transform.scale(boy_sprite,
                               (boy_sprite.get_width()/3,
                                boy_sprite.get_height()/3))
        
        screen.blit(boy_sprite,(500,200))

        cat_sprite = pygame.image.load('temp3.png').convert_alpha()
        cat_sprite = pygame.transform.scale(cat_sprite,
                               (cat_sprite.get_width()/2.8,
                                cat_sprite.get_height()/2.8))
                                            
        screen.blit(cat_sprite,(800,230))

        #back button, checks for mouse click and collision with back button, sets background fill transparency to zero.
        back_button = pygame.Rect(1050,550,60,60)
        m_collision4 = back_button.collidepoint(mpos)

        if m_collision4 == True:
            back_button = pygame.Rect(1045,545,70,70)

        if left_click[0] and m_collision4:
            current_screen = 'menu'
        
        pygame.draw.rect(screen,button_col,back_button,border_radius=12)
        if current_screen == 'menu':
            screen_col = (255,237,203,0)


        



    if current_screen == "leaderboard_page":
        time.sleep(0.2)
        screen.fill((255,237,203))
        warning = sub_font.render('This page is not being worked on yet.', True, text_col)
        screen.blit(warning,(50,50))
        back_button = pygame.Rect(400,400,40,40)
        m_collision5 = back_button.collidepoint(mpos)
        if left_click[0] and m_collision5:
            current_screen = 'menu'
        
        pygame.draw.rect(screen,button_col,back_button)
        if current_screen == 'menu':
            time.sleep(0.1)
            screen_col = (255,237,203,0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #updates the screen, making the contents above visible.
    pygame.display.flip()
    delta_time = clock.tick(60) / 1000
    delta_time =max(0.001,min(0.1, delta_time))

pygame.quit()
sys.exit()
