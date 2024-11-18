import Vehiculo
import pygame

if __name__ == "__main__":
    print("Se ha ejecutado el programa principal")
    a = Vehiculo.Automovil()
    a.setCapacidad(6)
    print("capacidad automovil, ", a.getCapacidad())
    a.avanzar()
    a.izquierda()
    a.retroceder()
    a.derecha()
    a.bajar()
    a.subir()
    print("El eje X del automovil", a.getVector())
    
    pygame.init()
    pygame.display.set_caption("Plain Game")
    ventana = pygame.display.set_mode((736, 401))
    
    anchura_imagen = 736
    imagen_fondo1 = pygame.transform.scale(pygame.image.load('fondo.jpg'), (anchura_imagen, 401))
    imagen_fondo2 = pygame.transform.scale(pygame.image.load('fondo 2.jpg'), (anchura_imagen, 401))
    
    pos_x1 = 0
    pos_x2 = anchura_imagen
    velocidad_fondo = -2  # Negativa para mover hacia la izquierda
    
    imagen = pygame.image.load(a.imagen)
    imagen = pygame.transform.flip(imagen, True, False)
    imagen = pygame.transform.scale(imagen, (200, 100))
    
    corriendo = True
    while corriendo:
        ventana.fill((0, 0, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    print("Tecla abajo")
                if evento.key == pygame.K_d:
                    print("Tecla d")
                    a.avanzar()
                if evento.key == pygame.K_w:
                    print("Tecla w")
                if evento.key == pygame.K_a:
                    print("Tecla a")
        
        # Actualizar y dibujar fondos
        pos_x1 += velocidad_fondo
        pos_x2 += velocidad_fondo
        if pos_x1 <= -anchura_imagen:
            pos_x1 = anchura_imagen
        if pos_x2 <= -anchura_imagen:
            pos_x2 = anchura_imagen
        ventana.blit(imagen_fondo1, (pos_x1, 0))
        ventana.blit(imagen_fondo2, (pos_x2, 0))
        
        ventana.blit(imagen, (a.vector["x"], a.vector["y"]))
        pygame.display.flip()

        pygame.time.Clock().tick(60)  # 60 FPS

    pygame.quit()
