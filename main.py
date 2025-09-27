#atualizado em 2025/09/27-Versão 1.2. Função estável. Introduz o conceito de estruturas de controle (if/else). Melhoria: Nenhuma neste estágio.
"""
Arquivo principal da olDox222 Python School (OPSchool).

Nesta versão, introduzimos as estruturas de controle if/else,
permitindo que o programa tome decisões com base nos valores das variáveis.
"""

def run_school():
    """
    Função principal que executa a lógica central da escola.
    """
    # --- Variáveis e Tipos de Dados ---
    welcome_message = "Olá, Mundo! Bem-vindo(a) à olDox222 Python School."
    start_year = 2025
    course_version = 1.2
    is_active = True
    
    # --- Tomando Decisões ---
    
    # A instrução 'if' verifica se a condição é Verdadeira (True).
    # Como a variável 'is_active' é True, o código dentro deste bloco será executado.
    if is_active:
        print(welcome_message)
        print(f"Este projeto começou no ano de {start_year}.")
        print(f"Versão atual do curso: {course_version}")
        
        # Podemos aninhar 'ifs' para decisões mais complexas.
        if course_version > 1.0:
            print("O curso já recebeu suas primeiras atualizações!")
            
    # A instrução 'else' define o que acontecerá se a condição do 'if' for Falsa (False).
    else:
        print("A olDox222 Python School está em desenvolvimento. Volte em breve!")


# Este bloco de código é uma boa prática fundamental em Python.
# Ele verifica se o arquivo está sendo executado diretamente pelo usuário.
# Se estiver, ele chama a nossa função principal.
if __name__ == "__main__":
    run_school()