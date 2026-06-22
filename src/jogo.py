import os
import pygame

from .config import (LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JANELA, CAMINHO_RECORDE)
from .funcoes import (verificar_colisao, gerar_alturas_canos, carregar_imagens, calcular_pontos, tomar_dano, jogador_perdeu)
from .dados import carregar_recorde, salvar_recorde
from .sprites import Passaro, Cano

# Configurações de dificuldade
VELOCIDADE_INICIAL = 3
VELOCIDADE_MAXIMA = 7
INCREMENTO_VELOCIDADE_POR_SEGUNDO = 0.03


def criar_par_canos(x, altura_tela, chao_y, chao_altura, espaco_entre_canos, imagem_cano):
    """Cria um novo par de canos (cima/baixo) na posição x informada."""
    altura_cano_cima, altura_cano_baixo = gerar_alturas_canos(altura_tela, chao_altura, espaco_entre_canos)
    cano_cima = Cano(x, altura_cano_cima, imagem_cano, de_cima=True)
    cano_baixo = Cano(x, chao_y - altura_cano_baixo, imagem_cano, de_cima=False)
    return {"cima": cano_cima, "baixo": cano_baixo, "pontuado": False}


def executar_jogo():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    som_pulo = pygame.mixer.Sound("assets/sons/som_pulo.mp3")
    som_ponto = pygame.mixer.Sound("assets/sons/som_ponto.mp3")
    som_gameover = pygame.mixer.Sound("assets/sons/som_gameover.mp3")

    diretorio_dados = os.path.dirname(CAMINHO_RECORDE)
    if diretorio_dados and not os.path.exists(diretorio_dados):
        os.makedirs(diretorio_dados)

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JANELA)

    fonte_game_over = pygame.font.SysFont('arial', 50, bold=True)
    fonte_instrucoes = pygame.font.SysFont('arial', 30)
    fonte_menu = pygame.font.SysFont('arial', 40, bold=True)  # fonte do menu

    # Configurações dos canos
    cano_largura = 80
    espaco_entre_canos = 190       # espaço vertical pra passar (aumentado de 150 -> 190)
    distancia_entre_canos = 450    # distância horizontal entre um cano e o próximo (mais "apertado")
    cano_velocidade = VELOCIDADE_INICIAL

    # Configurações do chão
    chao_altura = ALTURA_TELA // 4
    chao_y = ALTURA_TELA - chao_altura
    chao_rect = pygame.Rect(0, chao_y, LARGURA_TELA, chao_altura)
    chao_x = 0

    imagens = carregar_imagens(chao_altura, cano_largura)
    pygame.display.set_icon(imagens['icone'])

    relogio = pygame.time.Clock()

    passaro = Passaro(50, ALTURA_TELA // 4, imagens['passaro'])

    pontos = 0
    vidas = 3
    tempo_segundos = 0
    tempo_inicio_partida = 0
    recorde = carregar_recorde(CAMINHO_RECORDE)
    novo_recorde = False


    def reiniciar_canos():
        """Cria a lista inicial de canos, já espaçados horizontalmente pela tela."""
        lista = []
        x = LARGURA_TELA
        for _ in range(3):
            lista.append(criar_par_canos(x, ALTURA_TELA, chao_y, chao_altura, espaco_entre_canos, imagens['cano']))
            x += distancia_entre_canos
        return lista

    canos = reiniciar_canos()

    estado_jogo = "MENU"  # começa no menu agora
    opcao_menu = 0        # 0 = Jogar, 1 = Ranking, 2 = Sair
    em_ranking = False

    rodando = True
    while rodando:
        relogio.tick(FPS)

        # Processamento de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            # Mouse
            if estado_jogo == "MENU" and not em_ranking:
                opcoes_mouse = ["JOGAR", "RANKING", "SAIR"]
                
                # Movimento do mouse
                if evento.type == pygame.MOUSEMOTION:
                    for i, texto in enumerate(opcoes_mouse):
                        largura, altura = fonte_menu.size(texto)
                        rect_x = LARGURA_TELA // 2 - largura // 2
                        rect_y = ALTURA_TELA // 2 - 60 + i * 70
                        rect_opcao = pygame.Rect(rect_x, rect_y, largura, altura)
                        
                        if rect_opcao.collidepoint(evento.pos):
                            opcao_menu = i

                # Clique do mouse
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    for i, texto in enumerate(opcoes_mouse):
                        largura, altura = fonte_menu.size(texto)
                        rect_x = LARGURA_TELA // 2 - largura // 2
                        rect_y = ALTURA_TELA // 2 - 60 + i * 70
                        rect_opcao = pygame.Rect(rect_x, rect_y, largura, altura)
                        
                        if rect_opcao.collidepoint(evento.pos):
                            if i == 0:  # Jogar
                                passaro.rect.y = ALTURA_TELA // 4
                                passaro.velocidade_y = 0
                                canos = reiniciar_canos()
                                cano_velocidade = VELOCIDADE_INICIAL
                                pontos = 0
                                vidas = 3
                                estado_jogo = "INICIO"
                            elif i == 1:  # Ranking
                                em_ranking = True
                            elif i == 2:  # Sair
                                rodando = False
            # -----------------------------------------------

            if evento.type == pygame.KEYDOWN:
                if estado_jogo == "MENU":
                    if em_ranking:
                        if evento.key in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_ESCAPE):
                            em_ranking = False
                    else:
                        if evento.key == pygame.K_UP:
                            opcao_menu = (opcao_menu - 1) % 3
                        elif evento.key == pygame.K_DOWN:
                            opcao_menu = (opcao_menu + 1) % 3
                        elif evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                            if opcao_menu == 0:  # Jogar
                                passaro.rect.y = ALTURA_TELA // 4
                                passaro.velocidade_y = 0
                                canos = reiniciar_canos()
                                cano_velocidade = VELOCIDADE_INICIAL
                                pontos = 0
                                vidas = 3
                                estado_jogo = "INICIO"
                            elif opcao_menu == 1:  # Ranking
                                em_ranking = True
                            elif opcao_menu == 2:  # Sair
                                rodando = False
                        elif evento.key == pygame.K_ESCAPE:
                            rodando = False

                elif estado_jogo == "INICIO":
                    if evento.key == pygame.K_SPACE:
                        passaro.pular()
                        som_pulo.play()
                        tempo_inicio_partida = pygame.time.get_ticks()
                        estado_jogo = "JOGANDO"
                    elif evento.key == pygame.K_ESCAPE:
                        estado_jogo = "MENU"

                elif estado_jogo == "JOGANDO":
                    if evento.key == pygame.K_SPACE:
                        passaro.pular()
                        som_pulo.play()
                    elif evento.key == pygame.K_ESCAPE:
                        estado_jogo = "MENU"

                elif estado_jogo == "GAME_OVER":
                    if evento.key == pygame.K_SPACE:
                        passaro.rect.y = ALTURA_TELA // 4
                        passaro.velocidade_y = 0
                        canos = reiniciar_canos()
                        cano_velocidade = VELOCIDADE_INICIAL
                        pontos = 0
                        vidas = 3
                        tempo_inicio_partida = pygame.time.get_ticks()
                        estado_jogo = "JOGANDO"
                    elif evento.key == pygame.K_ESCAPE:
                        estado_jogo = "MENU"

        if estado_jogo == "JOGANDO":
            tempo_segundos = (pygame.time.get_ticks() - tempo_inicio_partida) // 1000

            # Progressão gradual da velocidade dos canos, com limite máximo
            cano_velocidade = min(
                VELOCIDADE_MAXIMA,
                VELOCIDADE_INICIAL + tempo_segundos * INCREMENTO_VELOCIDADE_POR_SEGUNDO
            )

            # Passarinho
            passaro.atualizar()

            # Canos
            for par in canos:
                par["cima"].atualizar(cano_velocidade)
                par["baixo"].atualizar(cano_velocidade)

            # Quando o cano mais à esquerda sai da tela, remove ele e cria outro no final
            if canos[0]["cima"].rect.x < -cano_largura:
                canos.pop(0)
                x_ultimo = canos[-1]["cima"].rect.x
                canos.append(
                    criar_par_canos(x_ultimo + distancia_entre_canos, ALTURA_TELA, chao_y, chao_altura, espaco_entre_canos, imagens['cano'])
                )

            # Atualização do movimento do chão
            chao_x -= cano_velocidade
            if chao_x <= -LARGURA_TELA:
                chao_x = 0

            # Pontuação: assim que o passarinho passa pelo cano
            for par in canos:
                if not par["pontuado"] and par["cima"].rect.right < passaro.rect.left:
                    pontos = calcular_pontos(pontos, 1)
                    par["pontuado"] = True
                    som_ponto.play()

            # Verificação de colisões
            bateu_no_chao = verificar_colisao(passaro.rect, chao_rect)
            bateu_no_teto = passaro.rect.top <= 0
            bateu_no_cano = any(
                verificar_colisao(passaro.rect, par["cima"].rect) or verificar_colisao(passaro.rect, par["baixo"].rect)
                for par in canos
            )

            if bateu_no_chao or bateu_no_teto or bateu_no_cano:
                som_gameover.play()
                vidas = tomar_dano(vidas, 1)

                if jogador_perdeu(vidas):
                    if bateu_no_chao:
                        passaro.rect.bottom = chao_rect.top
                    estado_jogo = "GAME_OVER"
                    som_gameover.play()
                    if pontos > recorde:
                        recorde = pontos
                        novo_recorde = True
                        salvar_recorde(CAMINHO_RECORDE, recorde)
                else:
                    passaro.rect.y = ALTURA_TELA // 4
                    passaro.velocidade_y = 0
                    canos = reiniciar_canos()
                    tempo_inicio_partida = pygame.time.get_ticks()

        # Renderização
        tela.blit(imagens['fundo'], (0, 0))

        if estado_jogo == "MENU":
            if em_ranking:
                texto_ranking = fonte_game_over.render("RANKING", True, (255, 255, 0))
                texto_recorde_val = fonte_game_over.render(f"Recorde: {recorde}", True, (255, 255, 255))
                texto_voltar = fonte_instrucoes.render("ESC ou ESPAÇO para voltar", True, (200, 200, 200))
                tela.blit(texto_ranking,     (LARGURA_TELA // 2 - texto_ranking.get_width()     // 2, ALTURA_TELA // 2 - 100))
                tela.blit(texto_recorde_val, (LARGURA_TELA // 2 - texto_recorde_val.get_width() // 2, ALTURA_TELA // 2))
                tela.blit(texto_voltar,      (LARGURA_TELA // 2 - texto_voltar.get_width()      // 2, ALTURA_TELA // 2 + 80))
            else:
                opcoes = ["JOGAR", "RANKING", "SAIR"]
                titulo = fonte_game_over.render("FLAPPY BIRD", True, (255, 255, 0))
                tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, ALTURA_TELA // 2 - 160))
                for i, texto in enumerate(opcoes):
                    cor = (255, 255, 0) if i == opcao_menu else (255, 255, 255)
                    superficie = fonte_menu.render(texto, True, cor)
                    tela.blit(superficie, (LARGURA_TELA // 2 - superficie.get_width() // 2, ALTURA_TELA // 2 - 60 + i * 70))

        else:
            tela.blit(passaro.image, passaro.rect)
            for par in canos:
                tela.blit(par["cima"].image, par["cima"].rect)
                tela.blit(par["baixo"].image, par["baixo"].rect)

            tela.blit(imagens['chao'], (chao_x, chao_y))
            tela.blit(imagens['chao'], (chao_x + LARGURA_TELA, chao_y))

            # HUD
            texto_pontos = fonte_instrucoes.render(f"Pontos: {pontos}", True, (255, 255, 255))
            texto_recorde = fonte_instrucoes.render(f"Recorde: {recorde}", True, (255, 255, 0))
            texto_timer = fonte_instrucoes.render(f"Tempo: {tempo_segundos}s", True, (255, 255, 255))

            tela.blit(texto_pontos, (20, 20))
            tela.blit(texto_recorde, (20, 50))
            tela.blit(texto_timer, (LARGURA_TELA - 160, 20))

            for i in range(vidas):
                tela.blit(imagens['coracao'], (LARGURA_TELA - 40 - (i * 35), 60))

            if estado_jogo == "GAME_OVER":
                overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
                overlay.set_alpha(180)
                overlay.fill((0,0,0))
                tela.blit(overlay,(0,0))

                caixa = pygame.Rect(LARGURA_TELA//2-320, ALTURA_TELA//2-150, 640, 300)
                pygame.draw.rect(tela,(40,40,40),caixa,border_radius=15)
                pygame.draw.rect(tela,(255,255,255),caixa,3,border_radius=15)

                texto_morte = fonte_game_over.render("GAME OVER!", True, (255, 50, 50))
                texto_pts = fonte_instrucoes.render(f"Pontos: {pontos}", True, (255,255,255))
                texto_rec = fonte_instrucoes.render(f"Recorde: {recorde}", True, (255,255,0))
                texto_reiniciar = fonte_instrucoes.render("ESPACO = jogar novamente | ESC = menu", True, (255,255,255))

                tela.blit(texto_morte,(LARGURA_TELA//2-texto_morte.get_width()//2, ALTURA_TELA//2-120))
                tela.blit(texto_pts,(LARGURA_TELA//2-texto_pts.get_width()//2, ALTURA_TELA//2-40))
                tela.blit(texto_rec,(LARGURA_TELA//2-texto_rec.get_width()//2, ALTURA_TELA//2))
                if novo_recorde:
                    nr = fonte_instrucoes.render("NOVO RECORDE!", True, (255,215,0))
                    tela.blit(nr,(LARGURA_TELA//2-nr.get_width()//2, ALTURA_TELA//2+40))
                tela.blit(texto_reiniciar,(LARGURA_TELA//2-texto_reiniciar.get_width()//2, ALTURA_TELA//2+90))

            if estado_jogo == "INICIO":
                texto_inicio = fonte_game_over.render("FLAPPY BIRD", True, (255, 255, 255))
                texto_instrucao = fonte_instrucoes.render("Aperte a tecla ESPAÇO para começar", True, (255, 255, 0))
                tela.blit(texto_inicio, (LARGURA_TELA // 2 - texto_inicio.get_width() // 2, ALTURA_TELA // 2 - 60))
                tela.blit(texto_instrucao, (LARGURA_TELA // 2 - texto_instrucao.get_width() // 2, ALTURA_TELA // 2 + 10))

        pygame.display.flip()

    pygame.quit()