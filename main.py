import pygame, sys
import time
import math
from doplnok import scale_image, blit_rotate_center, blit_text_center
from button import Button

pygame.init()   #stihane všetky importované moduly pygame
pygame.display.set_caption("Menu")  #popis okna

BG = pygame.image.load("obrazky/menuBG.png")    #pozadie 

GRASS = scale_image(pygame.image.load("obrazky/grass.jpg"), 2.5)    #trava
TRACK = scale_image(pygame.image.load("obrazky/track3.png"), 0.9)   #trat

TRACK_BORDER = scale_image(pygame.image.load("obrazky/track-border3.1.png"), 0.9)   #okraje trate
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)  #vytvorenie masky z okrajov trate

FINISH = scale_image(pygame.image.load("obrazky/finish.png"), 0.77) #start/ciel
FINISH_MASK = pygame.mask.from_surface(FINISH)  #vytvorenie masky z startu/ciela
FINISH_POSITION = (140 , 250)   #pozicia startu/ciela

RED_CAR = scale_image(pygame.image.load("obrazky/red-car.png"), 0.55)   #esety jednotlivych aut
BLUE_CAR = scale_image(pygame.image.load("obrazky/blue-car.png"), 0.55)
MAGENTA_CAR = scale_image(pygame.image.load("obrazky/magenta-car.png"), 0.55)
GREY_CAR = scale_image(pygame.image.load("obrazky/grey-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("obrazky/green-car.png"), 0.55)
YELLOW_CAR = scale_image(pygame.image.load("obrazky/yellow-car.png"), 0.55)
KHAKI_CAR = scale_image(pygame.image.load("obrazky/khaki-car.png"), 0.55)

CARS = [RED_CAR , BLUE_CAR ,MAGENTA_CAR, GREY_CAR, GREEN_CAR, YELLOW_CAR, KHAKI_CAR]    #pole s asetmi aut

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()   #vyska/sirka okna
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  #pridelenie okna pod WIN
pygame.display.set_caption("CaRacing!") #nazov vytvoreneho okna

MAIN_FONT = pygame.font.SysFont("comicsans", 36) #pridelenie fontu na MAIN_FONT

GAME_MODE_1VPC = False  #urcenie hodnot pre konstanty
GAME_MODE_1V1 = False   #urcenie hodnot pre konstanty
OPTIONS = False #urcenie hodnot pre konstanty
GAME_MODE = False   #urcenie hodnot pre konstanty
clicked = False #urcenie hodnot pre premennu

FPS = 60    
PATH = [(173, 120), (101, 76), (54, 137), (55, 466), (317, 731), (404, 673), (412, 529), (499, 470), (599, 537),    
(616, 718), (735, 680), (731, 394), (610, 358), (428, 358), (468, 257), (693, 256), (697, 71), (539, 66), (315, 76), (254, 320), (253, 378), (162, 369),(178, 264)] #urcenie prejazdovych bodov pre PC auto

index1 = 0  #urcenie hodnot pre premennu(auta v menu)
index2 = 0  #urcenie hodnot pre premennu(auta v menu)

def get_font(size): #definicia na vyuzivany font
    return pygame.font.SysFont("comicsans", size)

def get_font2(size): #definicia na vyuzivany font
    return pygame.font.SysFont("impact", size)

def winner_1V1(): #definicia vytvarajuca okno vytaza/remizy v mode (1V1)
    global WINNER_BANNER_1V1
    global WINNER_MOUSE_POS_1V1
    
    WIN.fill("Palegreen")   #vyplnenie okna farbou
    WINNER_MOUSE_POS_1V1 = pygame.mouse.get_pos()   #sledovanie pozicie kurzorana 

    def pointComparison():  #definicia porovnavacia, zistuje ktore auto ma viac bodov
        global player_car1
        global player_car2
        
        if player_car1.points > player_car2.points:
            return "WINNER is Player1"
        elif player_car1.points < player_car2.points:
            return "WINNER is Player2"
        else:
            return "It`s DRAW"



    WINNER_BANNER_1V1 = Button (image=(scale_image(pygame.image.load("obrazky/universal_banner.png"), 0.92)), pos=(400,400),text_input= (f"{pointComparison()}!"), font=get_font2(60), base_color="Black", hovering_color="#005400")
    #Textura vyherneho okna

    for button in [WINNER_BANNER_1V1]: #for cyklus na zmenu farby + vykreslenie WIN aj s novym bannerom
        button.changeColor(WINNER_MOUSE_POS_1V1)
        button.update(WIN)
    pygame.display.update() #displej update
    pygame.time.wait(5000) #5 sekundova cakacka
    
def winner_1VPC():  #definicia vytvarajuca okno vytaza v mode (1VPC)
    global WINNER_BANNER_1VPC
    global WINNER_MOUSE_POS_1VPC

    WIN.fill("Palegreen")   #vyplnenie okna farbou

    WINNER_MOUSE_POS_1VPC = pygame.mouse.get_pos() #sledovanie pozicie kurzorana 

    WINNER_BANNER_1VPC = Button (image=(scale_image(pygame.image.load("obrazky/winner_1VPC.png"), 0.92)), pos=(400,400),text_input= " ", font=get_font2(60), base_color="Black", hovering_color="Green")
    #Textura vyherneho okna

    for button in [WINNER_BANNER_1VPC]: #for cyklus na zmenu farby + vykreslenie WIN aj s novym bannerom
        button.changeColor(WINNER_MOUSE_POS_1VPC)
        button.update(WIN)
    pygame.display.update() #displej update
    pygame.time.wait(5000) #5 sekundova cakacka

def lost_1VPC(): #definicia vytvarajuca okno prehry v mode (1VPC)
    global LOST_BANNER
    global LOST_MOUSE_POS

    WIN.fill("Red") #vyplnenie okna farbou

    LOST_MOUSE_POS = pygame.mouse.get_pos() #sledovanie pozicie kurzorana 

    LOST_BANNER = Button (image=(scale_image(pygame.image.load("obrazky/lost_1VPC.png"), 0.92)), pos=(400,400),text_input= " ", font=get_font2(60), base_color="Black", hovering_color="Green")
    #Textura okna prehry

    for button in [LOST_BANNER]: #for cyklus na zmenu farby + vykreslenie WIN aj s novym bannerom
        button.changeColor(LOST_MOUSE_POS)
        button.update(WIN)
    pygame.display.update() #displej update
    pygame.time.wait(5000) #5 sekundova cakacka

def options():  #definicia vytvarajuca options okno v menu
    global PLAYER_1_OPTIONS_LEFT_BUTTON
    global PLAYER_1_OPTIONS_RIGHT_BUTTON
    global PLAYER_2_OPTIONS_LEFT_BUTTON
    global PLAYER_2_OPTIONS_RIGHT_BUTTON
    global CARS
    global PLAYER_1
    global PLAYER_2
    global index1
    global index2
    global OPTIONS

    OPTIONS_MOUSE_POS = pygame.mouse.get_pos( )#sledovanie pozicie kurzorana

    WIN.fill("Palegreen")#vyplnenie okna farbou

    OPTIONS_TEXT = get_font(75).render("OPTIONS", True, "Black")#nastavenie textu do textoveho pola
    OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 100))#vytvorenie textoveho pola 
    WIN.blit(OPTIONS_TEXT, OPTIONS_RECT)#zobrazenie textoveho pola 


    OPTIONS_TAKE_CAR = Button(image=None, pos=(400, 750), text_input="TAKE IT", font=get_font(75), base_color="Black", hovering_color="Green")#tlacidlo na vzatie auta

    PLAYER_1 =  get_font(45).render("PLAYER1", True, "Black")#nastavenie textu do textoveho pola
    PLAYER_1_RECT = PLAYER_1.get_rect(center=(200, 170))#vytvorenie textoveho pola 
    WIN.blit(PLAYER_1, PLAYER_1_RECT)#zobrazenie textoveho pola 

    PLAYER_2 =  get_font(45).render("PLAYER2", True, "Black")#nastavenie textu do textoveho pola
    PLAYER_2_RECT = PLAYER_2.get_rect(center=(600, 170))#vytvorenie textoveho pola 
    WIN.blit(PLAYER_2, PLAYER_2_RECT)#zobrazenie textoveho pola 

    PLAYER_1_OPTIONS_LEFT_BUTTON = Button (image=(scale_image(pygame.image.load("obrazky/Options_Left_Rect.png"), 0.5)), pos=(100, 680),text_input=" ", font=get_font(15), base_color="Black", hovering_color="Green")
    PLAYER_1_OPTIONS_RIGHT_BUTTON = Button (image=(scale_image(pygame.image.load("obrazky/Options_Right_Rect.png"), 0.5)), pos=(300, 680),text_input=" ", font=get_font(15), base_color="Black", hovering_color="Green")
    PLAYER_2_OPTIONS_LEFT_BUTTON = Button (image=(scale_image(pygame.image.load("obrazky/Options_Left_Rect.png"), 0.5)), pos=(500, 680),text_input=" ", font=get_font(15), base_color="Black", hovering_color="Green")
    PLAYER_2_OPTIONS_RIGHT_BUTTON = Button (image=(scale_image(pygame.image.load("obrazky/Options_Right_Rect.png"), 0.5)), pos=(700, 680),text_input=" ", font=get_font(15), base_color="Black", hovering_color="Green")
    #vytvorenie tlacidiel
    OPTIONS_TAKE_CAR.changeColor(OPTIONS_MOUSE_POS)#zmena farby
    OPTIONS_TAKE_CAR.update(WIN)#update WIN

    for button in [PLAYER_1_OPTIONS_LEFT_BUTTON,PLAYER_1_OPTIONS_RIGHT_BUTTON,PLAYER_2_OPTIONS_LEFT_BUTTON,PLAYER_2_OPTIONS_RIGHT_BUTTON,OPTIONS_TAKE_CAR]: #for cyklus na zmenu farby + vykreslenie WIN aj s novym bannerom
        button.changeColor(OPTIONS_MOUSE_POS)
        button.update(WIN)

    WIN.blit(scale_image(CARS[index1], 10), (90,220))#vykreslenie pola aut v okne
    WIN.blit(scale_image(CARS[index2], 10), (490,220))#vykreslenie pola aut v okne

    for event in pygame.event.get(): #cyklus na vyber farby aut
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAYER_1_OPTIONS_LEFT_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                index1 -= 1 #zmenselie hodnoty indexu
                if index1 < 0: 
                    index1 = len(CARS)-1
                elif index1 > len(CARS)-1:  #oprava bugu (ostavas iba v cislach aut)
                    index1 = 0
            elif PLAYER_1_OPTIONS_RIGHT_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                index1 += 1 #zvacsenie hodnoty indexu
                if index1 < 0:
                    index1 = len(CARS)-1
                elif index1 > len(CARS)-1:  #oprava bugu (ostavas iba v cislach aut)
                    index1 = 0
            elif PLAYER_2_OPTIONS_LEFT_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                index2 -= 1 #zmenselie hodnoty indexu
                if index2 < 0:
                    index2 = len(CARS)-1
                elif index2 > len(CARS)-1:  #oprava bugu (ostavas iba v cislach aut)
                    index2 = 0
            elif PLAYER_2_OPTIONS_RIGHT_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                index2 += 1 #zvacsenie hodnoty indexu
                if index2 < 0:
                    index2 = len(CARS)-1
                elif index2 > len(CARS)-1:  #oprava bugu (ostavas iba v cislach aut)
                    index2 = 0
            if OPTIONS_TAKE_CAR.checkForInput(OPTIONS_MOUSE_POS):
                OPTIONS = False #potvrdenie a vypnutie vyberu aut
    pygame.display.update() #displej update

