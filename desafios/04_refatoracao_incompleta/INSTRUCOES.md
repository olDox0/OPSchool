# Desafio 04: A Refatoração Incompleta (TypeError)

## O Cenário
Este script (`processador_texto.py`) deveria processar uma frase. No entanto, ele falha com um erro que pode não ser óbvio à primeira vista. A mensagem de erro exata pode variar, mas o problema é um `TypeError` implícito.

A função `split_text` foi atualizada para retornar uma lista de palavras. A função `print_word_lengths`, no entanto, ainda espera receber uma única string.

## Sua Missão
Seu objetivo é corrigir a função `print_word_lengths` para que ela funcione corretamente com a **lista** de palavras que ela agora recebe. O programa deve imprimir o comprimento de **cada palavra individualmente**.

## Pistas
1.  O que a função `split_text` retorna? Use `print(type(dados_processados))` para descobrir.
2.  A função `print_word_lengths` recebe uma lista. Como podemos executar uma ação para cada item de uma lista? (Lembre-se da nossa lição sobre loops).
3.  Você precisará de um loop `for` dentro de `print_word_lengths`.

Consulte `solucao.md` se precisar de ajuda.