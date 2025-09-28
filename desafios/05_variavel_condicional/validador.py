# O objetivo deste programa é validar um número.
# Se o número for negativo, ele deve criar uma mensagem de erro.
# No final, ele deve retornar uma mensagem de status.
# O programa funciona com números negativos, mas quebra com positivos.

def validate_number(number):
    """
    Verifica se um número é positivo.
    """
    is_valid = True
    
    if number < 0:
        is_valid = False
        error_message = "O número não pode ser negativo."
        
    # ERRO: A variável 'error_message' só é criada se o 'if' for executado.
    # Se o número for positivo, ela não existe, causando o UnboundLocalError.
    if is_valid:
        return "Validação bem-sucedida!"
    else:
        return f"Erro de validação: {error_message}"

if __name__ == "__main__":
    # Teste que funciona:
    print(validate_number(-5))
    
    # Teste que quebra:
    print(validate_number(10))