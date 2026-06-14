# Flappy Py

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Lucas Gomes Esteves Da Silva

- Rafael Felipe Oliveira do Espirito Santo

- Yandi Orlando Santos Rivero

- Nicolas Rodrigues Bessa de Almeida

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.

- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).

- `assets/`: imagens, fontes e sons.

- `data/`: arquivos persistentes (recorde/ranking).

- `tests/`: testes unitários com `pytest`.

- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Trata-se de um jogo 2D de desviar de obstáculos com progressão lateral contínua. O cenário se move constantemente da direita para a esquerda, criando a ilusão de que o personagem principal está voando para a frente. O jogador precisa desviar de obstáculos posicionados a frente dele, cujos espaçamentos e alturas variam.

## Objetivo do jogador

O objetivo é sobreviver pelo maior tempo possível e acumular a maior pontuação possível, atravessando com sucesso os obstáculos gerados e superando seu próprio recorde.

## Regras do jogo

- O personagem está sujeito a uma força de gravidade constante que o puxa para baixo.

- O jogador deve acionar um comando de pulo para vencer a gravidade momentaneamente e ganhar altitude, clicando espaço no teclado.

- Cada par de obstáculos ultrapassado com sucesso concede 1 ponto ao jogador.

- O personagem possui 3 vidas. Cada colisão com um obstáculo, com o chão ou com o teto consome uma vida.

- O jogo termina quando todas as vidas do personagem se esgotam.

## Controles

- **Barra de Espaço**: Realizar a ação de "pular" (voar para cima). No início da partida, também inicia o jogo; na tela de Game Over, reinicia uma nova partida.

- **ESC**: Sair do jogo.

## Como executar o projeto

### 1. Clonar o repositório

```bash

git clone LINK_DO_REPOSITORIO

cd NOME_DA_PASTA

pip install -r requirements.txt

python main.py

```