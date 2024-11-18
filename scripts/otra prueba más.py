import pygame
import sys

def main():
    pygame.init()

    # Creación de la ventana del juego y del fondo
    ventana = pygame.display.set_mode((1472, 800))
    pygame.display.set_caption("SkyMon Dash") #Nombre deljuego
    anchura_imagen = 1472
    imagen_fondo1 = pygame.transform.scale(pygame.image.load('fondopx.jpg'), (anchura_imagen, 800))
    imagen_fondo2 = pygame.transform.scale(pygame.image.load('fondopx.jpg'), (anchura_imagen, 800))
    pos_x1 = 0
    pos_x2 = anchura_imagen
    velocidad_fondo = -2  # Negativa para mover hacia la izquierda el fondo

    # Coordenadas de ubicación de la imagen del avión
    xavion = 10
    yavion = 405
    avion = pygame.image.load('avion.png') 
    avion = pygame.transform.scale(avion, (70, 70))

    # Imágenes de los Pokemón´s  
    moltrespx = pygame.image.load('moltrespx.png')
    moltrespx = pygame.transform.scale(moltrespx, (150,150))
    
    zapdospx = pygame.image.load('zapdospx.png')
    zapdospx = pygame.transform.scale(zapdospx, (110,110))
    
    articunopx = pygame.image.load('articuno.png')
    articunopx = pygame.transform.scale(articunopx, (120,120))

    lugiapx = pygame.image.load('lugiapx.png')
    lugiapx = pygame.transform.scale(lugiapx, (370,370))
   
    megapinsirpx = pygame.image.load('megapinsirpx.png')
    megapinsirpx = pygame.transform.scale(megapinsirpx, (100,100)) 
    
    # Posiciones iniciales para los Pokemón´s
    
    #xmoltrespx = 400
    xmoltrespx = 1000
    #ymoltrespx = 400
    ymoltrespx = 505

    #xzapdospx = 150
    #yzapdospx = 350
    xzapdospx = 600
    yzapdospx = 660
    #yzapdospx = 600
    
    xarticunopx = 600
    yarticunopx = 660
    
    #xlugiapx = 500
    #ylugiapx = 100
    xlugiapx = 200
    ylugiapx = 30
    
    xmegapinsirpx = 100
    ymegapinsirpx = 100
   
    reloj = pygame.time.Clock()
    font = pygame.font.SysFont(None, 74)
    game_over = False
    score = 0

# Agrego sonido de fondo, PD = es la cancion del Furret que camina jajajaja
    pygame.mixer.init()
    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.play(-1)  # -1 para loop infinito

    corriendo = True
    while corriendo:
        reloj.tick(10)
        score += 1  # Incrementar el puntaje
        
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

        # Pokemones y sus velocidades
        xlugiapx -= 40  #+10 veces más rapido que megapinsir
        #xlugiapx -= 10 
        xmegapinsirpx -= 30 #+5 veces más rapido que zapdos
        #xmegapinsirpx -= 25
        xzapdospx -= 25 #+10 veces más rapido que moltres
        #xzapdospx -= 85
        xmoltrespx -= 15 #+5 veces más rapido que articuno
        #xmoltrespx -= 20
        xarticunopx -= 10
        #xarticunopx -= 25 
 
        # Si los Pokemón´s salen de la pantalla, resetear su posición y se genere un bucle
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
  
        # GAME OVER: Si el avión colisiona con un Pokemón
        avion_rect = avion.get_rect(topleft=(xavion, yavion))
        for pajaro in [(moltrespx, xmoltrespx, ymoltrespx), (zapdospx, xzapdospx, yzapdospx), 
                       (articunopx, xarticunopx, yarticunopx), (lugiapx, xlugiapx, ylugiapx),
                       (megapinsirpx, xmegapinsirpx, ymegapinsirpx)]:  # Añadir el resto de pájaros aquí
            pajaro_rect = pajaro[0].get_rect(topleft=(pajaro[1], pajaro[2]))
            if avion_rect.colliderect(pajaro_rect):
                corriendo = False
                if game_over:
                    game_over_font = pygame.font.Font('game_over.ttf', 50)  
                    texto = game_over_font.render(f'Game Over', True, (255, 255, 255))
                    ventana.blit(texto, (600, 350))
                    pygame.display.flip()
                    break
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
                    #Si el juego ha terminado

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
    #Guarda el puntaje en el archivo de texto y mostrar los 10 mejores
    with open('puntajes.txt', 'a') as archivo:
        archivo.write(str(score) + '\n')
    
    with open('puntajes.txt', 'r') as archivo:
        lines = archivo.readlines()
        puntajes = sorted([int(line.strip()) for line in lines], reverse=True)[:10]

        for i, puntaje in enumerate(puntajes, 1):
            print(f"Puntaje {i}: {puntaje}")
    
    pygame.quit()
    sys.exit()
main()

