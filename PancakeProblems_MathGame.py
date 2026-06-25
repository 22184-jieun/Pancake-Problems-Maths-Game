import pygame
import sys
import time

pygame.init()

x=0
clock = pygame.time.Clock()
delta_time = 0.1

header_font = pygame.font.Font('Assets/MonsterFriendFore.otf', size =20)
header_font_lrg = pygame.font.Font('Assets/MonsterFriendFore.otf', size =22)
sub_font = pygame.font.Font('Assets/monoMMM_5.ttf',size =24)
sub_font_lrg = pygame.font.Font('Assets/monoMMM_5.ttf',size =26)

#Creating a screen / display and setting its size
screen = pygame.display.set_mode((1200,675))

#Setting display name to 'Maths Game'
pygame.display.set_caption('Maths Game')

#Changing the display's icon to icon.png
pygame.display.set_icon(pygame.image.load('Assets/icon.png').convert_alpha())



class Buttons():
    def __init__(self, x, y, width, height, text, colour):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.colour = colour
            
        

    def draw(self, surface): 
        
        x = self.rect.x
        y = self.rect.y
        width = self.rect.width
        height = self.rect.height

        mpos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mpos) == True:
            
            width += 10
            height += 10 
            x -= 5
            y -= 5

        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(surface, self.colour, button_rect, border_radius=12)
        if  self.rect.collidepoint(mpos) == True:
            text_surface = header_font_lrg.render(self.text, True, (115,70,55))
        else:
            text_surface = header_font.render(self.text, True, (115,70,55))
        
        text_rect = text_surface.get_rect(center=button_rect.center)

        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class Buttons2():
    def __init__(self, x, y, width, height, text, colour):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.colour = colour
            
        

    def draw(self, surface): 
        
        x = self.rect.x
        y = self.rect.y
        width = self.rect.width
        height = self.rect.height

        mpos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mpos) == True:
            
            width += 10
            height += 10 
            x -= 5
            y -= 5

        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(surface, self.colour, button_rect, border_radius=12)
        if  self.rect.collidepoint(mpos) == True:
            text_surface = sub_font_lrg.render(self.text, True, (115,70,55))
        else:
            text_surface = sub_font.render(self.text, True, (115,70,55))
        
        text_rect = text_surface.get_rect(center=button_rect.center)

        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
    
class Inputbox:
    def __init__(self, x, y, width, height, text, colour):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.colour = colour
        self.active = False

    def userinput(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            if self.active:
                self.text = ""

        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect, border_radius=12)

        text_surface = sub_font.render(self.text, True, (115, 70, 55))
        text_rect = text_surface.get_rect(center=self.rect.center)

        surface.blit(text_surface, text_rect)

