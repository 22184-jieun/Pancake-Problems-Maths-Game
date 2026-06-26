import pygame
import sys
import time

pygame.init()

x=0
clock = pygame.time.Clock()
delta_time = 0.1


header_font = pygame.font.Font('Assets/MonsterFriendFore.otf', size =20)
header_font_lrg = pygame.font.Font('Assets/MonsterFriendFore.otf', size =22)
header_font_XL = pygame.font.Font('Assets/MonsterFriendFore.otf', size =26)

sub_font_sml = pygame.font.Font('Assets/monoMMM_5.ttf',size =20)
sub_font = pygame.font.Font('Assets/monoMMM_5.ttf',size =24)
sub_font_lrg = pygame.font.Font('Assets/monoMMM_5.ttf',size =26)

filename = 'PancakeProblemsData.txt'
#Creating a screen / display and setting its size
screen = pygame.display.set_mode((1200,675))

#Setting display name to 'Maths Game'
pygame.display.set_caption('Pancake Problems - Maths Game')

#Changing the display's icon to icon.png
pygame.display.set_icon(pygame.image.load('Assets/icon.png').convert_alpha())

gingham = pygame.image.load('Assets/gingham4.png').convert_alpha()




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
        pygame.draw.rect(surface, self.colour, self.rect, border_radius=6)

        text_surface = sub_font_sml.render(self.text, True, (158, 109, 63))
        text_rect = text_surface.get_rect(center=self.rect.center)

        surface.blit(text_surface, text_rect)

