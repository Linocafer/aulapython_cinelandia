import pygame
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("🏓 Pong Game")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# FPS
clock = pygame.time.Clock()
fps = 60

# Raquetes
largura_raquete, altura_raquete = 15, 100
raquete_esquerda_y = altura // 2 - altura_raquete // 2
raquete_direita_y = altura // 2 - altura_raquete // 2
velocidade_raquete = 7

# Bola
bola_x, bola_y = largura // 2, altura // 2
velocidade_bola_x = 5
velocidade_bola_y = 5
tamanho_bola = 20

# Pontuação
pontos_esquerda = 0
pontos_direita = 0
fonte = pygame.font.SysFont("arial", 40)

# Função principal
def desenhar():
    tela.fill(preto)
    # Linha do meio
    pygame.draw.aaline(tela, branco, (largura // 2, 0), (largura // 2, altura))
    # Raquetes
    pygame.draw.rect(tela, branco, (20, raquete_esquerda_y, largura_raquete, altura_raquete))
    pygame.draw.rect(tela, branco, (largura - 20 - largura_raquete, raquete_direita_y, largura_raquete, altura_raquete))
    # Bola
    pygame.draw.ellipse(tela, branco, (bola_x, bola_y, tamanho_bola, tamanho_bola))
    # Pontuação
    texto = fonte.render(f"{pontos_esquerda}    {pontos_direita}", True, branco)
    tela.blit(texto, (largura // 2 - texto.get_width() // 2, 20))
    pygame.display.flip()

# Loop principal
def jogo():
    global raquete_esquerda_y, raquete_direita_y
    global bola_x, bola_y, velocidade_bola_x, velocidade_bola_y
    global pontos_esquerda, pontos_direita

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimento das raquetes
        teclas = pygame.key.get_pressed()
        # Raquete esquerda (W e S)
        if teclas[pygame.K_w] and raquete_esquerda_y > 0:
            raquete_esquerda_y -= velocidade_raquete
        if teclas[pygame.K_s] and raquete_esquerda_y < altura - altura_raquete:
            raquete_esquerda_y += velocidade_raquete
        # Raquete direita (setas ↑ ↓)
        if teclas[pygame.K_UP] and raquete_direita_y > 0:
            raquete_direita_y -= velocidade_raquete
        if teclas[pygame.K_DOWN] and raquete_direita_y < altura - altura_raquete:
            raquete_direita_y += velocidade_raquete

        # Movimento da bola
        bola_x += velocidade_bola_x
        bola_y += velocidade_bola_y

        # Colisão com bordas
        if bola_y <= 0 or bola_y >= altura - tamanho_bola:
            velocidade_bola_y *= -1

        # Colisão com raquete esquerda
        if (20 < bola_x < 20 + largura_raquete and
                raquete_esquerda_y < bola_y < raquete_esquerda_y + altura_raquete):
            velocidade_bola_x *= -1

        # Colisão com raquete direita
        if (largura - 20 - largura_raquete < bola_x + tamanho_bola < largura - 20 and
                raquete_direita_y < bola_y < raquete_direita_y + altura_raquete):
            velocidade_bola_x *= -1

        # Pontuação
        if bola_x <= 0:
            pontos_direita += 1
            bola_x, bola_y = largura // 2, altura // 2
            velocidade_bola_x *= -1
        elif bola_x >= largura - tamanho_bola:
            pontos_esquerda += 1
            bola_x, bola_y = largura // 2, altura // 2
            velocidade_bola_x *= -1

        desenhar()
        clock.tick(fps)

jogo()
