import pygame
import random
import sys

pygame.init()

LARGURA = 500
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Corrida")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 100, 255)

pos_jogador_x = LARGURA // 2 - 25
pos_jogador_y = ALTURA - 120

pos_inimigo_x = random.randint(50, LARGURA - 100)
pos_inimigo_y = -100

velocidade_inimigo = 5
velocidade_jogador = 5
pontuacao = 0

fonte = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and pos_jogador_x > 0:
        pos_jogador_x -= velocidade_jogador
    if teclas[pygame.K_RIGHT] and pos_jogador_x < LARGURA - 50:
        pos_jogador_x += velocidade_jogador

    pos_inimigo_y += velocidade_inimigo

    if pos_inimigo_y > ALTURA:
        pos_inimigo_y = -100
        pos_inimigo_x = random.randint(50, LARGURA - 100)
        pontuacao += 1
        velocidade_inimigo += 0.2

    jogador_rect = pygame.Rect(pos_jogador_x, pos_jogador_y, 50, 100)
    inimigo_rect = pygame.Rect(pos_inimigo_x, pos_inimigo_y, 50, 100)

    if jogador_rect.colliderect(inimigo_rect):
        tela.fill(VERMELHO)
        texto = fonte.render("Game Over!", True, BRANCO)
        tela.blit(texto, (LARGURA // 2 - 80, ALTURA // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    tela.fill(PRETO)
    pygame.draw.rect(tela, AZUL, jogador_rect)
    pygame.draw.rect(tela, VERMELHO, inimigo_rect)

    texto_pontos = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
    tela.blit(texto_pontos, (10, 10))

    pygame.display.update()
    clock.tick(60)
