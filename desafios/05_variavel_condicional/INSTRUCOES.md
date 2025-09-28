# Desafio 05: A Variável Condicional (UnboundLocalError)

## O Cenário
Este script (`validador.py`) possui uma função que valida números. Curiosamente, ele funciona perfeitamente quando o número é negativo, mas quebra com o seguinte erro quando o número é positivo:

`UnboundLocalError: cannot access local variable 'error_message' where it is not associated with a value`

## Sua Missão
Seu objetivo é corrigir a função `validate_number` para que ela funcione tanto para números positivos quanto negativos, sem alterar a lógica principal.

## Pistas
1.  O erro `UnboundLocalError` acontece porque você está tentando usar uma variável que, em alguns caminhos do seu código, nunca foi criada.
2.  Observe a variável `error_message`. Em que condição ela é criada?
3.  O que acontece se a condição `number < 0` for falsa? A variável `error_message` chega a existir?
4.  Como você pode garantir que `error_message` sempre tenha um valor inicial no início da função?

Consulte `solucao.md` se precisar de ajuda.