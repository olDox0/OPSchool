# O objetivo deste programa é imprimir uma mensagem colorida no terminal.
# Para isso, ele depende da biblioteca 'click'.
#
# Se você executar este arquivo sem instalar suas dependências
# ou no ambiente errado, ele vai falhar.

import click

def main():
    """
    Função principal que imprime uma mensagem de sucesso.
    """
    click.echo(click.style("Parabéns! Você consertou o ambiente e o programa funcionou!", fg='green'))

if __name__ == "__main__":
    main()