#atualizado em 2025/09/27-Versão 1.0. Funcionalidade. Módulo dedicado para a lógica de web scraping. Melhoria: Adicionar mais funções de extração (links, imagens).
"""
Módulo Web Scraper para a OPSchool.

Este módulo contém toda a lógica para buscar e analisar
conteúdo de páginas da web.
"""
import requests
from bs4 import BeautifulSoup

def fetch_and_parse_website(url):
    """
    Busca e analisa o conteúdo de uma URL para extrair título e parágrafos.

    Args:
        url (str): A URL do site.

    Returns:
        tuple: (título, lista_de_paragrafos) ou (mensagem_de_erro, None).
    """
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')
        
        title = soup.find('title').get_text()
        paragraphs_tags = soup.find_all('p')
        paragraphs_text = [p.get_text().strip() for p in paragraphs_tags]
        
        return title, paragraphs_text

    except requests.exceptions.RequestException as e:
        return f"Erro de conexão: {e}", None