def game_mode():    #definicia vytvarajuca game_mode okno v menu
    global GAME_MODE_LEVEL_PICKER_LEFT
    global GAME_MODE_LEVEL_PICKER_RIGHT
    global GAME_MODE_LEVEL_PICKER_TABLE
    global GAME_MODE
    global GAME_MODE_1V1
    global GAME_MODE_1VPC
    global player_car1
    global player_car2
    global computer_car
    global game_info
    global clicked

    GAME_MODE_MOUSE_POS = pygame.mouse.get_pos() #sledovanie pozicie kurzorana

    WIN.fill("Palegreen") #vyplnenie okna farbou

    GAME_MODE_TEXT =  get_font(75).render("GAME MODE!", True, "Black")#nastavenie textu do textoveho pola
    GAME_MODE_TEXT_RECT = GAME_MODE_TEXT.get_rect(center=(400, 100))#vytvorenie textoveho pola 
    WIN.blit(GAME_MODE_TEXT, GAME_MODE_TEXT_RECT)#zobrazenie textoveho pola 

    GAME_MODE_LEVEL_PICKER_LEFT = Button (image=(scale_image(pygame.image.load("obrazky/Options_Left_Rect.png"), 0.5)), pos=(100, 350),text_input=" ", font=get_font(15), base_color="Black", hovering_color="Green")
    GAME_MODE_LEVEL_PICKER_RIGHT = Button (image=(scale_image(pygame.image.load("obrazky/Options_Right_Rect.png"), 0.5)), pos=(700, 350),text_input=" ", font=get_font(15), base_color="Black", hovering_color="Green")
    GAME_MODE_LEVEL_PICKER_TABLE = Button (image=(scale_image(pygame.image.load("obrazky/Play Rect.png"), 0.5)), pos=(400, 250),text_input= str(game_info.LEVELS), font=get_font(45), base_color="Black", hovering_color="Black")
    #vytvorenie tlacidiel a okna na zobrazenie textu

    GAME_MODE_BACK_BUTTON = Button(image=None, pos=(400, 750), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
    GAME_MODE_1V1_BUTTON = Button (image=(scale_image(pygame.image.load("obrazky/Play Rect.png"), 1.25)), pos=(400, 350),text_input="PLAYER vs PLAYER", font=get_font(45), base_color="Black", hovering_color="Green")
    GAME_MODE_1VPC_BUTTON = Button (image=(scale_image(pygame.image.load("obrazky/Play Rect.png"), 1.25)), pos=(400, 500),text_input="PLAYER vs PC", font=get_font(45), base_color="Black", hovering_color="Green")
    #vytvorenie tlacidiel

    for button in [GAME_MODE_BACK_BUTTON,GAME_MODE_1V1_BUTTON,GAME_MODE_1VPC_BUTTON,]: #for cyklus na zmenu farby + vykreslenie WIN aj s novym bannerom
        button.changeColor(GAME_MODE_MOUSE_POS)
        button.update(WIN)
    
    if clicked: #nastavenie zobrazenia tlacidiel a okna na zobrazenie textu
        for button in [GAME_MODE_LEVEL_PICKER_LEFT, GAME_MODE_LEVEL_PICKER_RIGHT, GAME_MODE_LEVEL_PICKER_TABLE]:
            button.changeColor(GAME_MODE_MOUSE_POS)
            button.update(WIN) #displej update

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if GAME_MODE_1V1_BUTTON.checkForInput(GAME_MODE_MOUSE_POS) and not clicked:
                clicked = True #premenna clicked ostava schovana
            elif GAME_MODE_1V1_BUTTON.checkForInput(GAME_MODE_MOUSE_POS) and clicked:
                GAME_MODE = False
                GAME_MODE_1V1 = True #spustenie modu 1V1
            elif GAME_MODE_1VPC_BUTTON.checkForInput(GAME_MODE_MOUSE_POS):
                GAME_MODE = False
                GAME_MODE_1VPC = True #spustenie modu 1VPC
            elif GAME_MODE_BACK_BUTTON.checkForInput(GAME_MODE_MOUSE_POS):
                GAME_MODE = False #vyskocenie z okna vyberu
            elif GAME_MODE_LEVEL_PICKER_LEFT.checkForInput(GAME_MODE_MOUSE_POS):
                if game_info.LEVELS > 1: #posuvanie sa v ciselnom textovom poli na pocet kol
                    game_info.LEVELS -= 1
            elif GAME_MODE_LEVEL_PICKER_RIGHT.checkForInput(GAME_MODE_MOUSE_POS):
                if game_info.LEVELS <= 9: #posuvanie sa v ciselnom textovom poli na pocet kol
                    game_info.LEVELS += 1

    pygame.display.update()#displej update

def main_menu():#definicia na vytvorenie samotneho menu
    global GAME_MODE
    global GAME_MODE_1V1
    global OPTIONS
    global player_car1
    global player_car2
    global computer_car
    WIN.blit(BG, (0, 0)) #nastavenie pozadia

    MENU_MOUSE_POS = pygame.mouse.get_pos() #sledovanie pozicie kurzorana 

    MENU_TEXT = get_font(100).render("CaRacing!", True, "#4ba814")#nastavenie textu do textoveho pola
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))#vytvorenie textoveho pola 

    PLAY_BUTTON = Button(image=pygame.image.load("obrazky/Options Rect.png"), pos=(400, 250), text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="#4ba814")
    OPTIONS_BUTTON = Button(image=pygame.image.load("obrazky/Options Rect.png"), pos=(400, 400), text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="#4ba814")
    QUIT_BUTTON = Button(image=pygame.image.load("obrazky/Options Rect.png"), pos=(400, 700), text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="#4ba814")
    #vytvorenie tlacidiel
    
    WIN.blit(MENU_TEXT, MENU_RECT)#zobrazenie textoveho pola 

    for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]: #for cyklus na zmenu farby + vykreslenie WIN aj s novym bannerom
        button.changeColor(MENU_MOUSE_POS)
        button.update(WIN)
    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT: #ukoncenie okna
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #vytvorenie logiky pre menu okno
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS): #tlacidlo PLAY
                player_car1 = PlayerCar(4, 4, CARS[index1],(150, 200)) #objekt player_car1(rychlost, farba, spawn)
                player_car2 = PlayerCar(4, 4, CARS[index2],(180, 200)) #objekt player_car2(rychlost, farba, spawn)
                computer_car = ComputerCar(2, 4, PATH, CARS[index2],(180, 200)) #objekt computer_car (rychlost, trasa, farba, spawn)
                GAME_MODE = True #spustenie okna GAME_MODE
            elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS): #tlacidlo OPTIONS
                OPTIONS = True #spustenie okna OPTIONS
            elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): #tlacidlo QUIT
                pygame.quit()
                sys.exit()

    pygame.display.update() #displej update

