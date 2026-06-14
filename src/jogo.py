import pygame
 
from .config import (LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JANELA)
from .funcoes import verificar_colisao, limitar_valor, gerar_alturas_canos, carregar_imagens
from .sprites import Passaro, Cano
 
def executar_jogo():
    pygame.init()
 
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JANELA)
 
    # Configurações dos canos
    cano_x = LARGURA_TELA
    cano_velocidade = 3
    cano_largura = 80
    espaco_entre_canos = 150
    
    # Configurações do chão
    chao_altura = ALTURA_TELA // 4 
    chao_y = ALTURA_TELA - chao_altura
    chao_rect = pygame.Rect(0, chao_y, LARGURA_TELA, chao_altura)
    chao_x = 0

    # Carregamento de recursos
    imagens = carregar_imagens(chao_altura, cano_largura)
    pygame.display.set_icon(imagens['icone'])

    relogio = pygame.time.Clock()

    # Inicialização das entidades
    passaro = Passaro(50, ALTURA_TELA // 2, imagens['passaro'])

    # TODO: PONTUAÇÃO E VIDAS - Inicializar as variáveis de pontos e quantidade de vidas aqui antes do loop começar.
    # TODO: LER RECORDE - Importar e usar a função `carregar_recorde()` do arquivo src/dados.py para ler o arquivo recorde.txt e guardar o valor numa variável.

    altura_cano_cima, altura_cano_baixo = gerar_alturas_canos(ALTURA_TELA, chao_altura, espaco_entre_canos)

    imagem_fundo = imagens['fundo']
    imagem_chao = imagens['chao']
    
    cano_cima = Cano(cano_x, altura_cano_cima, imagens['cano'], de_cima=True)
    cano_baixo = Cano(cano_x, chao_y - altura_cano_baixo, imagens['cano'], de_cima=False)


    rodando = True
    while rodando:
        relogio.tick(FPS)
 
        # Processamento de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                passaro.pular()
 
        # Atualização do pássaro
        passaro.atualizar()
        
        # Atualização dos canos
        cano_cima.atualizar(cano_velocidade)
        cano_baixo.atualizar(cano_velocidade)
        cano_x = cano_cima.rect.x
        
        if cano_x < -cano_largura:
            cano_x = LARGURA_TELA
            altura_cano_cima, altura_cano_baixo = gerar_alturas_canos(ALTURA_TELA, chao_altura, espaco_entre_canos)
            
            cano_cima = Cano(cano_x, altura_cano_cima, imagens['cano'], de_cima=True)
            cano_baixo = Cano(cano_x, chao_y - altura_cano_baixo, imagens['cano'], de_cima=False)
            
            # TODO: MARCAR PONTO - Se os canos saíram da tela, significa que o pássaro passou por eles. Somar +1 ponto aqui!
            
        # Atualização do chão em loop dinâmico
        chao_x -= cano_velocidade
        if chao_x <= -LARGURA_TELA:
            chao_x = 0
            
        # Verificação de colisões
        if verificar_colisao(passaro.rect, chao_rect):
            passaro.rect.bottom = chao_rect.top
            passaro.velocidade_y = 0
            # TODO: PERDA DE VIDA (CHÃO) - O pássaro tocou o chão. Subtrair uma vida da variável de vidas aqui.
        
        if verificar_colisao(passaro.rect, cano_cima.rect) or verificar_colisao(passaro.rect, cano_baixo.rect):
            print("Bateu no cano!")
            
            # TODO: PERDA DE VIDA (CANO) - O pássaro bateu no cano. Subtrair uma vida da variável de vidas aqui.
            
            # Reinicia o estado do jogo após colisão
            passaro.rect.y = ALTURA_TELA // 2
            passaro.velocidade_y = 0
            cano_x = LARGURA_TELA
            altura_cano_cima, altura_cano_baixo = gerar_alturas_canos(ALTURA_TELA, chao_altura, espaco_entre_canos)
            cano_cima = Cano(cano_x, altura_cano_cima, imagens['cano'], de_cima=True)
            cano_baixo = Cano(cano_x, chao_y - altura_cano_baixo, imagens['cano'], de_cima=False)
            
            # TODO: GAME OVER - Se a quantidade de vidas chegar a 0, interromper o jogo e exibir uma tela de Game Over.
            # TODO: SALVAR RECORDE - No momento do Game Over, checar se os pontos > recorde atual. Se for, usar `salvar_recorde()` do src/dados.py.

        # Renderização
        tela.blit(imagem_fundo, (0, 0))
        
        tela.blit(passaro.image, passaro.rect)
        tela.blit(cano_cima.image, cano_cima.rect)
        tela.blit(cano_baixo.image, cano_baixo.rect)
        
        tela.blit(imagem_chao, (chao_x, chao_y))
        tela.blit(imagem_chao, (chao_x + LARGURA_TELA, chao_y))
 
        # TODO: INTERFACE E TEXTOS - Renderizar e desenhar os textos na tela (ex: vidas, pontuação e recorde) aqui no final, por cima de todo o resto.
 
        pygame.display.flip()
 
    pygame.quit()