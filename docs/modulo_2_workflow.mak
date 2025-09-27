# Módulo 2: O Salto para a Eficiência com `doxoade`

Até agora, preparamos nosso ambiente e escrevemos código em uma estrutura já existente. Mas como começamos um projeto do zero?

### A Dor do Processo Manual

Um desenvolvedor Python, ao iniciar um novo projeto, precisa executar uma série de comandos repetitivos:
1.  Criar a pasta do projeto (`mkdir meu_projeto`).
2.  Entrar na pasta (`cd meu_projeto`).
3.  Criar o ambiente virtual (`python -m venv venv`).
4.  Ativar o ambiente (`.\venv\Scripts\activate`).
5.  Criar arquivos essenciais (`.gitignore`, `requirements.txt`, `main.py`).
6.  Inicializar o repositório Git (`git init`).

Este processo é lento, tedioso e propenso a erros.

### A Solução: `doxoade init`

A ferramenta `doxoade` automatiza todo esse ritual com um único comando.

**Comando:**
```bash
doxoade init <NOME_DO_PROJETO>