class GameInfo: #classa na ratanie levelov, kol, herneho casu
    LEVELS = 10 #pocet levelov

    def __init__(self, level=1): #definicia na urcenie casu v kole
        self.level = level
        self.started = False 
        self.level_start_time = 0 #pocita cas od nuly

    def next_level(self): #definicia na pocitanie levelov
        self.level += 1 #pridava vzdy o jeden level 
        self.started = False

    def reset(self): #definicia na reset udajov ingame
        self.level = 1  #hra zacne od levelu 1
        self.started = False
        self.level_start_time = 0 #hra spusti casovac od nula sekund

    def game_finished(self): #definicia na ukoncenie hry
        return self.level > self.LEVELS #konic(ked je odohratych viac ako zadanuch levelov)

    def start_level(self): #zacatie kola
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self):
        if not self.started: #ukoncenie pocitani po konci levelu
            return 0
        return round(time.time() - self.level_start_time) #vratenie udaju o skutocnom case


class AbstractCar: #classa na pohyb, vykreslovanie pohybu, otacanie, kolizie (vseobecne vlastnosti aut)
    
    def __init__(self, max_vel, rotation_vel, img, start_pos): 
        #definicia na rychlost auta, rychlost zatacania, vykreslenie auta, spravny spawn (pre vsetky auta)
        self.img = img #vykreslenie
        self.max_vel = max_vel # maximalna rychlost auta
        self.vel = 0 #(pociatocna) rychlost auta
        self.rotation_vel = rotation_vel #zatacania
        self.angle = 0 #(pociatocna) rychlost zatacania
        self.x, self.y = start_pos #spawn
        self.acceleration = 0.1 #velkost akceleracie (rozbehnutia)

    def rotate(self, left = False, right = False): #definicia na zatacanie auta
        if left:
            self.angle += self.rotation_vel #zvacsovanie uhlu rotacie
        elif right:
            self.angle -= self.rotation_vel #zmensovanie uhlu rotacie

    def draw(self, win): #definicia na vykreslenie a spravnu rotaciu obrazku
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
    
    def move_forward(self): #definicia na pohyb auta dopredu
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        #vzorec maximalnej rychlosti auta (rychlost + akceleracia = max)
        self.move()

    def move_backward(self): #definicia na cuvanie auta
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        #vzorec maximalnej rychlosti auta pri spiatocke 
        self.move()

    def move(self): # definicia na vytvorenie pohybu v jedenej, ale aj vo viacerych osiach(naraz)
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel #vzorec na vypocet verticalneho pohybu
        horizontal = math.sin(radians) * self.vel #vzorec na vypocet horizontalneho pohybu

        self.x -= horizontal
        self.y -= vertical

    def collide(self,mask, x=0, y=0): #definicia na vytvorenie koliznych casti obrazka (auta) 
        car_mask = pygame.mask.from_surface(self.img) #definovanie masky auta (dotykovych ploch)
        offset = (int(self.x - x),int(self.y - y)) #vypocet kolizii auta na x a y osi
        poi = mask.overlap(car_mask, offset) #vztvorenie koliznych casti auta 
        return poi

    def reset(self, start_pos): #definicia na respawn aut v spravnej polohe a yo spravnou rychlostou
        self.x, self.y = start_pos
        self.angle = 0
        self.vel = 0

    def __del__(self):  #definicia s destruktorom na odstranenie buggu zo zlym spawnom
        pass

