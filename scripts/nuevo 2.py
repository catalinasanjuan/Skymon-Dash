import pygame 

WINDOW_SIZE =(800,600)
pygame.init()
pygame.display.set_caption("POS")
ventana = pygame.display.set_mode((800,600))
background=pygame.Surface ((800,600))
background.fill(pygame.Color('#090909'))

rectangulo=pygame.rect(10,10,150)

running=True
while(running):
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            running =False
        if (event.type==pygame.MOUSEBUTTONDOWN):
            pass
    pygame.draw.rect(ventana,'#A0A0A0',rectangulo)
    ventana.blit(background,(0,0))
    pygame.display.update()
    
