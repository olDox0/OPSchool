# Desafio 01: O Ambiente Quebrado

## O Cenário
Você recebeu este script (`programa.py`) de um colega. Ele deveria imprimir uma mensagem de sucesso em verde. No entanto, ao tentar executá-lo com `python programa.py`, você recebe o seguinte erro:
Traceback (most recent call last):
File ".../programa.py", line 8, in <module>
import click
ModuleNotFoundError: No module named 'click'

## Sua Missão
Seu objetivo é fazer o programa rodar com sucesso, sem modificar o código do `programa.py`. Você precisa consertar o **ambiente** para que o programa funcione.

## Pistas
1.  O erro `ModuleNotFoundError` significa que o Python não conseguiu encontrar a biblioteca `click`. Como instalamos bibliotecas em Python?
2.  Existe um arquivo `requirements.txt`. O que o comando `pip install -r requirements.txt` faz?
3.  Lembre-se da nossa lição sobre Ambientes Virtuais. O erro está acontecendo porque a biblioteca está faltando no seu `venv` ou no seu Python Global?
4.  Qual ferramenta do `doxoade` usamos para verificar se nosso ambiente está consistente? Tente rodá-la.

Quando o programa imprimir a mensagem em verde, você terá concluído o desafio! Consulte `solucao.md` se precisar de ajuda.