class PlayerCar(AbstractCar): #classa potrebna pre hracovo auto(spomalenie auta, spetneho pohybu po naraze)
    points = 0 #pocet bodov v hre

    def reduce_speed(self): #definicia na postupne spomalenie auta
        self.vel = max(self.vel - self.acceleration /2 , 0)
        #vzorec na spomalenie auta
        self.move()

    def bounce(self): #definicia na vytvorenie spetneho pohybu po naraze
        self.vel = -self.vel
        #vzorec na vypocet spetneho pohybu po naraze
        self.move()

class ComputerCar(AbstractCar): #classa potrebna pre pohyb, vykreslovanie otacania, spravnej orientacie virtualneho auta na body prejazdu a spravne pridavanie rychlosti pre Computer car

    def __init__(self, max_vel, rotation_vel, path=[], img = CARS[index2], start_pos = (150,200)):
        #definicia na rychlost a max. rychlost Computer car, body prejazdu, spravne esety, startovacia pozicia
        super().__init__(max_vel, rotation_vel, img, start_pos) #dedenie parametrov
        self.img = self.img #obrazok
        self.path = path #body prejazdu
        self.current_point = 0 #zaciatocny body prejazdu
        self.vel = max_vel #rychlost a max. rychlost
        self.start_pos = start_pos #startovacia pozicia

    def draw_points(self): #definicia na vykreslovanie bodov prejazdu (potrebne na vyvoj)
        for point in self.path:
            pygame.draw.circle(WIN, (255, 0, 0), point, 5)
    
    def draw(self, win): #dedicne vykreslenie obrazkov
        super().draw(win)

    def calculate_angle(self):  #definicia na spravne vykreslenie otacania auta
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radian_angle = math.pi /2 #vzorce na vypocet spravneho otacania
        else:
            desired_radian_angle = math.atan(x_diff/y_diff) #vzorce na vypocet spravneho otacania

        if target_y > self.y:
            desired_radian_angle += math.pi #vzorce na vypocet spravneho otacania

        difference_in_angle = self.angle - math.degrees(desired_radian_angle) #sposoby otacania v polkruhoch
        if difference_in_angle >= 180:
            difference_in_angle -= 360

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_vel, abs(difference_in_angle)) #vzorce na vypocet spravneho otacania
        else:
            self.angle += min(self.rotation_vel, abs(difference_in_angle)) #vzorce na vypocet spravneho otacania


    def update_path_point(self): #definicia na updatovanie bodov prejazdu pre Computer car
        target = self.path[self.current_point] #definicia targetu auta
        rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height()) #vytvorenie rectangelu pre auto
        if rect.collidepoint(*target):
            self.current_point += 1 #navysovanie bodov prejazdu

    def move(self): #definicia na vytvorenie principu jazdy cez body prejazdu pre Computer car
        if self.current_point >= len(self.path):
            return
         
        self.calculate_angle() #povolanie spravneho vykreslenia otacania auta
        self.update_path_point() #povolanie updatovanie bodov prejazdu pre Computer car
        super().move()

    def next_level(self, level): #definicia noveho kola
        self.reset(self.start_pos) #resetovnaie startovacej pozicie pre auto
        self.vel = self.max_vel + (level - 1) * 0.2 #vytvorenie principu na zrychlovanie pre Computer car (kazdym kolom rychlejsie o 0.2 px/s)
        self.current_point = 0 #yaciatocny (prvy) prejazdovy bod pre Computer car

