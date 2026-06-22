import random
import pygame

from .config import LARGURA_TELA, ALTURA_TELA

def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica se há colisão entre dois retângulos."""
    return retangulo_1.colliderect(retangulo_2)


def gerar_alturas_canos(altura_tela, chao_altura, espaco_entre_canos):
    """Gera alturas aleatórias para os canos de cima e de baixo."""
    altura_disponivel = altura_tela - chao_altura
    altura_minima = 50
    altura_maxima_cima = altura_disponivel - espaco_entre_canos - altura_minima
    altura_cima = random.randint(altura_minima, altura_maxima_cima)
    altura_baixo = altura_disponivel - altura_cima - espaco_entre_canos
    
    return altura_cima, altura_baixo


def carregar_imagens(chao_altura, cano_largura):
    """Carrega e redimensiona todas as imagens do jogo, retornando um dicionário."""
    imagens = {}
    
    imagens['icone'] = pygame.image.load("assets/imagens/icon.png").convert_alpha()
    
    fundo = pygame.image.load("assets/imagens/background.png").convert()
    imagens['fundo'] = pygame.transform.scale(fundo, (LARGURA_TELA, ALTURA_TELA))
    
    chao = pygame.image.load("assets/imagens/ground.png").convert()
    imagens['chao'] = pygame.transform.scale(chao, (LARGURA_TELA, chao_altura))
    
    cano = pygame.image.load("assets/imagens/cano.png").convert_alpha()
    imagens['cano'] = pygame.transform.scale(cano, (cano_largura, cano.get_height()))
    
    img_b1 = pygame.image.load("assets/imagens/B1.png").convert_alpha()
    img_b2 = pygame.image.load("assets/imagens/B2.png").convert_alpha()
    img_b3 = pygame.image.load("assets/imagens/B3.png").convert_alpha()
    imagens['passaro'] = [img_b1, img_b2, img_b3, img_b2]

    coracao = pygame.image.load("assets/imagens/heart.png").convert()
    coracao.set_colorkey(coracao.get_at((0, 0)))
    imagens['coracao'] = pygame.transform.scale(coracao, (30, 30))
    
    # Usamos .convert() e pegamos a cor do pixel (0,0) para garantir a transparência
    coracao = pygame.image.load("assets/imagens/heart.png").convert()
    coracao.set_colorkey(coracao.get_at((0, 0)))
    imagens['coracao'] = pygame.transform.scale(coracao, (30, 30))

    return imagens