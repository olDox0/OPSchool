# Desafio 02: O Acesso Negado (Erro 403)

## O Cenário
Este script (`web_scraper_quebrado.py`) deveria buscar e imprimir o título de uma página da Wikipedia. No entanto, ao executá-lo, ele falha com a seguinte mensagem:

`Falha na requisição: 403 Client Error: Forbidden for url: ...`

## Sua Missão
Seu objetivo é fazer o programa funcionar, modificando **apenas** o script `web_scraper_quebrado.py`. Você precisa fazer com que o script consiga acessar a página e imprimir seu título.

## Pistas
1.  Um erro `403 Forbidden` significa que o servidor se recusou a nos dar o conteúdo. Por quê?
2.  Servidores web modernos tentam bloquear scripts automatizados (bots). Como nossa requisição pode se parecer mais com a de um navegador real?
3.  A biblioteca `requests` permite enviar informações extras na requisição. Essas informações são chamadas de "cabeçalhos" (`headers`).

Consulte `solucao.md` se precisar de ajuda.