import os
import pygame
 
from .config import (LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JANELA, CAMINHO_RECORDE)
from .funcoes import (verificar_colisao, gerar_alturas_canos, carregar_imagens, calcular_pontos, tomar_dano, jogador_perdeu)
from .dados import carregar_recorde, salvar_recorde
from .sprites import Passaro, Cano
 
def executar_jogo():
    pygame.init()
    pygame.font.init() # Adiciona uma fonte para mensagem de Game Over

    # Garante que a pasta de dados exista para evitar erro ao salvar o recorde
    diretorio_dados = os.path.dirname(CAMINHO_RECORDE)
    if diretorio_dados and not os.path.exists(diretorio_dados):
        os.makedirs(diretorio_dados)
 
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JANELA)

    # Tipo da fonte para os textos
    fonte_game_over = pygame.font.SysFont('arial', 50, bold=True)
    fonte_instrucoes = pygame.font.SysFont('arial', 30)
 
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
    passaro = Passaro(50, ALTURA_TELA // 4, imagens['passaro'])

    # Sistema de pontuação, vidas e timer
    pontos = 0
    vidas = 3
    tempo_segundos = 0
    tempo_inicio_partida = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)

    altura_cano_cima, altura_cano_baixo = gerar_alturas_canos(ALTURA_TELA, chao_altura, espaco_entre_canos)

    imagem_fundo = imagens['fundo']
    imagem_chao = imagens['chao']
    
    cano_cima = Cano(cano_x, altura_cano_cima, imagens['cano'], de_cima=True)
    cano_baixo = Cano(cano_x, chao_y - altura_cano_baixo, imagens['cano'], de_cima=False)

    # O programa sabe quando for aberto.
    estado_jogo = "INICIO"

    rodando = True
    while rodando:
        relogio.tick(FPS)
 
        # Processamento de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                # A tela quando alguem acabar de abrir o jogo
                if estado_jogo == "INICIO":
                    passaro.pular()
                    tempo_inicio_partida = pygame.time.get_ticks()
                    estado_jogo = "JOGANDO"
                elif estado_jogo == "JOGANDO":
                    passaro.pular()
                elif estado_jogo == "GAME_OVER":
                    # Reinicia o jogo após colisão
                    passaro.rect.y = ALTURA_TELA // 4
                    passaro.velocidade_y = 0
                    cano_x = LARGURA_TELA
                    altura_cano_cima, altura_cano_baixo = gerar_alturas_canos(ALTURA_TELA, chao_altura, espaco_entre_canos)
                    cano_cima = Cano(cano_x, altura_cano_cima, imagens['cano'], de_cima=True)
                    cano_baixo = Cano(cano_x, chao_y - altura_cano_baixo, imagens['cano'], de_cima=False)
                    pontos = 0
                    vidas = 3
                    tempo_inicio_partida = pygame.time.get_ticks()
                    estado_jogo = "JOGANDO"

            # As coisas vão se mover
        if estado_jogo == "JOGANDO":
            tempo_segundos = (pygame.time.get_ticks() - tempo_inicio_partida) // 1000

            # Passarinho
            passaro.atualizar()

            # Canos
            cano_cima.atualizar(cano_velocidade)
            cano_baixo.atualizar(cano_velocidade)
            cano_x = cano_cima.rect.x
                
            if cano_x < -cano_largura:
                cano_x = LARGURA_TELA  
                altura_cano_cima, altura_cano_baixo = gerar_alturas_canos(ALTURA_TELA, chao_altura, espaco_entre_canos)

                cano_cima = Cano(cano_x, altura_cano_cima, imagens['cano'], de_cima=True)
                cano_baixo = Cano(cano_x, chao_y - altura_cano_baixo, imagens['cano'], de_cima=False)
            
                pontos = calcular_pontos(pontos, 1)
            
            # Atualização do movimento do chão
            chao_x -= cano_velocidade
            if chao_x <= -LARGURA_TELA:
                chao_x = 0
            
            # Verificação de colisões
            bateu_no_chao = verificar_colisao(passaro.rect, chao_rect)
            bateu_no_teto = passaro.rect.top <= 0
            bateu_no_cano = verificar_colisao(passaro.rect, cano_cima.rect) or verificar_colisao(passaro.rect, cano_baixo.rect)
            
            if bateu_no_chao or bateu_no_teto or bateu_no_cano:
                vidas = tomar_dano(vidas, 1)

                if jogador_perdeu(vidas):
                    if bateu_no_chao:
                        passaro.rect.bottom = chao_rect.top
                    estado_jogo = "GAME_OVER"
                    if pontos > recorde:
                        recorde = pontos
                        salvar_recorde(CAMINHO_RECORDE, recorde)
                else:
                    # Resetar posição para continuar com a próxima vida
                    passaro.rect.y = ALTURA_TELA // 4
                    passaro.velocidade_y = 0
                    cano_x = LARGURA_TELA
                    cano_cima = Cano(cano_x, altura_cano_cima, imagens['cano'], de_cima=True)
                    cano_baixo = Cano(cano_x, chao_y - altura_cano_baixo, imagens['cano'], de_cima=False)
                    tempo_inicio_partida = pygame.time.get_ticks()

        # Renderização
        tela.blit(imagem_fundo, (0, 0))
        
        tela.blit(passaro.image, passaro.rect)
        tela.blit(cano_cima.image, cano_cima.rect)
        tela.blit(cano_baixo.image, cano_baixo.rect)
        
        tela.blit(imagem_chao, (chao_x, chao_y))
        tela.blit(imagem_chao, (chao_x + LARGURA_TELA, chao_y))
 
        # Renderização da interface (HUD)
        texto_pontos = fonte_instrucoes.render(f"Pontos: {pontos}", True, (255, 255, 255))
        texto_recorde = fonte_instrucoes.render(f"Recorde: {recorde}", True, (255, 255, 0))
        texto_timer = fonte_instrucoes.render(f"Tempo: {tempo_segundos}s", True, (255, 255, 255))
        
        tela.blit(texto_pontos, (20, 20))
        tela.blit(texto_recorde, (20, 50))
        tela.blit(texto_timer, (LARGURA_TELA - 160, 20))

        # Desenha os corações das vidas
        for i in range(vidas):
            tela.blit(imagens['coracao'], (LARGURA_TELA - 40 - (i * 35), 60))

        # A mensagem depois de colidir/morrer
        if estado_jogo == "GAME_OVER":
            texto_morte = fonte_game_over.render("GAME OVER!", True, (255, 50, 50))
            texto_reiniciar = fonte_instrucoes.render("Aperte a tecla ESPAÇO para tentar de novo!", True, (255, 255, 255))

            # Centraliza as mensagens nas telas
            tela.blit(texto_morte, (LARGURA_TELA // 2 - texto_morte.get_width() // 2, ALTURA_TELA // 2 - 50))
            tela.blit(texto_reiniciar, (LARGURA_TELA // 2 - texto_reiniciar.get_width() // 2, ALTURA_TELA // 2 + 20))
        
        # Tela de inicio
        if estado_jogo == "INICIO":
            texto_inicio = fonte_game_over.render("FLAPPY BIRD", True, (255, 255, 255))
            texto_instrucao = fonte_instrucoes.render("Aperte a tecla ESPAÇO para começar", True, (255, 255, 0))
            
            # Centraliza as mensagens nas telas no começo do jogo
            tela.blit(texto_inicio, (LARGURA_TELA // 2 - texto_inicio.get_width() // 2, ALTURA_TELA // 2 - 60))
            tela.blit(texto_instrucao, (LARGURA_TELA // 2 - texto_instrucao.get_width() // 2, ALTURA_TELA // 2 + 10))
        pygame.display.flip()
 
    pygame.quit()