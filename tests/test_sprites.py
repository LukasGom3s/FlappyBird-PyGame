import pygame
from src.sprites import Passaro, Cano

# Inicializamos uma mini-janela invisível do PyGame para testar as mecânicas das Classes
pygame.init()
pygame.display.set_mode((1, 1), pygame.HIDDEN)

def test_passaro_pular():
    """Testa se a função pular altera a velocidade no eixo Y do pássaro corretamente."""
    imagens_mock = [pygame.Surface((30, 30))]
    passaro = Passaro(50, 300, imagens_mock)
    
    assert passaro.velocidade_y == 0
    passaro.pular()
    assert passaro.velocidade_y == -8

def test_passaro_atualizar_aplica_gravidade():
    """Verifica se a gravidade puxa o pássaro para baixo ao chamar atualizar."""
    imagens_mock = [pygame.Surface((30, 30))]
    passaro = Passaro(50, 300, imagens_mock)
    
    passaro.atualizar()
    assert passaro.velocidade_y == 0.5  # Gravidade base foi aplicada

def test_cano_posicionamento_cima_baixo():
    """Testa se as caixas de colisão dos canos se alinham no topo e fundo da fresta."""
    imagem_mock = pygame.Surface((80, 400))
    
    cano_cima = Cano(100, 200, imagem_mock, de_cima=True)
    assert cano_cima.rect.bottomleft == (100, 200) # Base alinhada na posição Y = 200
    
    cano_baixo = Cano(100, 500, imagem_mock, de_cima=False)
    assert cano_baixo.rect.topleft == (100, 500) # Topo alinhado na posição Y = 500

def test_cano_movimentacao():
    imagem_mock = pygame.Surface((80, 400))
    cano = Cano(100, 200, imagem_mock)
    cano.atualizar(velocidade=3)
    assert cano.rect.x == 97  # 100 - 3 pixels da velocidade