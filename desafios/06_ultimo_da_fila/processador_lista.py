# O objetivo deste programa é acessar e imprimir o último item de uma lista.
# No entanto, ele comete um erro comum sobre como os índices funcionam.

def get_last_item(items):
    """
    Tenta retornar o último item da lista.
    """
    # ERRO: A lista tem 3 itens, mas os índices são 0, 1, e 2.
    # Não existe um índice 3.
    last_index = len(items)
    return items[last_index]

if __name__ == "__main__":
    frutas = ["Maçã", "Banana", "Laranja"]
    print(f"A lista tem {len(frutas)} frutas.")
    
    # Esta chamada vai quebrar com um IndexError.
    ultima_fruta = get_last_item(frutas)
    print(f"A última fruta é: {ultima_fruta}")