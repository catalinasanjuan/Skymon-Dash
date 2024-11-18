import pygame
import sys

def main():
    pygame.init()
    
    ventana = pygame.display.set_mode((736, 401))
    
    anchura_imagen = 736
    imagen_fondo1 = pygame.transform.scale(pygame.image.load('fondo.jpg'), (anchura_imagen, 401))
    imagen_fondo2 = pygame.transform.scale(pygame.image.load('fondo 2.jpg'), (anchura_imagen, 401))
    
    pos_x1 = 0
    pos_x2 = anchura_imagen
    velocidad_fondo = -2  # Negativa para mover hacia la izquierda
    
    xCuadrado = 400
    yCuadrado = 200
    
    # Cargamos la imagen que queremos usar en lugar del cuadrado
    pajaro = pygame.image.load('pajaro.png') # Reemplaza 'ruta_a_tu_imagen.png' con la ruta de tu imagen
    pajaro = pygame.transform.scale(pajaro, (50, 50)) # Ajustar el tamaño de la imagen si es necesario
    
    reloj = pygame.time.Clock()
    
    corriendo = True
    while corriendo:
        reloj.tick(20)
        
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
        
        xCuadrado -= 10
        if xCuadrado < -50:
            xCuadrado = 736
        
        # Dibujamos la imagen en lugar del rectángulo
        ventana.blit(pajaro, (xCuadrado, yCuadrado))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

main()

