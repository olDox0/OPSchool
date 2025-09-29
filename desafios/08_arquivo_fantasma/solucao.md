# Solução do Desafio 08: O Arquivo Fantasma

## O Diagnóstico
O erro `FileNotFoundError` é um dos mais diretos do Python. Ele ocorre quando a função `open()` tenta acessar um arquivo em um caminho que não existe. Neste caso, o script `leitor_de_notas.py` tentou abrir `notas.txt` na mesma pasta, mas o arquivo não estava lá.

## O Processo de Correção
A solução é simples: criar o arquivo que o programa está esperando.

**Passo 1: Crie o Arquivo**
Na pasta `08_arquivo_fantasma`, crie um novo arquivo de texto chamado `notas.txt`.

**Passo 2: Adicione Conteúdo (Opcional)**
Você pode deixar o arquivo vazio ou adicionar algum texto a ele, como:
`Lembrar de estudar a lição sobre FileNotFoundError.`

**Passo 3: Execute o Programa**
Agora, ao rodar `doxoade run leitor_de_notas.py`, o programa encontrará o arquivo, o lerá e imprimirá seu conteúdo (ou nada, se estiver vazio) sem erros.

**Dica de Profissional: Tratando o Erro no Código**
Em uma aplicação real, não podemos garantir que um arquivo sempre existirá. A maneira robusta de lidar com isso é usar um bloco `try...except` para capturar o erro e lidar com ele de forma elegante.

```python
def read_notes_safe():
    try:
        with open("notas.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "O arquivo 'notas.txt' não foi encontrado. Por favor, crie-o."