import pygame
import random
import sys

# Inicialização
pygame.init()

# --- Configurações da janela ---
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("🚀 Jogo da Nave Espacial")

# --- Cores ---
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# --- Clock ---
clock = pygame.time.Clock()
FPS = 60

# --- Classe Nave ---
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA // 2
        self.rect.bottom = ALTURA - 10
        self.velocidade = 7

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < LARGURA:
            self.rect.x += self.velocidade

    def atirar(self):
        tiro = Tiro(self.rect.centerx, self.rect.top)
        todos_sprites.add(tiro)
        tiros.add(tiro)

# --- Classe Tiro ---
class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocidade = -10

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.bottom < 0:
            self.kill()  # Remove o tiro da tela

# --- Classe Inimigo ---
class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(VERMELHO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.velocidade_y = random.randint(3, 8)

    def update(self):
        self.rect.y += self.velocidade_y
        if self.rect.top > ALTURA:
            self.rect.x = random.randint(0, LARGURA - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.velocidade_y = random.randint(3, 8)

# --- Grupos de sprites ---
todos_sprites = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
tiros = pygame.sprite.Group()

# Cria a nave
nave = Nave()
todos_sprites.add(nave)

# Cria inimigos iniciais
for i in range(8):
    inimigo = Inimigo()
    todos_sprites.add(inimigo)
    inimigos.add(inimigo)

# --- Loop principal ---
pontuacao = 0
rodando = True
while rodando:
    clock.tick(FPS)

    # --- Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                nave.atirar()

    # --- Atualizações ---
    todos_sprites.update()

    # --- Colisões: tiro vs inimigo ---
    hits = pygame.sprite.groupcollide(inimigos, tiros, True, True)
    for hit in hits:
        pontuacao += 10
        inimigo = Inimigo()
        todos_sprites.add(inimigo)
        inimigos.add(inimigo)

    # --- Colisões: nave vs inimigo ---
    colisao = pygame.sprite.spritecollide(nave, inimigos, False)
    if colisao:
        rodando = False  # Fim de jogo

    # --- Desenho ---
    tela.fill(PRETO)
    todos_sprites.draw(tela)

    # Exibir pontuação
    fonte = pygame.font.SysFont("Arial", 30)
    texto = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
    tela.blit(texto, (10, 10))

    pygame.display.flip()

# --- Fim de jogo ---
pygame.quit()
sys.exit()
