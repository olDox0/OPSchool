# Módulo 3: Lidando com a Web e APIs

Neste módulo, nosso programa deixa de ser um sistema isolado e aprende a interagir com a internet.

### Lição 1: Buscando Conteúdo da Web

A primeira tarefa é "baixar" o conteúdo de uma página. Para isso, usamos a biblioteca `requests`, o padrão da indústria em Python para fazer requisições HTTP.

**O Problema do Acesso Negado (Erro 403)**

Nossa primeira tentativa de acessar a Wikipedia falhou com um "Erro 403 - Forbidden". Isso acontece porque servidores se protegem de scripts automatizados. A solução é fazer nossa requisição se parecer com a de um navegador real, adicionando um cabeçalho `User-Agent`.

### Lição 2: Analisando HTML com BeautifulSoup

O conteúdo que recebemos é um HTML bruto e caótico. Para extrair informações dele, como o título, usamos a biblioteca `BeautifulSoup4`. Ela transforma o "texto" em um objeto estruturado que podemos navegar.

**O Código Final:**

```python
import requests
from bs4 import BeautifulSoup

def fetch_and_parse_website(url):
    headers = {
        'User-Agent': 'Mozilla/5.0...'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.find('title').get_text()
        return title
    #...