def draw(win, images, car1, car2, game_info): #vykreslenie udajov o danom kole na obrazovke
    global GAME_MODE_1V1

    for img, pos in images: #cyklus na vykreslenie udajov
        win.blit(img, pos)

    level_text = MAIN_FONT.render(f"Level: {game_info.level}", 1, (255,255,255))  #vykreslenie levelu 
    win.blit(level_text, (10, HEIGHT - level_text.get_height() - 70)) #vykreslenie a urcenie presnej polohy (ide o dynamicke udaje)

    time_text = MAIN_FONT.render(f"Time: {game_info.get_level_time()}s", 1, (255,255,255)) #vykreslenie casu
    win.blit(time_text, (10, HEIGHT - time_text.get_height() - 40)) #vykreslenie a urcenie presnej polohy (ide o dynamicke udaje)

    if not GAME_MODE_1V1:
        vel_text = MAIN_FONT.render(f"Speed: {round(player_car1.vel, 1)}px/s", 1, (255,255,255)) #vykreslenie rychlosti (1VPC) 
        win.blit(vel_text, (10, HEIGHT  - vel_text.get_height() - 10)) #vykreslenie a urcenie presnej polohy (ide o dynamicke udaje)

    if(GAME_MODE_1VPC): #vykreslenie aut (1VPC)
        car1.draw(win)
        car2.draw(win)
    else:
        car1.draw(win) #vykreslenie aut (1V1)
        car2.draw(win)
        
    pygame.display.update() #displej update

