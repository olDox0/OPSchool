# O objetivo deste programa é buscar o título de uma página da Wikipedia.
# No entanto, ele está falhando com um erro de acesso.

import requests

def fetch_title(url):
    try:
        # ERRO: Esta requisição não se identifica e é bloqueada.
        response = requests.get(url, timeout=10)
        
        # raise_for_status() irá lançar um erro se o status for 4xx ou 5xx.
        response.raise_for_status()
        
        # A análise do título só acontecerá se a requisição for bem-sucedida.
        title = response.text.split('<title>')[1].split('</title>')[0]
        return title

    except requests.exceptions.RequestException as e:
        return f"Falha na requisição: {e}"

if __name__ == "__main__":
    target_url = "https://pt.wikipedia.org/wiki/Python_(linguagem_de_programa%C3%A7%C3%A3o)"
    result = fetch_title(target_url)
    print(result)
