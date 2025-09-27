# Módulo 4: Construindo Ferramentas Interativas (CLI)

Até agora, para mudar o que nosso programa faz (como analisar uma URL diferente), precisamos editar o código-fonte. Isso não é prático. Neste módulo, vamos transformar nosso script em uma **Ferramenta de Linha de Comando (CLI - Command-Line Interface)** interativa.

### Lição 1: Aceitando Argumentos com `click`

Vamos permitir que o usuário nos diga qual URL analisar diretamente no terminal. Para isso, usamos a biblioteca `click`.

**O Problema do Ambiente (`ModuleNotFoundError`)**

Ao adicionar uma nova biblioteca (`click`), enfrentamos um `ModuleNotFoundError`. A causa foi um erro clássico: o comando `pip install` foi executado sem o ambiente virtual (`venv`) estar ativo.
*   **A Lição:** Sempre ative seu `venv` (`.\venv\Scripts\activate`) antes de instalar dependências ou rodar seu programa. Isso garante que tudo fique no ambiente isolado do seu projeto.

**O Código Final:**

```python
import click
from web_scraper import fetch_and_parse_website

@click.command()
@click.argument('url')
def cli(url):
    """Uma CLI que busca e analisa o conteúdo de uma URL."""
    click.echo(f"Buscando e analisando: {url}")
    # ... resto da lógica ...
    
if __name__ == "__main__":
    cli()