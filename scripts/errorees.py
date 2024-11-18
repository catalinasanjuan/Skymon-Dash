import pygame
import sys

def main():
    pygame.init()

    ventana = pygame.display.set_mode((1472, 800))
    pygame.display.set_caption("avion desplazamiento")

    # [El resto de la inicialización permanece igual]

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

        # [El resto del código para mover y dibujar objetos]

        # Detección de colisiones
        avion_rect = avion.get_rect(topleft=(xavion, yavion))
        moltrespx_rect = moltrespx.get_rect(topleft=(xmoltrespx, ymoltrespx))
        zapdospx_rect = zapdospx.get_rect(topleft=(xzapdospx, yzapdospx))
        articunopx_rect = articunopx.get_rect(topleft=(xarticunopx, yarticunopx))
        lugiapx_rect = lugiapx.get_rect(topleft=(xlugiapx, ylugiapx))
        megapinsirpx_rect = megapinsirpx.get_rect(topleft=(xmegapinsirpx, ymegapinsirpx))

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
# ...

# Detección de colisiones
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

# ...

main()
