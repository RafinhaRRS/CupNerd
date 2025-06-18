import pygame
import sys
import random

pygame.init()

LARGURA = 1000
ALTURA = 700

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("CupNerd")

# --- CARREGAMENTO DE IMAGENS ---
try:
    fundo = pygame.image.load('assets/fundojogo.png').convert()
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

    calice_img = pygame.image.load('assets/calice_lendaria.png').convert_alpha()
    calice_img = pygame.transform.scale(calice_img, (300, 300))

    caneco_img = pygame.image.load('assets/caneco.png').convert_alpha()
    caneco_img = pygame.transform.scale(caneco_img, (300, 300))

    nave_img_up = pygame.image.load('assets/nave.png').convert_alpha()
    nave_img_up = pygame.transform.scale(nave_img_up, (100, 100))

    nave_img_right = pygame.image.load('assets/nave_direita.png').convert_alpha()
    nave_img_right = pygame.transform.scale(nave_img_right, (100, 100))

    inimigo_img = pygame.image.load('assets/inimigo.png').convert_alpha()
    inimigo_img = pygame.transform.scale(inimigo_img, (50, 50))

    inimigo2_img = pygame.image.load('assets/inimigo2.png').convert_alpha()
    inimigo2_img = pygame.transform.scale(inimigo2_img, (70, 70))

    chefao_img = pygame.image.load('assets/chefao.png').convert_alpha()
    chefao_img = pygame.transform.scale(chefao_img, (150, 150))

    tiro_jogador_img_up = pygame.image.load('assets/tiro_jogador_up.png').convert_alpha()
    tiro_jogador_img_up = pygame.transform.scale(tiro_jogador_img_up, (30, 60))

    tiro_jogador_img_right = pygame.image.load('assets/tiro_jogador_right.png').convert_alpha()
    tiro_jogador_img_right = pygame.transform.scale(tiro_jogador_img_right, (60, 30))

    tiro_chefao_img = pygame.image.load('assets/tiro_chefao.png').convert_alpha()
    tiro_chefao_img = pygame.transform.scale(tiro_chefao_img, (15, 15))

    explosao_img = pygame.image.load('assets/explosao.png').convert_alpha()
    explosao_img = pygame.transform.scale(explosao_img, (150, 150))

except pygame.error:
    fundo = None
    calice_img = None
    caneco_img = None
    nave_img_up = None
    nave_img_right = None
    inimigo_img = None
    inimigo2_img = None
    chefao_img = None
    tiro_jogador_img_up = None
    tiro_jogador_img_right = None
    tiro_chefao_img = None
    explosao_img = None

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)

# Fonte
fonte_grande = pygame.font.SysFont(None, 48)
fonte_media = pygame.font.SysFont(None, 32)
fonte = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

# --- TELA PARA DIGITAR O NOME ---

