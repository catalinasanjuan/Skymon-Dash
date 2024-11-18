import pygame
import sys

def main():
    pygame.init()

    ventana = pygame.display.set_mode((1472, 800))
    pygame.display.set_caption("avion desplazamiento")

    anchura_imagen = 1472
    imagen_fondo1 = pygame.transform.scale(pygame.image.load('fondopx.jpg'), (anchura_imagen, 800))
    imagen_fondo2 = pygame.transform.scale(pygame.image.load('fondopx.jpg'), (anchura_imagen, 800))
    pos_x1 = 0
    pos_x2 = anchura_imagen
    velocidad_fondo = -2  # Negativa para mover hacia la izquierda
    # Coordenadas y carga de imagen del avión
    xavion = 10
    yavion = 400
    avion = pygame.image.load('avion.png')  # Reemplaza con la ruta de tu imagen
    avion = pygame.transform.scale(avion, (100, 100))

    # Cargar imágenes de los pájaros y posiciones iniciales
    # (Aquí agregarás todos los pájaros y sus respectivas inicializaciones)

    moltrespx = pygame.image.load('moltrespx.png')
    moltrespx = pygame.transform.scale(moltrespx, (158,158))
    
    zapdospx = pygame.image.load('zapdospx.png')
    zapdospx = pygame.transform.scale(zapdospx, (127,127))
    
    articunopx = pygame.image.load('articuno.png')
    articunopx = pygame.transform.scale(articunopx, (134,134))

    lugiapx = pygame.image.load('lugiapx.png')
    lugiapx = pygame.transform.scale(lugiapx, (300,300))
   
    megapinsirpx = pygame.image.load('megapinsirpx.png')
    megapinsirpx = pygame.transform.scale(megapinsirpx, (134,134)) 
    
    xmoltrespx = 400
    ymoltrespx = 600

    xzapdospx = 600
    yzapdospx = 600
    
    xarticunopx = 100
    yarticunopx = 100
    
    xlugiapx = 200
    ylugiapx = 100
    
    xmegapinsirpx = 100
    ymegapinsirpx = 100
    
    reloj = pygame.time.Clock()
    font = pygame.font.SysFont(None, 74)
    game_over = False

    while True:
        ventana.fill((0, 0, 0))
        
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                if tecla_presionada == "w":
                    yavion -= 80
                elif tecla_presionada == "a":
                    xavion -= 80
                elif tecla_presionada == "s":
                    yavion += 80
                elif tecla_presionada == "d":
                    xavion += 80

        # Mover fondos
        pos_x1 += velocidad_fondo
        pos_x2 += velocidad_fondo
        if pos_x1 <= -anchura_imagen:
            pos_x1 = anchura_imagen
        if pos_x2 <= -anchura_imagen:
            pos_x2 = anchura_imagen

        # Mover pájaros
        xmoltrespx -= 20
        xzapdospx -= 65
        xarticunopx -= 15
        xlugiapx -= 10
        xmegapinsirpx -= 5

        # Si los pájaros salen de la pantalla, resetear su posición
        if xmoltrespx < -50: xmoltrespx = 1472
        if xzapdospx < -50: xzapdospx = 1472
        if xarticunopx < -50: xarticunopx = 1472
        if xlugiapx < -50: xlugiapx = 1472
        if xmegapinsirpx < -50: xmegapinsirpx = 1472

        # Dibujar fondos
        ventana.blit(imagen_fondo1, (pos_x1, 0))
        ventana.blit(imagen_fondo2, (pos_x2, 0))
        
        # Dibujar avión y pájaros
        ventana.blit(avion, (xavion, yavion))
        ventana.blit(moltrespx, (xmoltrespx, ymoltrespx))
        ventana.blit(zapdospx, (xzapdospx, yzapdospx))
        ventana.blit(articunopx, (xarticunopx, yarticunopx))
        ventana.blit(lugiapx, (xlugiapx, ylugiapx))
        ventana.blit(megapinsirpx, (xmegapinsirpx, ymegapinsirpx))

        # Detección de colisiones
        avion_rect = avion.get_rect(topleft=(xavion, yavion))
        avion_rect = avion.get_rect(topleft=(xavion, yavion))
        moltrespx_rect = moltrespx.get_rect(topleft=(xmoltrespx, ymoltrespx))
        zapdospx_rect = zapdospx.get_rect(topleft=(xzapdospx, yzapdospx))
        articunopx_rect = articunopx.get_rect(topleft=(xarticunopx, yarticunopx))
        lugiapx_rect = lugiapx.get_rect(topleft=(xlugiapx, ylugiapx))
        megapinsirpx_rect = megapinsirpx.get_rect(topleft=(xmegapinsirpx, ymegapinsirpx))

# Comprobamos cada colisión por separado para identificar qué pájaro está colisionando
        if avion_rect.colliderect(moltrespx_rect):
            game_over = True
            print("Colisión detectada con Moltres!")
        elif avion_rect.colliderect(zapdospx_rect):
            game_over = True
            print("Colisión detectada con Zapdos!")
        elif avion_rect.colliderect(articunopx_rect):
            game_over = True
            print("Colisión detectada con Articuno!")
        elif avion_rect.colliderect(lugiapx_rect):
            game_over = True
            print("Colisión detectada con Lugia!")
        elif avion_rect.colliderect(megapinsirpx_rect):
            game_over = True
            print("Colisión detectada con Mega Pinsir!")

        if (avion_rect.colliderect(moltrespx_rect) or 
            avion_rect.colliderect(zapdospx_rect) or
            avion_rect.colliderect(articunopx_rect) or
            avion_rect.colliderect(lugiapx_rect) or
            avion_rect.colliderect(megapinsirpx_rect)):
            game_over = True
            print("Colisión detectada!")  # <-- código de depuración


        # Si el juego ha terminado
        if game_over:
            text = font.render("Game Over", True, (255, 0, 0))
            ventana.blit(text, (600, 350))

        pygame.display.flip()

main()
