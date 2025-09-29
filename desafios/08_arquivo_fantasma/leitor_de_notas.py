# O objetivo deste programa é ler e exibir o conteúdo de um arquivo de texto
# chamado 'notas.txt'. No entanto, o arquivo não existe.

def read_notes():
    """
    Tenta abrir, ler e retornar o conteúdo de 'notas.txt'.
    """
    # ERRO: O programa vai quebrar aqui porque o arquivo 'notas.txt'
    # não foi encontrado no mesmo diretório.
    with open("notas.txt", "r", encoding="utf-8") as file:
        content = file.read()
        return content

if __name__ == "__main__":
    print("Tentando ler o arquivo de notas...")
    notas = read_notes()
    print("--- Conteúdo das Notas ---")
    print(notas)