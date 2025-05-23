import pygame
import sys

# Inicializar Pygame
pygame.init()

# Tamaño más pequeño de ventana
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Modo ventana normal
pygame.display.set_caption("Mover personaje en ventana")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Personaje
player_size = 40
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Bucle principal del juego
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)  # 60 FPS
    screen.fill(WHITE)

    # Eventos
    for event in pygame.event.get(
