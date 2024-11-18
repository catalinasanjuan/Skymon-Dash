import pygame
import sys

def main():
    pygame.init()

    # Configuración inicial de la ventana y del fondo
    ventana = pygame.display.set_mode((1472, 800))
    pygame.display.set_caption("avion desplazamiento")
    anchura_imagen = 1472
    imagen_fondo1 = pygame.transform.scale(pygame.image.load('fondopx.jpg'), (anchura_imagen, 800))
    imagen_fondo2 = pygame.transform.scale(pygame.image.load('fondopx.jpg'), (anchura_imagen, 800))
    pos_x1 = 0
    pos_x2 = anchura_imagen
    velocidad_fondo = -2  # Negativa para mover hacia la izquierda

    # Coordenadas y carga de imagen del avión
    xavion = 200
    yavion = 300
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

    xzapdospx = 150
    yzapdospx = 350
    
    xarticunopx = 100
    yarticunopx = 100
    
    xlugiapx = 500
    ylugiapx = 110
    
    xmegapinsirpx = 100
    ymegapinsirpx = 100
    # ... Agregar el resto de los pájaros aquí ...
# Cargar sonido de fondo
    pygame.mixer.init()
    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.play(-1)  # -1 para loop infinito
    reloj = pygame.time.Clock()

    corriendo = True
    while corriendo:
        reloj.tick(10)
        ##texto = (f'Speed {xavion} km/h', True, (0,255,0))
        # Mover y dibujar fondos
        pos_x1 += velocidad_fondo
        pos_x2 += velocidad_fondo
        if pos_x1 <= -anchura_imagen:
            pos_x1 = anchura_imagen
        if pos_x2 <= -anchura_imagen:
            pos_x2 = anchura_imagen
        ventana.blit(imagen_fondo1, (pos_x1, 0))
        ventana.blit(imagen_fondo2, (pos_x2, 0))

        # Dibujar el "avión"
        ventana.blit(avion, (xavion, yavion))

        # Dibujar pájaros y moverlos
        xmoltrespx -= 50
        xzapdospx -= 65
        xarticunopx -= 25
        xlugiapx -= 10  
        xmegapinsirpx -= 25
        
        if xmoltrespx < -50:
            xmoltrespx = 1472
        if xzapdospx < -50:
            xzapdospx = 1472
        if xarticunopx < -50:
            xarticunopx = 1472
        if xlugiapx < -50:  
            xlugiapx = 1472
        if xmegapinsirpx < -50:
            xmegapinsirpx = 1472
        ventana.blit(moltrespx, (xmoltrespx, ymoltrespx))
        ventana.blit(zapdospx, (xzapdospx, yzapdospx))
        ventana.blit(articunopx, (xarticunopx, yarticunopx))
        ventana.blit(lugiapx, (xlugiapx, ylugiapx)) 
        ventana.blit(megapinsirpx, (xmegapinsirpx, ymegapinsirpx))
        # ... Agregar el resto de los pájaros aquí ...

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                # Mover el "avión" con las teclas
                if tecla_presionada == "w":
                    yavion -= 80
                elif tecla_presionada == "a":
                    xavion -= 80
                elif tecla_presionada == "s":
                    yavion += 80
                elif tecla_presionada == "d":
                    xavion += 80
                elif tecla_presionada == "q":
                    corriendo = False
        pygame.display.flip()

    pygame.quit()
    sys.exit()

main()
