import os, sys, time, pygame, random, math

os.system('cls')
pygame.init()

WHITE = [255,255,255]
BLACK = [0,0,0]

TitleFont= pygame.font.SysFont("helvetica", 70)  
WordFont=pygame.font.SysFont("helvetica", 50)
LetterFont=pygame.font.SysFont("helvetica",40)

WIDTH = 800 
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Asteroids")

Wbox = 30
dist = 10



def game_Init(message):  
    screen.fill(WHITE)
    text = WordFont.render(message, 1, BLACK)
    screen.blit(text,(200,100))

    rect1=pygame.Rect(150, 350, Wbox*2,Wbox*2)
    pygame.draw.rect(screen, BLACK, rect1, width=1)
    text = LetterFont.render("1", 1, BLACK)
    screen.blit(text, (160 , 350))

    rect2=pygame.Rect(550, 350, Wbox*2,Wbox*2)
    pygame.draw.rect(screen, BLACK, rect2, width=1)
    text = LetterFont.render("2", 1, BLACK)
    screen.blit(text, (560 , 350))
    
    rect3=pygame.Rect(150, 150, Wbox*2,Wbox*2)
    pygame.draw.rect(screen, BLACK, rect3, width=1)
    text = LetterFont.render("Exit", 1, BLACK)
    screen.blit(text, (160 , 160))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my= pygame.mouse.get_pos()
            if rect1.collidepoint((mx,my)):
                #call main function
                level1()
            if rect2.collidepoint((mx,my)):
                level2()
            if rect3.collidepoint((mx,my)):
                display_message("goodbye!!")
                pygame.quit()
                sys.exit()
        pygame.display.update() 

def display_message(message):
    pygame.time.delay(500)
    screen.fill(WHITE)
    text = WordFont.render(message, 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

def level1():
    display_message("You are in level 1")
def level2():
    display_message("You are in level 2")
def level3():
    display_message("you are in level 3")
def scores():
    display_message("score function")

while True:
    game_Init("Asteroids")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
