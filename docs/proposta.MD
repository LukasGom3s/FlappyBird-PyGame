# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> Flappy Py

## 2. Integrantes do grupo

- Nome 1: Lucas Gomes Esteves Da Silva
- Nome 2: Rafael Felipe Oliveira do Espirito Santo
- Nome 3: Yandi Orlando Santos Rivero
- Nome 4: Nicolas Rodrigues Bessa de Almeida

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Jogo de desviar de obstáculos.

## 4. Descrição geral do jogo

Descrição:

> O jogo consiste em um cenário de rolagem lateral contínua (da direita para a esquerda). O jogador controla um personagem com gravidade que deve voar através de frestas entre pares de obstáculos que surgem no teto e no chão. O desafio é calcular o tempo exato dos pulos para não bater nos obstáculos ou cair no chão.

## 5. Objetivo do jogador

Objetivo:

> Sobreviver pelo maior tempo possível e superar a sua pontuação máxima anterior, atravessando os obstáculos com sucesso.

## 6. Regras principais

Regras do grupo:

- Regra 1: O personagem é constantemente puxado para baixo pela gravidade.
- Regra 2: O comando do jogador faz o personagem dar um pequeno salto, ganhando altitude.
- Regra 3: Passar com sucesso por um par de obstáculos concede 1 ponto ao jogador.
- Regra 4: Bater em qualquer obstáculo ou no chão encerra a partida imediatamente.

## 7. Condição de vitória

Condição de vitória:

> Por ser um jogo de sobrevivência infinita, não há uma tela de "Você Venceu". A vitória do jogador consiste em sobreviver o suficiente para quebrar o seu próprio recorde anterior.

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

> A partida termina instantaneamente se o jogador colidir a caixa de colisão do personagem contra qualquer um dos obstacúlos ou contra o chão.

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

Descrição:

> Um pássaro (com física de gravidade), com o qual você pode usar o botão esquerdo do mouse, a tecla espaço ou as setinhas do teclado para pular, movimentando ele um pouco para cima. 

## Obstáculos, inimigos ou desafios

Descrição:

> Colunas/canos gerados em pares (um vindo do teto e outro do chão), os quais começam a vir mais rapidamente na direção do jogador com o passar o tempo. 

## Itens, alvos ou objetos de interação

Descrição:

> Não haverá coleta de itens. A interação se dá puramente pelas frestas entre os obstáculos, que ativam o registro de pontuação ao serem cruzadas.

## Pontuação, vidas, tempo ou progresso

Descrição:

> O jogador possui apenas 1 "vida" (colisão = morte). A pontuação é incrementada de 1 em 1 a cada obstáculo superado e o progresso é infinito até a derrota.

## 10. Controles previstos

Controles do grupo:

- Espaço: pular (voar para cima)
- Seta para Cima: pular (voar para cima)
- Clique Esquerdo do Mouse: pular (voar para cima)
- ESC: sair do jogo

## 11. Organização inicial do código

Organização planejada:

> - `main.py`: inicia o jogo e gerencia o menu;
> - `src/jogo.py`: contém o loop principal, a física e a geração de obstáculos;
> - `src/sprites.py`: contém as classes do personagem e dos canos;
> - `src/config.py`: guarda configurações como tamanho da tela, gravidade e cores;
> - `data/`: pasta para armazenar o arquivo de recorde de pontuação;
> - `src/dados.py`: gerencia o armazenamento de recordes;
> - `assets/`: pasta para armazenar imagens e sons.

## 12. Recursos externos previstos

Recursos previstos:

> - Imagens e *sprites* obtidos de bancos gratuitos voltados para *pixel art*, *assets* de jogos (estilo Flappy Bird) e Sprites pessoais feitos por membros do grupo.
> - Efeitos sonoros gratuitos para pulo, marcação de ponto e colisão.
> - Fontes personalizadas para exibição de texto retro/arcade.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Dificuldade 1: Implementar uma gravidade e pulo que pareçam fluídos e respondam bem aos comandos.
- Dificuldade 2: Lógica de geração procedural para garantir que os canos apareçam com um espaço ultrapassável.
- Dificuldade 3: Ajuste preciso das hitboxes para não gerar mortes injustas.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima exigida conterá um quadrado ou imagem básica representando o pássaro caindo por gravidade e pulando, retângulos simples funcionando como os canos vindo da direita, detecção de colisão parando o jogo e a exibição da pontuação atual na tela.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: Implementar sistema persistente de *High Score* salvando e lendo a partir de um arquivo externo (`.txt` ou `.json`). ( FEITO )
- Melhoria 2: Animação do pássaro batendo as asas (troca de *sprites*). ( FEITO )
- Melhoria 3: Menus estilizados (Tela Inicial e Tela de *Game Over*). ( FEITO )