def tela_nome_jogador():
    nome = ""
    ativo = True
    while ativo:
        tela.fill(PRETO)
        texto = fonte_grande.render("Bem vindo ao CupNerd - Digite seu nome:", True, BRANCO)
        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, 250))

        caixa = pygame.Rect(LARGURA // 2 - 150, 350, 300, 50)
        pygame.draw.rect(tela, BRANCO, caixa, 2)
        texto_nome = fonte.render(nome, True, BRANCO)
        tela.blit(texto_nome, (caixa.x + 10, caixa.y + 10))

        dica = fonte_media.render("Pressione ENTER para confirmar", True, BRANCO)
        tela.blit(dica, (LARGURA // 2 - dica.get_width() // 2, 420))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nome.strip() != "":
                    ativo = False
                elif evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                else:
                    if len(nome) < 15:
                        char = evento.unicode
                        if char.isalnum() or char == " ":
                            nome += char
        clock.tick(30)
    return nome

# --- NOVA TELA DE COMANDOS ---

def tela_comandos():
    tela.fill(PRETO)
    linhas_comandos = [
        "COMANDOS DO CUPNERD",
        "",
        "Setas (↑ ↓ ← →): Mover a nave",
        "Z: Disparar tiro",
        "T: Trocar direção do tiro (após 50 pontos)",
        "Espaço: Pausar/despausar o jogo",
        "",
        "Pressione ESPAÇO para continuar..."
    ]
    y_texto = 200
    for linha in linhas_comandos:
        texto_render = fonte_media.render(linha, True, BRANCO)
        tela.blit(texto_render, (LARGURA // 2 - texto_render.get_width() // 2, y_texto))
        y_texto += 45
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False
        clock.tick(30)

# --- TELA INICIAL ---

def tela_inicial():
    tela.fill(PRETO)
    if calice_img:
        tela.blit(calice_img, (LARGURA//2 - calice_img.get_width()//2, 50))

    linhas_texto = [
        "Olá sou a Cálice Lendária",
        "",
        "Seu irmão Caneco foi capturado pela Lunar!",
        "Você precisa resgatá-lo em uma missão perigosa.",
        "Prepare-se para destruir a Lunar e salvar Caneco.",
        "",
        "Pressione ESPAÇO para começar o jogo."
    ]

    y_texto = 370
    for linha in linhas_texto:
        if linha == "":
            y_texto += 10
            continue
        texto_render = fonte_media.render(linha, True, BRANCO)
        tela.blit(texto_render, (LARGURA//2 - texto_render.get_width()//2, y_texto))
        y_texto += 40

    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False
        clock.tick(30)

# --- TELA DE AGRADECIMENTO ---

def tela_agradecimento(nome_jogador):
    tela.fill(PRETO)
    if caneco_img:
        tela.blit(caneco_img, (LARGURA // 2 - caneco_img.get_width() // 2, 100))
    texto = fonte_grande.render(f"Obrigado por me salvar, {nome_jogador}!", True, BRANCO)
    tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, 420))
    dica = fonte_media.render("Pressione ESPAÇO para finalizar", True, BRANCO)
    tela.blit(dica, (LARGURA // 2 - dica.get_width() // 2, 470))
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False
        clock.tick(30)

# --- TELA DE PAUSA ---

def tela_pausa():
    texto = fonte_grande.render("Jogo Pausado!", True, BRANCO)
    dica = fonte_media.render("Pressione ESPAÇO para continuar", True, BRANCO)
    tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2 - 40))
    tela.blit(dica, (LARGURA // 2 - dica.get_width() // 2, ALTURA // 2 + 30))
    pygame.display.flip()

    pausado = True
    while pausado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    pausado = False
        clock.tick(30)

# --- INÍCIO DO JOGO ---
nome_jogador = tela_nome_jogador()
tela_comandos()         # <-- NOVA TELA DE COMANDOS!
tela_inicial()

pontos = 0

# Jogador
if nave_img_up:
    jogador = nave_img_up.get_rect(center=(400, 500))
else:
    jogador = pygame.Rect(400, 500, 100, 50)

vel_jogador = 4
direcao_nave = 'up'

# Inimigos
if inimigo_img:
    inimigo = inimigo_img.get_rect(topleft=(random.randint(0, LARGURA - 50), 0))
else:
    inimigo = pygame.Rect(random.randint(0, LARGURA - 50), 0, 50, 50)

if inimigo2_img:
    inimigo2 = inimigo2_img.get_rect(topleft=(random.randint(0, LARGURA - 70), 0))
else:
    inimigo2 = pygame.Rect(random.randint(0, LARGURA - 70), 0, 70, 70)

vel_inimigo = 1.5

tiros = []
vel_tiro = 7

chefao_ativo = False
tiros_chefao = []
vel_tiro_chefao = 5
tiros_acertados_chefao = 0
max_tiros_chefao = 25
explosao_ativo = False
explosao_tempo = 0

if chefao_img:
    chefao = chefao_img.get_rect(midright=(LARGURA + 100, ALTURA // 2))
else:
    chefao = pygame.Rect(LARGURA + 100, ALTURA // 2 - 75, 150, 150)

vel_chefao = 2

caneco_salvo = False
pausado = False

def fim_de_jogo():
    texto = fonte.render("Game Over", True, BRANCO)
    tela.blit(texto, (LARGURA // 2 - 70, ALTURA // 2 - 20))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

while True:
    if caneco_salvo:
        tela_agradecimento(nome_jogador)
        pygame.quit()
        sys.exit()

    # Evento de pausa
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN and not pausado:
            # Pausar/despausar com espaço
            if evento.key == pygame.K_SPACE:
                pausado = True
                tela_pausa()
                pausado = False
        if evento.type == pygame.KEYDOWN and not pausado:
            if evento.key == pygame.K_z:
                if direcao_nave == 'up':
                    tiro_x = jogador.centerx - 15
                    tiro_y = jogador.top - 60
                    rect_tiro = pygame.Rect(tiro_x, tiro_y, 30, 60)
                    tiros.append({'rect': rect_tiro, 'dir': 'up'})
                elif direcao_nave == 'right':
                    tiro_x = jogador.right
                    tiro_y = jogador.centery - 15
                    rect_tiro = pygame.Rect(tiro_x, tiro_y, 60, 30)
                    tiros.append({'rect': rect_tiro, 'dir': 'right'})

            if evento.key == pygame.K_t and pontos >= 50:
                if direcao_nave == 'up':
                    direcao_nave = 'right'
                    jogador.width, jogador.height = 50, 100
                else:
                    direcao_nave = 'up'
                    jogador.width, jogador.height = 100, 50

    if pausado:
        continue

    if fundo:
        tela.blit(fundo, (0, 0))
    else:
        tela.fill(PRETO)

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador.left > 0:
        jogador.x -= vel_jogador
    if teclas[pygame.K_RIGHT] and jogador.right < LARGURA:
        jogador.x += vel_jogador
    if teclas[pygame.K_UP] and jogador.top > 0:
        jogador.y -= vel_jogador
    if teclas[pygame.K_DOWN] and jogador.bottom < ALTURA:
        jogador.y += vel_jogador

    def mover_inimigo(inim, velocidade, pontuacao):
        if pontuacao >= 125:
            inim.x -= velocidade
            if inim.right < 0:
                inim.y = random.randint(0, ALTURA - inim.height)
                inim.x = LARGURA
        else:
            inim.y += velocidade
            if inim.top > ALTURA:
                inim.x = random.randint(0, LARGURA - inim.width)
                inim.y = 0

    mover_inimigo(inimigo, vel_inimigo, pontos)
    mover_inimigo(inimigo2, vel_inimigo, pontos)

    for tiro in tiros[:]:
        if tiro['dir'] == 'up':
            tiro['rect'].y -= vel_tiro
            if tiro['rect'].bottom < 0:
                tiros.remove(tiro)
        elif tiro['dir'] == 'right':
            tiro['rect'].x += vel_tiro
            if tiro['rect'].left > LARGURA:
                tiros.remove(tiro)

    for tiro in tiros[:]:
        if inimigo.colliderect(tiro['rect']):
            tiros.remove(tiro)
            inimigo.x = LARGURA if pontos >= 125 else random.randint(0, LARGURA - inimigo.width)
            inimigo.y = random.randint(0, ALTURA - inimigo.height) if pontos >= 125 else 0
            pontos += 5
            vel_inimigo += 0.1

        elif inimigo2.colliderect(tiro['rect']):
            tiros.remove(tiro)
            inimigo2.x = LARGURA if pontos >= 125 else random.randint(0, LARGURA - inimigo2.width)
            inimigo2.y = random.randint(0, ALTURA - inimigo2.height) if pontos >= 125 else 0
            pontos += 8
            vel_inimigo += 0.1

    if pontos >= 200:
        if not chefao_ativo:
            chefao_ativo = True
            chefao.midright = (LARGURA + chefao.width, ALTURA // 2)

    if chefao_ativo and chefao.right > LARGURA - 10:
        chefao.x -= vel_chefao
    elif chefao_ativo:
        chefao.right = LARGURA - 10

    if chefao_ativo:
        if random.randint(0, 60) == 0:
            alvos = []
            if inimigo.left < LARGURA:
                alvos.append(inimigo)
            if inimigo2.left < LARGURA:
                alvos.append(inimigo2)
            if alvos:
                alvo = random.choice(alvos)
                tiro_rect = tiro_chefao_img.get_rect(center=(chefao.left, chefao.top + chefao.height // 2))
                tiros_chefao.append({'rect': tiro_rect, 'alvo': alvo})

    for tiro_c in tiros_chefao[:]:
        tiro_c['rect'].x -= vel_tiro_chefao
        if tiro_c['rect'].right < 0:
            tiros_chefao.remove(tiro_c)

        if jogador.colliderect(tiro_c['rect']):
            fim_de_jogo()

        if tiro_c['alvo'].colliderect(tiro_c['rect']):
            if tiro_c['alvo'] == inimigo:
                inimigo.x = LARGURA if pontos >= 125 else random.randint(0, LARGURA - inimigo.width)
                inimigo.y = random.randint(0, ALTURA - inimigo.height) if pontos >= 125 else 0
            elif tiro_c['alvo'] == inimigo2:
                inimigo2.x = LARGURA if pontos >= 125 else random.randint(0, LARGURA - inimigo2.width)
                inimigo2.y = random.randint(0, ALTURA - inimigo2.height) if pontos >= 125 else 0
            tiros_chefao.remove(tiro_c)

    if chefao_ativo:
        for tiro in tiros[:]:
            if chefao.colliderect(tiro['rect']):
                tiros.remove(tiro)
                tiros_acertados_chefao += 1
                if tiros_acertados_chefao >= max_tiros_chefao:
                    explosao_ativo = True
                    explosao_pos = chefao.topleft
                    chefao_ativo = False
                    tiros_acertados_chefao = 0
                    caneco_salvo = True

    if explosao_ativo:
        tela.blit(explosao_img, explosao_pos)
        explosao_tempo += 1
        if explosao_tempo > 60:
            explosao_ativo = False
            explosao_tempo = 0

    if jogador.colliderect(inimigo) or jogador.colliderect(inimigo2):
        fim_de_jogo()

    if direcao_nave == 'up':
        if nave_img_up:
            tela.blit(nave_img_up, jogador)
        else:
            pygame.draw.rect(tela, (0, 0, 255), jogador)
    else:
        if nave_img_right:
            tela.blit(nave_img_right, jogador)
        else:
            pygame.draw.rect(tela, (0, 0, 255), jogador)

    if inimigo_img:
        tela.blit(inimigo_img, inimigo)
    else:
        pygame.draw.rect(tela, (255, 0, 0), inimigo)

    if inimigo2_img:
        tela.blit(inimigo2_img, inimigo2)
    else:
        pygame.draw.rect(tela, (255, 0, 0), inimigo2)

    for tiro in tiros:
        if tiro['dir'] == 'up':
            if tiro_jogador_img_up:
                tela.blit(tiro_jogador_img_up, tiro['rect'])
            else:
                pygame.draw.rect(tela, AMARELO, tiro['rect'])
        else:
            if tiro_jogador_img_right:
                tela.blit(tiro_jogador_img_right, tiro['rect'])
            else:
                pygame.draw.rect(tela, AMARELO, tiro['rect'])

    if chefao_ativo:
        if chefao_img:
            tela.blit(chefao_img, chefao)
        else:
            pygame.draw.rect(tela, (255, 0, 0), chefao)

    for tiro_c in tiros_chefao:
        if tiro_chefao_img:
            tela.blit(tiro_chefao_img, tiro_c['rect'])
        else:
            pygame.draw.rect(tela, AMARELO, tiro_c['rect'])

    texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto_pontos, (10, 10))

    pygame.display.flip()
    clock.tick(60)