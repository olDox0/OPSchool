# Solução do Desafio 01: O Ambiente Quebrado

## O Diagnóstico
O erro `ModuleNotFoundError: No module named 'click'` aconteceu porque a biblioteca `click` não estava instalada no ambiente Python que o terminal estava usando para executar o script.

Este é o problema mais comum enfrentado por desenvolvedores Python. A causa raiz é quase sempre uma dessincronização entre o **Ambiente Virtual (`venv`)** do projeto e o terminal.

## O Processo de Correção
A solução envolve garantir que todas as ações sejam feitas **dentro** do ambiente virtual ativado.

**Passo 1: Ativar o Ambiente Virtual**
O primeiro passo é sempre garantir que o `(venv)` apareça no seu terminal.
```bash
.\venv\Scripts\activate