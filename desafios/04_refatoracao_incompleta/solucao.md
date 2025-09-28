# Solução do Desafio 04: A Refatoração Incompleta

## O Diagnóstico
O problema aqui é um erro de "contrato quebrado" entre duas funções. A função `split_text` foi refatorada e mudou o tipo de dado que ela retorna (de `string` para `list`). No entanto, a função `print_word_lengths`, que consome esse dado, não foi atualizada para lidar com o novo formato.

Isso causa um `TypeError` lógico: estamos tentando usar uma lista como se fosse uma string. `len()` em uma lista nos dá o número de itens, não o comprimento do texto total, e não nos permite ver o comprimento de cada palavra.

## O Processo de Correção
A solução é modificar a função `print_word_lengths` para que ela saiba como lidar com uma lista, usando um loop `for` para iterar sobre cada palavra.

**Código Corrigido (`processador_texto.py`):**
```python
def split_text(text):
    return text.lower().split()

def print_word_lengths(word_list): # Nome do parâmetro alterado para clareza
    """
    Esta função agora aceita uma lista de palavras e imprime o
    comprimento de cada uma.
    """
    print("--- Comprimento das Palavras ---")
    for word in word_list:
        print(f"A palavra '{word}' tem {len(word)} letras.")

if __name__ == "__main__":
    frase = "Python e divertido de aprender"
    dados_processados = split_text(frase)
    print_word_lengths(dados_processados)