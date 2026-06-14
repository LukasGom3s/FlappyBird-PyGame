import pygame
            
class Passaro(pygame.sprite.Sprite):
    def __init__(self, x, y, imagens):
        super().__init__()
        self.imagens = imagens
        self.indice_imagem = 0
        self.contador_animacao = 0
        
        self.image = self.imagens[self.indice_imagem]
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Propriedades físicas
        self.velocidade_y = 0
        self.gravidade = 0.5
        self.forca_pulo = -8
        
    def pular(self):
        self.velocidade_y = self.forca_pulo
        
    def atualizar(self):
        # Aplica gravidade
        self.velocidade_y += self.gravidade
        self.rect.y += self.velocidade_y
        
        # Atualiza animação
        self.contador_animacao += 1
        if self.contador_animacao >= 5:
            self.contador_animacao = 0
            self.indice_imagem += 1
            if self.indice_imagem >= len(self.imagens):
                self.indice_imagem = 0
                
        self.image = self.imagens[self.indice_imagem]


class Cano(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem, de_cima=False):
        super().__init__()
        self.image = imagem
        self.rect = self.image.get_rect()
        
        # Alinha o cano com base na sua orientação (teto ou chão)
        if de_cima:
            self.rect.bottomleft = (x, y)
        else:
            self.rect.topleft = (x, y)
            
    def atualizar(self, velocidade):
        self.rect.x -= velocidade