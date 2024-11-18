import pygame
import sys

def main():
    pygame.init()
    
    ventana = pygame.display.set_mode((1472, 800))
    
    anchura_imagen = 1472
    imagen_fondo1 = pygame.transform.scale(pygame.image.load('fondo.jpg'), (anchura_imagen, 800))
    imagen_fondo2 = pygame.transform.scale(pygame.image.load('fondo 2.jpg'), (anchura_imagen, 800))
    
    pos_x1 = 0
    pos_x2 = anchura_imagen
    velocidad_fondo = -2  # Negativa para mover hacia la izquierda
    
    # Cargar las imágenes de los pájaros
  
    moltres = pygame.image.load('moltres.png')
    moltres = pygame.transform.scale(moltres, (158,158))
    
    zapdos = pygame.image.load('zapdos.png')
    zapdos = pygame.transform.scale(zapdos, (127,127))

    hoOh = pygame.image.load('hoOh.png')
    hoOh = pygame.transform.scale(hoOh, (300,300))
    
    articuno = pygame.image.load('articuno.png')
    articuno = pygame.transform.scale(articuno, (134,134))
    
    # Posiciones iniciales para los pájaros
    xmoltres = 400
    ymoltres = 600

    xzapdos = 150
    yzapdos = 350

    xhoOh = 500
    yhoOh = 100
    
    xarticuno = 100
    yarticuno = 100
    
    reloj = pygame.time.Clock()
    
    corriendo = True
    while corriendo:
        reloj.tick(15)
        
        ventana.fill((0, 0, 0))
        
        # Actualizar y dibujar fondos
        pos_x1 += velocidad_fondo
        pos_x2 += velocidad_fondo
        if pos_x1 <= -anchura_imagen:
            pos_x1 = anchura_imagen
        if pos_x2 <= -anchura_imagen:
            pos_x2 = anchura_imagen
        ventana.blit(imagen_fondo1, (pos_x1, 0))
        ventana.blit(imagen_fondo2, (pos_x2, 0))
        
        # Mover los pájaros
        xmoltres -= 50
        xzapdos -= 65
        xhoOh -= 10
        xarticuno -= 25

        if xmoltres < -50:
            xmoltres = 1472
        if xzapdos < -50:
            xzapdos = 1472
        if xhoOh < -50:
            xhoOh = 1472
        if xarticuno < -50:
            xarticuno = 1472
        
        # Dibujamos las imágenes de los pájaros
        ventana.blit(moltres, (xmoltres, ymoltres))
        ventana.blit(zapdos, (xzapdos, yzapdos))
        ventana.blit(hoOh, (xhoOh, yhoOh))
        ventana.blit(articuno, (xarticuno, yarticuno))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

main()
