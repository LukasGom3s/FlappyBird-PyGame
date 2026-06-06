import pygame
 
from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    AZUL_CEU,
)
 
 
def executar_jogo():
    """Loop Principal"""
    pygame.init()
 
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
 
    relogio = pygame.time.Clock()
    rodando = True
 
    while rodando:
        relogio.tick(FPS)
 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
 
        tela.fill(AZUL_CEU)
 
        pygame.display.flip()
 
    pygame.quit()