class Homepage:
    def __init__(self):
        self.start_button = Buttons(800 ,200,280,50, "START",(230,188,140))
        self.leaderboard_button = Buttons(800,300,280,50, "LEADERBOARD",(230,188,140))
        self.quit_button = Buttons(800,400,280,50, "QUIT", (230,188,140))
        self.title = pygame.image.load('Assets/title@3x.png').convert_alpha()
        self.title = pygame.transform.scale(self.title,
                                       (int(self.title.get_width()/2.2),int(self.title.get_height()/2.2)))
    
    def draw(self, surface):
        surface.fill((255,237,203,255))

        
        screen.blit(self.title,(30, 20))

        pygame.draw.rect(screen,(209, 162, 109),(800 ,210,280,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(800,310,280,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(800,410,280,50),border_radius=12)
        self.start_button.draw(surface)
        self.leaderboard_button.draw(surface)
        self.quit_button.draw(surface)

    def handle_event(self, event):
         if self.start_button.is_clicked(event):
              return "character_select"
         if self.leaderboard_button.is_clicked(event):
              return "leaderboard"
         if self.quit_button.is_clicked(event):
              return "quit"
         return None
    
class Chara_Select():
    def __init__(self):
       

        self.girl_button = Buttons2(170,425,150,50, "Select?", (230,188,140))
        self.boy_button = Buttons2(520,425,150,50, "Select?", (230,188,140))
        self.cat_button = Buttons2(870,425,150,50, "Select?", (230,188,140))
        
        self.input_box = Inputbox(445, 580, 300, 50, "Enter Name:", (230,188,140))
        self.back_button = Buttons(30,580,50,50, "B", (230,188,140))
        self.next_button = Buttons(1060,580,100,50, "Next", (230,188,140))
    
        self.chara_choice = ""

        self.girl_icon = pygame.image.load('Assets/girlICON@3x.png')
        self.girl_icon = pygame.transform.scale(self.girl_icon,(int(self.girl_icon.get_width()/6.5),int(self.girl_icon.get_height()/6.5)))
        

        self.boy_icon = pygame.image.load('Assets/boyICON@3x.png')
        self.boy_icon = pygame.transform.scale(self.boy_icon, (int(self.boy_icon.get_width()/6.5),int(self.boy_icon.get_height()/6.5)))
        
        self.cat_icon = pygame.image.load('Assets/catICON@3x.png')
        self.cat_icon = pygame.transform.scale(self.cat_icon, (int(self.cat_icon.get_width()/6.5),int(self.cat_icon.get_height()/6.5)))

        self.girl_icon_alt = pygame.image.load('Assets/girlICON_alt@3x.png')
        self.girl_icon_alt = pygame.transform.scale(self.girl_icon_alt,(int(self.girl_icon_alt.get_width()/6.5),int(self.girl_icon_alt.get_height()/6.5)))

        self.boy_icon_alt = pygame.image.load('Assets/boyICON_alt@3x.png')
        self.boy_icon_alt = pygame.transform.scale(self.boy_icon_alt,(int(self.boy_icon_alt.get_width()/6.5),int(self.boy_icon_alt.get_height()/6.5)))

        self.cat_icon_alt = pygame.image.load('Assets/catICON_alt@3x.png')
        self.cat_icon_alt = pygame.transform.scale(self.cat_icon_alt,(int(self.cat_icon_alt.get_width()/6.5),int(self.cat_icon_alt.get_height()/6.5)))
        

    def draw(self, surface):
        surface.fill((255,237,203,255))

        screen.blit(header_font_lrg.render('Choose a Character!', True, (196, 126, 77)), (410,40))

        pygame.draw.rect(screen,(209, 162, 109),(30,590,50,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(170,435,150,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(520,435,150,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(870,435,150,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(1060,590,100,50),border_radius=12)

        
        self.girl_button.draw(surface)
        self.boy_button.draw(surface)
        self.cat_button.draw(surface)
        

        self.input_box.draw(screen)
        self.back_button.draw(surface)
        self.next_button.draw(surface)

        screen.blit(self.girl_icon,(100, 100)) 
        screen.blit(self.boy_icon,(450, 100)) 
        screen.blit(self.cat_icon,(800, 100))

        
        if self.chara_choice =="girl":

            self.boy_button.text = "Select?"
            self.cat_button.text = "Select?"
            self.girl_button.text = "Chosen!"
            screen.blit(self.boy_icon,(450, 100)) 
            screen.blit(self.cat_icon,(800, 100))
            screen.blit(self.girl_icon_alt,(98, 99)) 

        if self.chara_choice =="boy":
            self.girl_button.text = "Select?"
            self.cat_button.text = "Select?"
            self.boy_button.text = "Chosen!"
            screen.blit(self.girl_icon,(100, 100))  
            screen.blit(self.cat_icon,(800, 100))
            screen.blit(self.boy_icon_alt,(448, 99)) 
        
        if self.chara_choice =="cat":
            self.girl_button.text = "Select?"
            self.boy_button.text = "Select?"
            self.cat_button.text = "Chosen!"
            screen.blit(self.girl_icon,(100, 100)) 
            screen.blit(self.boy_icon,(450, 100)) 
            screen.blit(self.cat_icon_alt,(801, 100)) 
            

    def handle_event(self, event):
        if self.back_button.is_clicked(event):
            self.girl_button.text = "Select?"
            self.boy_button.text = "Select?"
            self.cat_button.text = "Select?"
            self.input_box.text = "Enter Name:"
            self.chara_choice = ""
            return "home"
        if self.girl_button.is_clicked(event):
            self.chara_choice ="girl"

        if self.boy_button.is_clicked(event):
            self.chara_choice ="boy"

        if self.cat_button.is_clicked(event):
            self.chara_choice ="cat"
        return None
    
class Leaderboard():
    def __init__(self):
        self.back_button = Buttons(1050,550,60,60, "B", (230,188,140))

    def draw(self, surface):
        surface.fill((255,237,203,255))
        pygame.draw.rect(screen,(209, 162, 109),(1050,560,60,60),border_radius=12)
        self.back_button.draw(surface)

    def handle_event(self, event):
         if self.back_button.is_clicked(event):
              return "home"
         return None
        


current_screen = "home"
homepage = Homepage()
chara_select =Chara_Select()
leader = Leaderboard()
running = True 
while running:
    for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if current_screen == "home":
                result = homepage.handle_event(event)
                if result == "quit":
                     running = False
                elif result:
                     current_screen = result
            
            elif current_screen == "character_select":
                chara_select.input_box.userinput(event)
                result = chara_select.handle_event(event)
                if result == "home":
                     current_screen = "home"

            elif current_screen == "leaderboard":
                result = leader.handle_event(event)
                if result == "home":
                     current_screen = "home"

    if current_screen =="home":
         homepage.draw(screen)

    if current_screen == "character_select":
        chara_select.draw(screen)

    if current_screen == "leaderboard":
        leader.draw(screen)

    

    pygame.display.flip()

    delta_time = clock.tick(60) / 1000
    delta_time =max(0.001,min(0.1, delta_time))

pygame.quit()