def move_player(): #definicia na ovladanie pohybu
    keys = pygame.key.get_pressed()
    moved = False

    if(GAME_MODE_1V1): #ovladanie W,A,S,D (1V1)
        if keys[pygame.K_a]:
            player_car1.rotate(left=True)
        if keys[pygame.K_d]:
            player_car1.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            player_car1.move_forward()
        if keys[pygame.K_s]:
            moved = True
            player_car1.move_backward()

        if not moved:
            player_car1.reduce_speed() #spomalovanie 
        
        if keys[pygame.K_LEFT]: #ovladanie sipkami (1V1)
            player_car2.rotate(left=True)
        if keys[pygame.K_RIGHT]:
            player_car2.rotate(right=True)
        if keys[pygame.K_UP]:
            moved = True
            player_car2.move_forward()
        if keys[pygame.K_DOWN]:
            moved = True
            player_car2.move_backward()

        if not moved:
            player_car2.reduce_speed() #spomalovanie 
    else:   #ovladanie W,A,S,D (1VPC)
        if keys[pygame.K_a]: 
            player_car1.rotate(left=True)
        if keys[pygame.K_d]:
            player_car1.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            player_car1.move_forward()
        if keys[pygame.K_s]:
            moved = True
            player_car1.move_backward()

        if not moved:
            player_car1.reduce_speed() #spomalovanie 
        

