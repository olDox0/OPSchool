# Solução do Desafio 05: A Variável Condicional

## O Diagnóstico
O `UnboundLocalError` ocorre porque a variável `error_message` só é criada dentro do bloco `if number < 0:`. Se a função `validate_number` recebe um número positivo (como `10`), o bloco `if` é pulado, e a variável `error_message` nunca chega a existir. No entanto, o final da função, no bloco `else`, tenta acessá-la, causando o erro.

## O Processo de Correção
A solução é garantir que a variável `error_message` sempre exista, inicializando-a com um valor padrão no início da função.

**Código Corrigido (`validador.py`):**
```python
def validate_number(number):
    """
    Verifica se um número é positivo.
    """
    is_valid = True
    # Inicializamos a variável com um valor padrão.
    error_message = None 
    
    if number < 0:
        is_valid = False
        error_message = "O número não pode ser negativo."
        
    if is_valid:
        return "Validação bem-sucedida!"
    else:
        return f"Erro de validação: {error_message}"

if __name__ == "__main__":
    print(validate_number(-5))
    print(validate_number(10))