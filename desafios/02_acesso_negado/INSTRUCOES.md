# Desafio 02: O Acesso Negado (Erro 403)

## O Cen�rio
Este script (`web_scraper_quebrado.py`) deveria buscar e imprimir o t�tulo de uma p�gina da Wikipedia. No entanto, ao execut�-lo, ele falha com a seguinte mensagem:

`Falha na requisi��o: 403 Client Error: Forbidden for url: ...`

## Sua Miss�o
Seu objetivo � fazer o programa funcionar, modificando **apenas** o script `web_scraper_quebrado.py`. Voc� precisa fazer com que o script consiga acessar a p�gina e imprimir seu t�tulo.

## Pistas
1.  Um erro `403 Forbidden` significa que o servidor se recusou a nos dar o conte�do. Por qu�?
2.  Servidores web modernos tentam bloquear scripts automatizados (bots). Como nossa requisi��o pode se parecer mais com a de um navegador real?
3.  A biblioteca `requests` permite enviar informa��es extras na requisi��o. Essas informa��es s�o chamadas de "cabe�alhos" (`headers`).

Consulte `solucao.md` se precisar de ajuda.