#atualizado em 2025/09/27-Versão 1.1. Função estável. Introduz o conceito de variáveis e tipos de dados. Melhoria: Nenhuma neste estágio.
"""
Arquivo principal da olDox222 Python School (OPSchool).

Nesta versão, introduzimos o conceito de variáveis para armazenar
informações como mensagens, números e outros tipos de dados.
"""

def run_school():
    """
    Função principal que executa a lógica central da escola.
    """
    # --- Variáveis e Tipos de Dados ---
    
    # 1. String (str): Usada para armazenar texto.
    welcome_message = "Olá, Mundo! Bem-vindo(a) à olDox222 Python School."
    
    # 2. Integer (int): Usado para armazenar números inteiros.
    start_year = 2025
    
    # 3. Float (float): Usado para armazenar números com casas decimais.
    course_version = 1.1
    
    # 4. Boolean (bool): Usado para armazenar valores de Verdadeiro ou Falso.
    is_active = True
    
    # --- Usando as Variáveis ---
    
    # Agora, em vez de escrever o texto diretamente no print,
    # usamos a variável que o armazena.
    print(welcome_message)
    
    # Usando "f-strings" para formatar e exibir as outras variáveis.
    # O 'f' antes das aspas nos permite colocar variáveis dentro de {chaves}.
    print(f"Este projeto começou no ano de {start_year}.")
    print(f"Versão atual do curso: {course_version}")
    print(f"O curso está ativo? {is_active}")


# Este bloco de código é uma boa prática fundamental em Python.
# Ele verifica se o arquivo está sendo executado diretamente pelo usuário.
# Se estiver, ele chama a nossa função principal.
if __name__ == "__main__":
    run_school()