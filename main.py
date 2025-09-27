#atualizado em 2025/09/27-Versão 2.2. Funcionalidade. Adiciona BeautifulSoup para parsear HTML e extrair dados. Melhoria: Extrair mais do que apenas o título.
"""
Módulo 3: Lidando com a Web e APIs.

Nesta versão, usamos a biblioteca BeautifulSoup para analisar o HTML
bruto e extrair informações específicas, como o título da página.
"""
import requests
from bs4 import BeautifulSoup

def fetch_and_parse_website(url):
    """
    Busca e analisa o conteúdo de uma URL para extrair o título.

    Args:
        url (str): A URL do site.

    Returns:
        str: O título da página ou uma mensagem de erro.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Criamos um objeto BeautifulSoup para analisar o HTML.
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Acessamos a tag <title> e extraímos seu texto.
        # Usamos .get_text() para limpar qualquer tag HTML interna.
        title = soup.find('title').get_text()
        return title
    else:
        return f"Falha ao buscar a página. Código de status: {response.status_code}"

def run_school():
    """
    Função principal que agora executa nossa lógica de busca e análise.
    """
    target_url = "https://pt.wikipedia.org/wiki/Python_(linguagem_de_programa%C3%A7%C3%A3o)"
    
    print(f"Buscando e analisando: {target_url}")
    print("----------------------------------------")
    
    page_title = fetch_and_parse_website(target_url)
    
    print(f"O título da página é: {page_title}")


if __name__ == "__main__":
    run_school()