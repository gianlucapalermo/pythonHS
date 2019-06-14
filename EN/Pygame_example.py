import pygame
import time

pygame.init()

dimensioniSchermoX = 400
dimensioniSchermoY = 300

schermoDiGioco = pygame.display.set_mode((dimensioniSchermoX,dimensioniSchermoY))
pygame.display.set_caption("Test Game")

giocoAttivo = True
clock = pygame.time.Clock()

#nero in RGB
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)


while (giocoAttivo==True):
    
    pygame.draw.circle(schermoDiGioco, red, (240,60), 30)
    pygame.draw.rect(schermoDiGioco, green, [100, 150, 50, 35], 2)

    #Identificazione di eventi
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            giocoAttivo = False

    pygame.display.update()
    #Limita il massimo Frame Rate al secondo
    clock.tick(50)

pygame.quit()

