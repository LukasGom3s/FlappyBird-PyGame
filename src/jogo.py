import pygame
 
from .config import (LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO, AZUL_CEU, BRANCO, CINZA)
from .funcoes import verificar_colisao, limitar_valor
 
def executar_jogo():
    """Loop Principal"""
    pygame.init()
 
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
 
    relogio = pygame.time.Clock()
    
    # Jogador
    passaro_x = 50
    passaro_y = ALTURA_TELA // 2
    velocidade_y = 0
    gravidade = 0.5
    forca_pulo = -8

    # Elementos 
    cano_x = LARGURA_TELA
    cano_velocidade = 3
    cano_largura = 50
    cano_altura = 300
    chao_rect = pygame.Rect(0, ALTURA_TELA - 50, LARGURA_TELA, 50)

    rodando = True
    while rodando:
        relogio.tick(FPS)
 
        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            # Controle de pular com espaço
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                velocidade_y = forca_pulo
 
        # Lógica de movimentação
        velocidade_y += gravidade
        passaro_y += velocidade_y
        
        # Movimentação do cano
        cano_x -= cano_velocidade
        if cano_x < -cano_largura:
            cano_x = LARGURA_TELA
            
        # Atualização dos "canos"
        passaro_rect = pygame.Rect(passaro_x, passaro_y, 30, 30)
        cano_rect = pygame.Rect(cano_x, (cano_altura - 50), cano_largura, cano_altura)
        
        # Colisões
        if verificar_colisao(passaro_rect, chao_rect):
            passaro_y = chao_rect.top - 30 
            velocidade_y = 0
        
        if verificar_colisao(passaro_rect, cano_rect):
            print("Bateu no cano!")
            
            # Reseta se o passarinho bater
            passaro_y = ALTURA_TELA // 2

        # Desenho (A ordem das funções importa, nao muda!)
        tela.fill(AZUL_CEU) # 1. Pinta o fundo primeiro
        
        pygame.draw.rect(tela, BRANCO, passaro_rect)   # Desenha passarinho
        pygame.draw.rect(tela, CINZA, chao_rect)      # Desenha chão
        pygame.draw.rect(tela, (0, 255, 0), cano_rect) # Desenha cano
 
        pygame.display.flip() # Atualiza tudo na tela
 
    pygame.quit()