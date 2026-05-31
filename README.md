# Flappy Py

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Lucas Gomes Esteves Da Silva
- Rafael Felipe Oliveira do Espirito Santo
- Yandi Orlando Santos Rivero
- Nicolas Rodrigues Bessa de Almeida

## Tipo de Jogo
Arcade / Endless Runner 2D (Progressão lateral contínua).

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

Trata-se de um jogo 2D de desviar de obstáculos com progressão lateral contínua. O cenário se move constantemente da direita para a esquerda, criando a ilusão de que o personagem principal está voando para a frente. O jogador precisa desviar de obstáculos posicionados no teto e no chão, cujos espaçamentos e alturas variam.

## Objetivo do jogador

O objetivo é sobreviver pelo maior tempo possível e acumular a maior pontuação possível, atravessando com sucesso as frestas entre os obstáculos gerados e superando o seu próprio recorde.

## Condições de Vitória e Derrota

- **Condição de Vitória:** Por ser um jogo infinito, não há um fim. A "vitória" consiste em superar em bater seu próprio recorde.
- **Condição de Derrota:** O jogo encerra imediatamente caso o personagem colida com o chão ou com qualquer parte dos obstáculos.

## Regras do jogo

- O personagem está sujeito a uma força de gravidade constante que o puxa para baixo.
- O jogador deve acionar um comando de pulo para vencer a gravidade momentaneamente e ganhar altitude.
- Cada par de obstáculos ultrapassado com sucesso concede **1 ponto** ao jogador.

## Elementos Previstos

- **Personagem:** Entidade principal com animação simples controlada pelo jogador.
- **Obstáculos:** Colunas geradas em pares (cima e baixo).
- **Cenário:** Fundo em movimento e chão sólido.
- **Interface (UI):** Tela de Início, Contador de Pontuação na tela principal e Tela de *Game Over*.

## Controles

- **Barra de Espaço** / **Seta para Cima** / **Clique Esquerdo do Mouse**: Realizar a ação de "pular" (voar para cima).
- **ESC**: Sair do jogo.

## Estruturas de Dados e Arquivos Previstos

- **Estruturas de Dados:**
  - **Listas:** Para gerenciar o agrupamento, renderização e remoção dos obstáculos que entram e saem da tela.
  - **Dicionários:** Para gerenciar os estados do jogo (ex: menu, em andamento, game over).
  - **Tuplas:** Para definições de cores (RGB) e vetores de posição bidimensionais $(x, y)$.
- **Uso de Arquivos:**
  - **Mídia:** Imagens `.png` (sprites) e áudios `.wav` ou `.mp3` (efeitos sonoros).
  - **Dados:** Arquivo de texto `.txt` ou `.json` armazenado na pasta `data/` para salvar permanentemente a pontuação máxima.

## Planejamento Técnico

### Testes Planejados
- **Hitboxes (Colisões):** Garantir que a área de colisão do pássaro e dos obstáculos seja precisa, evitando mortes injustas.
- **Geração Procedural:** Testar a lógica de espaçamento para garantir que a distância entre os obstáculos inferior e superior sempre permita a passagem do personagem.

### Principais Dificuldades Esperadas
- Calibrar a física do jogo (peso da gravidade *versus* a força do pulo) para que a jogabilidade seja fluida.
- Gerenciar corretamente o uso de memória, removendo obstáculos que já saíram da tela para evitar quedas de desempenho (FPS).

### Escopo Mínimo para Entrega Final
- Personagem com física de gravidade e comando de pulo funcionais.
- Geração contínua de obstáculos na tela com frestas aleatórias.
- Sistema de detecção de colisão que encerra a partida corretamente.
- Sistema de pontuação visual e atualizado em tempo real.

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
