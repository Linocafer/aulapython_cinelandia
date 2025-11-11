import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("🐍 Snake Game")

# Cores
verde = (0, 255, 0)
vermelho = (255, 0, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)

# Clock (controla FPS)
clock = pygame.time.Clock()
fps = 15

# Tamanho do bloco
tamanho_bloco = 20

# Fonte
fonte = pygame.font.SysFont("arial", 25)

def mensagem(texto, cor, x, y):
    tela_texto = fonte.render(texto, True, cor)
    tela.blit(tela_texto, [x, y])

def jogo():
    game_over = False
    game_close = False

    # Posição inicial da cobrinha
    x = largura // 2
    y = altura // 2
    dx = 0
    dy = 0

    corpo = []
    tamanho = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    while not game_over:
        while game_close:
            tela.fill(preto)
            mensagem("Você perdeu! Pressione C para jogar novamente ou Q para sair.", vermelho, 30, altura // 3)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and dx == 0:
                    dx = -tamanho_bloco
                    dy = 0
                elif evento.key == pygame.K_RIGHT and dx == 0:
                    dx = tamanho_bloco
                    dy = 0
                elif evento.key == pygame.K_UP and dy == 0:
                    dy = -tamanho_bloco
                    dx = 0
                elif evento.key == pygame.K_DOWN and dy == 0:
                    dy = tamanho_bloco
                    dx = 0

        # Atualiza posição da cabeça
        x += dx
        y += dy

        # Verifica colisões com borda
        if x >= largura or x < 0 or y >= altura or y < 0:
            game_close = True

        tela.fill(preto)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        # Atualiza corpo da cobra
        cabeca = []
        cabeca.append(x)
        cabeca.append(y)
        corpo.append(cabeca)

        if len(corpo) > tamanho:
            del corpo[0]

        # Colisão com o próprio corpo
        for parte in corpo[:-1]:
            if parte == cabeca:
                game_close = True

        # Desenha a cobra
        for parte in corpo:
            pygame.draw.rect(tela, verde, [parte[0], parte[1], tamanho_bloco, tamanho_bloco])

        mensagem(f"Pontuação: {tamanho - 1}", branco, 10, 10)

        pygame.display.update()

        # Quando come a comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            tamanho += 1

        clock.tick(fps)

jogo()
