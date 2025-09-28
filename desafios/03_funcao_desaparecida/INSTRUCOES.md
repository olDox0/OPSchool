# Desafio 03: A Função Desaparecida (AttributeError)

## O Cenário
Este script (`app_quebrada.py`) deveria criar um objeto e imprimir mensagens de sucesso. No entanto, ao executá-lo, o programa quebra com o seguinte erro:

Traceback (most recent call last):
File ".../app_quebrada.py", line 22, in <module>
app = SimpleApp()
File ".../app_quebrada.py", line 12, in init
self.setup_widgets()
AttributeError: 'SimpleApp' object has no attribute 'setup_widgets'


## Sua Missão
Seu objetivo é fazer o programa rodar até o fim e imprimir "Aplicativo configurado com sucesso!", modificando **apenas** o script `app_quebrada.py`.

## Pistas
1.  O `traceback` é seu melhor amigo. Ele diz exatamente em qual linha o erro aconteceu.
2.  O erro é `AttributeError`. Ele está dizendo que tentou encontrar o atributo `setup_widgets` no objeto `SimpleApp`, mas não encontrou.
3.  Olhe o código da classe `SimpleApp`. Existe uma função (`def`) chamada `setup_widgets`? O que aconteceu com ela?

Consulte `solucao.md` se precisar de ajuda.