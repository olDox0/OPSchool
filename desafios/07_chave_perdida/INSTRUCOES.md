# Desafio 07: A Chave Perdida (KeyError)

## O Cenário
Este script (`config_quebrada.py`) deveria ler e imprimir o nome do usuário de um dicionário de configuração. No entanto, ele quebra com o seguinte erro:

`KeyError: 'usuario'`

## Sua Missão
Seu objetivo é corrigir a função `get_user_config` para que ela retorne o nome do usuário ("olDox222") corretamente.

## Pistas
1.  O erro `KeyError` é para dicionários o que o `IndexError` é para listas. Ele significa que você tentou usar uma chave que não existe no dicionário.
2.  Observe o dicionário `configuracao`. Quais são as chaves exatas que ele possui?
3.  Observe a função `get_user_config`. Qual chave ela está tentando acessar? Há alguma diferença?

Consulte `solucao.md` se precisar de ajuda.