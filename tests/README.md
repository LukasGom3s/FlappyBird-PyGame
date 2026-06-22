# Testes
 
Esta pasta contém testes automatizados do projeto.
 
## Arquivos
 
- `test_logica.py`: valida funções puras de lógica em `src/funcoes.py` (pontuação, colisão, vidas, canos).
- `test_sprites.py`: valida o comportamento das classes `Passaro` e `Cano` em `src/sprites.py` (movimento, gravidade, posicionamento).

## Como executar
 
```bash
python -m pytest
```
## Boas praticas

- Crie testes para toda regra de pontuacao, vidas e condicoes de fim de jogo.
- Prefira funcoes pequenas e testaveis no modulo `src/funcoes.py`.
