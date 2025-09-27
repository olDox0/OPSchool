#atualizado em 2025/09/27-Versão 4.0. Funcionalidade. Transforma o script em uma CLI interativa com 'click'. Melhoria: Adicionar mais opções de comando.
"""
Arquivo principal e ponto de entrada da olDox222 Python School (OPSchool).

Agora é uma ferramenta de linha de comando (CLI) que aceita uma URL
como argumento para análise.
"""
import click
from web_scraper import fetch_and_parse_website

# O decorador @click.command() transforma a função 'cli' em um comando executável.
@click.command()
# O decorador @click.argument(...) define que esperamos um argumento chamado 'url'.
@click.argument('url')
def cli(url):
    """
    Uma ferramenta de linha de comando que busca e analisa o conteúdo de uma URL.
    """
    click.echo(f"Buscando e analisando: {url}")
    click.echo("----------------------------------------")
    
    title, paragraphs = fetch_and_parse_website(url)
    
    if paragraphs:
        click.echo(click.style(f"Título: {title}\n", fg='cyan', bold=True))
        click.echo("--- Primeiros 3 Parágrafos ---")
        
        for p in paragraphs[:3]:
            click.echo(p.strip() + "\n")
    else:
        # Usamos click.style para colorir a saída de erro.
        click.echo(click.style(title, fg='red'))


# A 'cli' agora é nosso ponto de entrada.
if __name__ == "__main__":
    cli()