def handle_collision(game_info): #definicia na koliziu medzi drahou, cielovou paskou a autami(esetmi)
    global GAME_MODE_1VPC
    global GAME_MODE_1V1

    if(GAME_MODE_1VPC):
        if player_car1.collide(TRACK_BORDER_MASK) != None: #kolizia medzi autom a tratou
            player_car1.bounce()

        computer_finish_poi_collide = computer_car.collide(FINISH_MASK, *FINISH_POSITION) #kolizia medzi autom a cielovou paskou
        if computer_finish_poi_collide != None: #Computer car vyhra 
            game_info.reset() #reset game infa
            player_car1.reset((150, 200)) #reset hracovho auta
            computer_car.reset((180, 200)) #reset Computer car
            AbstractCar.__del__(computer_car) #odstranenie bugu s nehybnostou auta pomocou destruktora
            GAME_MODE_1VPC = False #ukoncenie modu 1VPC
            lost_1VPC() #otvorenie okna lost_1VPC

        player_finish_poi_collide = player_car1.collide(FINISH_MASK, *FINISH_POSITION)
        if player_finish_poi_collide != None:
            if player_finish_poi_collide[1] == 0:
                player_car1.bounce()
            else: #hrac prejde cez dany level
                game_info.next_level() #spusti sa dalsi level
                player_car1.reset((150, 200)) #reset hracovho auta
                computer_car.next_level(game_info.level) #reset a upgrade Computer car a game infa
    else:
        if player_car1.collide(TRACK_BORDER_MASK) != None: #kolizia medzi autom1 a tratou
            player_car1.bounce()

        player_finish_poi_collide = player_car1.collide(FINISH_MASK, *FINISH_POSITION) #kolizia medzi autom1 a cielovou paskou
        if player_finish_poi_collide != None:
            if player_finish_poi_collide[1] == 0:
                player_car1.bounce()
            else:
                game_info.next_level() #nove kolo
                player_car1.points += 1 #bod pre auto1
                #print(player_car1.points)
                #print(player_car2.points)
                #print(game_info.level)
                player_car1.reset((150, 200)) #reset aut
                player_car2.reset((180, 200)) #reset aut
            
        if player_car2.collide(TRACK_BORDER_MASK) != None: #kolizia medzi autom2 a tratou
            player_car2.bounce()

        player_finish_poi_collide = player_car2.collide(FINISH_MASK, *FINISH_POSITION) #kolizia medzi autom2 a cielovou paskou
        if player_finish_poi_collide != None:
            if player_finish_poi_collide[1] == 0:
                player_car2.bounce()
            else:
                game_info.next_level() #nove kolo
                player_car2.points += 1 #bod pre auto2
                #print(player_car1.points)
                #print(player_car2.points)
                #print(game_info.level)
                player_car1.reset((150, 200)) #reset aut
                player_car2.reset((180, 200)) #reset aut
   