class Homepage:
    def __init__(self):
        self.start_button = Buttons(800 ,220,280,50, "START",(230,188,140))
        self.leaderboard_button = Buttons(800,320,280,50, "LEADERBOARD",(230,188,140))
        self.quit_button = Buttons(800,420,280,50, "QUIT", (230,188,140))
        self.title = pygame.image.load('Assets/title@3x.png').convert_alpha()
        self.title = pygame.transform.scale(self.title,
                                       (int(self.title.get_width()/2.2),int(self.title.get_height()/2.2)))
    
    def draw(self, surface):
        surface.fill((255,237,203,255))
        screen.blit(gingham,(0,0))
        screen.blit(self.title,(50,20))

        pygame.draw.rect(screen,(209, 162, 109),(800 ,230,280,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(800,330,280,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(800,430,280,50),border_radius=12)
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
       

        self.girl_button = Buttons2(175,425,150,50, "Select?", (230,188,140))
        self.boy_button = Buttons2(520,425,150,50, "Select?", (230,188,140))
        self.cat_button = Buttons2(880,425,150,50, "Select?", (230,188,140))
        
        self.input_box = Inputbox(545, 580, 300, 50, "e.g. John", (255, 238, 207))
        self.back_button = Buttons(30,580,50,50, "B", (230,188,140))
        self.next_button = Buttons(1060,580,100,50, "Next", (230,188,140))
    
        self.chara_choice = ""
        self.warning_text = ""


        self.girl_icon = pygame.image.load('Assets/girlICON@3x.png').convert_alpha()
        self.girl_icon = pygame.transform.scale(self.girl_icon,(int(self.girl_icon.get_width()/6.5),int(self.girl_icon.get_height()/6.5)))
        

        self.boy_icon = pygame.image.load('Assets/boyICON@3x.png').convert_alpha()
        self.boy_icon = pygame.transform.scale(self.boy_icon, (int(self.boy_icon.get_width()/6.5),int(self.boy_icon.get_height()/6.5)))
        
        self.cat_icon = pygame.image.load('Assets/catICON@3x.png').convert_alpha()
        self.cat_icon = pygame.transform.scale(self.cat_icon, (int(self.cat_icon.get_width()/6.5),int(self.cat_icon.get_height()/6.5)))

        self.girl_icon_alt = pygame.image.load('Assets/girlICON_alt@3x.png').convert_alpha()
        self.girl_icon_alt = pygame.transform.scale(self.girl_icon_alt,(int(self.girl_icon_alt.get_width()/6.5),int(self.girl_icon_alt.get_height()/6.5)))

        self.boy_icon_alt = pygame.image.load('Assets/boyICON_alt@3x.png').convert_alpha()
        self.boy_icon_alt = pygame.transform.scale(self.boy_icon_alt,(int(self.boy_icon_alt.get_width()/6.5),int(self.boy_icon_alt.get_height()/6.5)))

        self.cat_icon_alt = pygame.image.load('Assets/catICON_alt@3x.png').convert_alpha()
        self.cat_icon_alt = pygame.transform.scale(self.cat_icon_alt,(int(self.cat_icon_alt.get_width()/6.5),int(self.cat_icon_alt.get_height()/6.5)))
        

    def draw(self, surface):
        surface.fill((255,237,203,255))
        screen.blit(gingham,(0,0))

        screen.blit(header_font_lrg.render('Choose a Character!', True, (158, 109, 63)), (415,40))
        screen.blit(header_font.render('Enter Name:',True,(158, 109, 63)), (320,600))
        screen.blit(sub_font_sml.render(self.warning_text,True,(158, 109, 63)),(450,520))

        pygame.draw.rect(screen,(209, 162, 109),(175,435,150,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(520,435,150,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(880,435,150,50),border_radius=12)

        pygame.draw.rect(screen,(230,188,140),(542, 577, 306, 56),border_radius=6)

       
        pygame.draw.rect(screen,(209, 162, 109),(30,590,50,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(1060,590,100,50),border_radius=12)

        
        self.girl_button.draw(surface)
        self.boy_button.draw(surface)
        self.cat_button.draw(surface)
        

        self.input_box.draw(screen)
        self.back_button.draw(surface)
        self.next_button.draw(surface)

        screen.blit(self.girl_icon,(105, 100)) 
        screen.blit(self.boy_icon,(450, 100)) 
        screen.blit(self.cat_icon,(810, 100))
        
        
        if self.chara_choice =="girl":
            self.boy_button.text = "Select?"
            self.cat_button.text = "Select?"
            self.girl_button.text = "Chosen!"
            screen.blit(self.boy_icon,(450, 100)) 
            screen.blit(self.cat_icon,(810, 100))
            screen.blit(self.girl_icon_alt,(103, 99)) 

        if self.chara_choice =="boy":
            self.girl_button.text = "Select?"
            self.cat_button.text = "Select?"
            self.boy_button.text = "Chosen!"
            screen.blit(self.girl_icon,(105, 100))  
            screen.blit(self.cat_icon,(810, 100))
            screen.blit(self.boy_icon_alt,(448, 99)) 
        
        if self.chara_choice =="cat":
            self.girl_button.text = "Select?"
            self.boy_button.text = "Select?"
            self.cat_button.text = "Chosen!"
            screen.blit(self.girl_icon,(105, 100)) 
            screen.blit(self.boy_icon,(450, 100)) 
            screen.blit(self.cat_icon_alt,(811, 100)) 
            

    def handle_event(self, event):
        if self.back_button.is_clicked(event):
            self.girl_button.text = "Select?"
            self.boy_button.text = "Select?"
            self.cat_button.text = "Select?"
            self.input_box.text = "Enter Name:"
            self.chara_choice = ""
            self.warning_text=""
            return "home"
        
        if self.girl_button.is_clicked(event):
            self.chara_choice ="girl"

        if self.boy_button.is_clicked(event):
            self.chara_choice ="boy"

        if self.cat_button.is_clicked(event):
            self.chara_choice ="cat"

        if self.next_button.is_clicked(event):

            if self.chara_choice == "":
                self.warning_text = "Please choose a character."

            elif self.input_box.text == "Eg: John":
                self.warning_text = "Please enter your name."

            elif self.input_box.text.strip() == "":
                self.warning_text = "Please enter your name."

            elif self.input_box.text.strip().isalpha() == False:
                self.warning_text = "Please use only alphabets."

            elif len(self.input_box.text.strip()) > 15:
                self.warning_text = "Please do not exceed 15 characters."
    
            else:
                with open(filename,"a") as f:
                    f.write(str(self.chara_choice)+"," +(str(self.input_box.text.strip().capitalize())))

                self.girl_button.text = "Select?"
                self.boy_button.text = "Select?"
                self.cat_button.text = "Select?"
                self.input_box.text = "e.g. John"
                self.chara_choice = ""
                self.warning_text=""

                return "concept"

        return None
    
#Mathematics concept selection page. Here the user can choose what maths concept they would like to play.
#The options include: 
class Concept_Select():
    def __init__(self):
        self.back_button = Buttons(30,580,50,50, "B", (230,188,140))
        self.next_button = Buttons(1060,580,100,50, "Next", (230,188,140))

        self.user_name = ""
        self.concept_choice=""
        self.warning_text=""

        self.addition_button = Buttons2(150,150,250,180, "Addition\n 1+2=3", (230,188,140))
        self.subtraction_button = Buttons2(475,150,250,180, "Subtraction\n   3-2=1", (230,188,140))
        self.multiplication_button = Buttons2(800,150,250,180, "Multiplication\n    2x2=4", (230,188,140))
        self.fractions_button = Buttons2(150,360,250,180, "  Fractions\n(1/2)+(1/2)=1", (230,188,140))
        self.exponents_button = Buttons2(475,360,250,180, "Exponents\n  2²=4", (230,188,140))
        self.algebra_button = Buttons2(800,360,250,180, "Algebra\n x+x=2x", (230,188,140))

        self.pipingbag1 = pygame.image.load('Assets/pipingbag_STRAWBERRY@3x.png').convert_alpha()
        self.pipingbag1 = pygame.transform.scale(self.pipingbag1,(int(self.pipingbag1.get_width()/7.5), int(self.pipingbag1.get_height()/7.5)))

        self.pipingbag2 = pygame.image.load('Assets/pipingbag_CHOCO@3x.png').convert_alpha()
        self.pipingbag2 = pygame.transform.scale(self.pipingbag2,(int(self.pipingbag2.get_width()/7.5), int(self.pipingbag2.get_height()/7.5)))

        self.pipingbag3 = pygame.image.load('Assets/pipingbag_LEMON@3x.png').convert_alpha()
        self.pipingbag3 = pygame.transform.scale(self.pipingbag3,(int(self.pipingbag3.get_width()/7.5), int(self.pipingbag3.get_height()/7.5)))

    
    def draw(self, surface):
        surface.fill((255,237,203,255))
        screen.blit(gingham,(0,0))

        welcome_surf=header_font_XL.render(f"Welcome, {self.user_name}!",True,(158, 109, 63))
        screen.blit(welcome_surf,(100,50))
        screen.blit(sub_font.render('Pick a maths concept~', True, (158, 109, 63)),((welcome_surf.get_width()+140) ,50))

        pygame.draw.rect(screen,(209, 162, 109),(30,590,50,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(1060,590,100,50),border_radius=12)

        pygame.draw.rect(screen,(209, 162, 109),(150,160,250,180),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(475,160,250,180),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(800,160,250,180),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(150,370,250,180),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(475,370,250,180),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(800,370,250,180),border_radius=12)

        self.back_button.draw(surface)
        self.next_button.draw(surface)

        self.addition_button.draw(surface)
        self.subtraction_button.draw(surface)
        self.multiplication_button.draw(surface)
        self.fractions_button.draw(surface)
        self.exponents_button.draw(surface)
        self.algebra_button.draw(surface)

        if self.concept_choice != "":
            screen.blit(sub_font_sml.render(f"You Selected: {self.concept_choice.capitalize()}", True, (158, 109, 63)),(450,580))

        screen.blit(sub_font_sml.render(self.warning_text, True, (158, 109, 63)),(450,620))

        screen.blit(self.pipingbag1,(200,300))
        screen.blit(self.pipingbag2,(530,300))
        screen.blit(self.pipingbag3,(850,300))


    def handle_event(self,event):

        if self.user_name == "":
            try: 
                with open(filename,"r") as f:
                    lines = f.readlines()
                    if lines:
                        #variable for latest line
                        last_record = lines[-1].strip()
                        #variables to print list values.
                        chara, name = last_record.strip().split(",")
                        self.user_name = name.capitalize()

            except FileNotFoundError:
                return "quit"
            
        if self.addition_button.is_clicked(event):
            self.concept_choice = "addition"
        
        if self.subtraction_button.is_clicked(event):
            self.concept_choice = "subtraction"
        
        if self.multiplication_button.is_clicked(event):
            self.concept_choice = "multiplication"
        
        if self.fractions_button.is_clicked(event):
            self.concept_choice = "fractions"
        
        if self.exponents_button.is_clicked(event):
            self.concept_choice = "exponents"

        if self.algebra_button.is_clicked(event):
            self.concept_choice = "algebra"


        if self.back_button.is_clicked(event):
            self.user_name=""
            self.concept_choice = ""
            self.warning_text = ""
            try:
                with open(filename,"r") as f:
                    lines = f.readlines()
                    if lines:
                        lines = lines[:-1]
                        with open(filename,"w") as f:
                            f.writelines(lines)
                            return "home"
            except FileNotFoundError:
                return "quit"
            
        if self.next_button.is_clicked(event):
            if self.concept_choice != "":
                with open(filename,"a") as f:
                    f.write(","+str(self.concept_choice))
                    return "difficulty"
            else:
                self.warning_text = "You have not selected a maths concept. Please choose one of the above."
        
        return None
    

class Difficulty_Select():

    def __init__(self):
        self.back_button = Buttons(30,580,50,50, "B", (230,188,140))
        self.play_button = Buttons(1060,580,100,50, "Play", (230,188,140))
        self.difficulty_choice = ""

        self.chara = ""
        self.easy_button = Buttons2(400,100,200,50,"Easy", (230,188,140))
        self.med_button = Buttons2(600,100,200,50,"Medium", (230,188,140))
        self.hard_button = Buttons2(800,100,200,50,"Hard", (230,188,140))
        
        self.chara_img = ""
        self.girl_sprite = pygame.image.load('Assets/girlspr_norm@3x.png').convert_alpha()
        self.girl_sprite = pygame.transform.scale(self.girl_sprite, (int(self.girl_sprite.get_width()/5),int(self.girl_sprite.get_height()/5)))

    def draw(self, surface):
        surface.fill((255,237,203,255))
        screen.blit(gingham,(0,0))

        

        self.easy_button.draw(surface)
        self.med_button.draw(surface)
        self.hard_button.draw(surface)

        if self.chara == "girl":
            screen.blit(self.girl_sprite,(0,400))

        
        pygame.draw.rect(screen,(209, 162, 109),(30,590,50,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(1060,590,100,50),border_radius=12)

        self.back_button.draw(surface)
        self.play_button.draw(surface)

    def handle_event(self, event):
        if self.easy_button.is_clicked(event):
            self.difficulty_choice = "easy"

        if self.med_button.is_clicked(event):
            self.difficulty_choice = "medium"
        
        if self.hard_button.is_clicked(event):
            self.difficulty_choice = "hard"

        if self.chara == "":
            try: 
                with open(filename,"r") as f:
                    lines = f.readlines()
                    if lines:
                        #variable for latest line
                        last_record = lines[-1].strip()
                        #variables to print list values.
                        chara, name, concept = last_record.strip().split(",")
                        self.chara = chara

            except FileNotFoundError:
                return "quit"

        if self.back_button.is_clicked(event):
            try:
                with open(filename,"r") as f:
                    lines = f.readlines()
                    if lines:
                        lines = lines[:-1]
                        with open(filename,"w") as f:
                            f.writelines(lines)
                            return "home"
            except FileNotFoundError:
                return "quit"
        return None
        
        
            
class Gameplay():
    def __init__(self):
        self.back_button = Buttons(30,580,50,50, "B", (230,188,140))
        

    def draw(self, surface):
        surface.fill((255,237,203,255))
        screen.blit(gingham,(0,0))

        pygame.draw.rect(screen,(209, 162, 109),(30,590,50,50),border_radius=12)
        pygame.draw.rect(screen,(209, 162, 109),(1060,590,100,50),border_radius=12)

        self.back_button.draw(surface)
        

    def handle_event(self, event):
        if self.back_button.is_clicked(event):
            try:
                with open(filename,"r") as f:
                    lines = f.readlines()
                    if lines:
                        lines = lines[:-1]
                        with open(filename,"w") as f:
                            f.writelines(lines)
                            return "home"
            except FileNotFoundError:
                return "quit"

class Leaderboard():
    def __init__(self):
        self.back_button = Buttons(1050,550,60,60, "B", (230,188,140))
        screen.blit(gingham,(0,0))

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
concept = Concept_Select()
difficulty = Difficulty_Select()
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
                if result:
                     current_screen = result
                

            elif current_screen == "leaderboard":
                result = leader.handle_event(event)
                if result == "home":
                     current_screen = "home"

            elif current_screen == "concept":
                result = concept.handle_event(event)
                if result:
                    current_screen = result
            
            elif current_screen == "difficulty":
                result = difficulty.handle_event(event)
                if result:
                    current_screen = result

    if current_screen =="home":
         homepage.draw(screen)

    if current_screen == "character_select":
        chara_select.draw(screen)

    if current_screen == "leaderboard":
        leader.draw(screen)

    if current_screen == "concept":
        concept.draw(screen)
    
    if current_screen == "difficulty":
        difficulty.draw(screen)

    pygame.display.flip()

    delta_time = clock.tick(60) / 1000
    delta_time =max(0.001,min(0.1, delta_time))

pygame.quit()