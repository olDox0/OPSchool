# Solução do Desafio 02: O Acesso Negado

## O Diagnóstico
O erro `403 Forbidden` ocorreu porque o servidor da Wikipedia identificou nossa requisição como um script automatizado e a bloqueou. Nossa requisição era "anônima". Para resolver isso, precisamos nos identificar como se fôssemos um navegador web comum, usando o cabeçalho `User-Agent`.

## O Processo de Correção
A solução é adicionar um dicionário `headers` à nossa chamada `requests.get()`.

**Código Corrigido (`web_scraper_quebrado.py`):**
```python
import requests

def fetch_title(url):
    try:
        # 1. Definimos os cabeçalhos para simular um navegador.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # 2. Passamos os headers para a requisição.
        response = requests.get(url, headers=headers, timeout=10)
        
        response.raise_for_status()
        
        title = response.text.split('<title>').split('</title>')
        return f"Título encontrado: {title}"

    except requests.exceptions.RequestException as e:
        return f"Falha na requisição: {e}"

if __name__ == "__main__":
    target_url = "https://pt.wikipedia.org/wiki/Python_(linguagem_de_programa%C3%A7%C3%A3o)"
    result = fetch_title(target_url)
    print(result)