run = True #definovanie hodnoty pre premennu
clock = pygame.time.Clock() #definovanie hodnoty premennej pre cas na trati
images = [(GRASS, (0, 0)), (TRACK, (0, 0)), (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))] #vykreslenie travy, trate, cielovej pasky, okrajov trate
game_info = GameInfo() 

while run: #cyklus na beh celej hry
    main_menu() #povolanie menu
    while OPTIONS: 
        options() #povolanie nastaveni
    while GAME_MODE:
        game_mode() #povolanei herneho modu
    while GAME_MODE_1VPC: #mod 1VPC
        clock.tick(FPS) #FPS limit
        draw(WIN, images, player_car1, computer_car, game_info) #vykreslenie, obrazkov, aut, hernych udajov
        while not game_info.started: 
            blit_text_center(WIN, MAIN_FONT, f"Press any button to start game level {game_info.level}!") #pred zacitkom hry nacitanie textu pre spravodlivy zaciatok
            pygame.display.update() #displej update
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #ukoncenie okna
                    pygame.quit()
                    break

                if event.type == pygame.KEYDOWN: #po stiknuti klavesy hra zacne
                    game_info.start_level()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #ukoncenie okna
                run = False
                break

        move_player() #povolanie definicie pre pohyb auta
        computer_car.move() #povolanie definicie pre pohyb Computer Car
        
        handle_collision(game_info) #povolanie definicie pre kolizie

        if game_info.game_finished(): #skoncenie hry / Hrac vyhra
            game_info.reset() #reset hernych udajov
            player_car1.reset((150, 200)) #reset auta1
            computer_car.reset((180, 200))#reset auta2
            winner_1VPC() #povolanie okna winner_1VPC
            GAME_MODE_1VPC = False #ukoncenie okna 

    while GAME_MODE_1V1: #mod 1V1
        clock.tick(FPS) #FPS limit
        draw(WIN, images, player_car1, player_car2, game_info) #vykreslenie, obrazkov, aut, hernych udajov
        while not game_info.started:
            blit_text_center(WIN, MAIN_FONT, f"Press any button to start game level {game_info.level}!") #pred zacitkom hry nacitanie textu pre spravodlivy zaciatok
            pygame.display.update() #displej update
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #ukoncenie okna
                    pygame.quit()
                    break

                if event.type == pygame.KEYDOWN: #po stiknuti klavesy hra zacne
                    game_info.start_level()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #ukoncenie okna
                run = False
                break

        move_player() #povolanie definicie pre pohyb aut
        
        handle_collision(game_info) #povolanie definicie pre kolizie

        if game_info.game_finished(): #skoncenie hry
            player_car1.reset((150, 200)) #reset auta1
            player_car2.reset((180, 200)) #reset auta2
            GAME_MODE_1V1 = False #ukoncenie okna 
            winner_1V1() #povolanie okna winner_1V1
            game_info.reset() #reset hernych udaov

pygame.quit() #ukoncenie programu
