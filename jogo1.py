import pygame
from sys import exit

pygame.init()
tela = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Jogo Simples")
clock = pygame.time.Clock()

x, y = 400, 200
velocidade = 5

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Movimento com teclas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Cor de fundo (RGB)
    tela.fill((30, 30, 30))
    # Desenha o jogador (retângulo)
    pygame.draw.rect(tela, (0, 255, 0), (x, y, 50, 50))
    pygame.display.update()
    clock.tick(60)
