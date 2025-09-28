# O objetivo deste programa é pegar uma frase, dividi-la em palavras,
# e depois imprimir o comprimento de cada palavra.
# Uma refatoração foi feita na função `split_text`, mas a função
# `print_word_lengths` não foi atualizada para lidar com a mudança.

def split_text(text):
    """
    Refatorado: Agora retorna uma lista de palavras em minúsculas.
    Versão antiga retornava uma única string em maiúsculas.
    """
    return text.lower().split()

def print_word_lengths(text_data):
    """
    Esta função espera receber uma única string, mas agora recebe
    uma lista da função split_text, causando um erro.
    """
    # ERRO: len() em uma lista retorna o número de itens, não o
    # comprimento do texto.
    print(f"Comprimento total do texto: {len(text_data)}")

if __name__ == "__main__":
    frase = "Python e divertido de aprender"
    
    dados_processados = split_text(frase)
    
    # Esta chamada vai quebrar, pois passamos uma lista para uma
    # função que espera uma string.
    print_word_lengths(dados_processados)