# Solução do Desafio 06: O Último da Fila

## O Diagnóstico
O `IndexError` é um dos erros mais comuns ao trabalhar com listas. Ele ocorre porque, em Python (e na maioria das linguagens de programação), a indexação de listas começa em **zero**.

Para uma lista com 3 itens, como `["Maçã", "Banana", "Laranja"]`:
*   O índice de "Maçã" é `0`.
*   O índice de "Banana" é `1`.
*   O índice de "Laranja" é `2`.

A função `len()` nos diz que há `3` itens. O código tentou acessar o índice `3`, que está fora dos limites da lista, causando o erro.

## O Processo de Correção
A regra para encontrar o último índice de qualquer lista é: **`comprimento da lista - 1`**.

**Código Corrigido (`processador_lista.py`):**
```python
def get_last_item(items):
    """
    Retorna corretamente o último item da lista.
    """
    # O último índice é sempre o comprimento menos 1.
    last_index = len(items) - 1
    return items[last_index]

if __name__ == "__main__":
    frutas = ["Maçã", "Banana", "Laranja"]
    print(f"A lista tem {len(frutas)} frutas.")
    
    ultima_fruta = get_last_item(frutas)
    print(f"A última fruta é: {ultima_fruta}")
	
Dica de Profissional: Python tem um atalho para isso! O índice -1 sempre se refere ao último item, -2 ao penúltimo, e assim por diante. A solução mais "Pythônica" seria:
code
Python
def get_last_item_pythonic(items):
    return items[-1]```
**Conclusão da Lição:** Lembre-se sempre: a contagem em Python começa em zero. O último índice válido é sempre `len(lista) - 1`.