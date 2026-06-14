import pygame
from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor, tomar_dano, verificar_colisao, gerar_alturas_canos


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_tomar_dano():
    """Deve subtrair corretamente o dano da vida atual."""
    assert tomar_dano(10, 3) == 7
    assert tomar_dano(5, 5) == 0


def test_verificar_colisao():
    """Deve retornar True se dois retângulos se sobrepõem e False caso contrário."""
    rect1 = pygame.Rect(0, 0, 20, 20)
    rect2 = pygame.Rect(10, 10, 20, 20) # Sobrepõe o rect1 na diagonal
    rect3 = pygame.Rect(50, 50, 20, 20) # Totalmente longe do rect1
    
    assert verificar_colisao(rect1, rect2) is True
    assert verificar_colisao(rect1, rect3) is False


def test_gerar_alturas_canos():
    """Verifica se a matemática dos canos respeita o espaço disponível e a altura mínima."""
    altura_cima, altura_baixo = gerar_alturas_canos(720, 180, 150)
    assert altura_cima >= 50
    assert altura_cima + altura_baixo + 150 == (720 - 180)