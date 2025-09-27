#atualizado em 2025/09/27-Versão 1.3. Função estável. Introduz listas para coleções de dados e loops 'for' para iteração. Melhoria: Nenhuma neste estágio.
"""
Arquivo principal da olDox222 Python School (OPSchool).

Nesta versão, introduzimos as listas para armazenar coleções de dados
e os loops 'for' para executar ações repetitivas sobre esses dados.
"""

def run_school():
    """
    Função principal que executa a lógica central da escola.
    """
    # --- Variáveis e Tipos de Dados ---
    course_name = "olDox222 Python School"
    is_active = True
    
    # --- Estruturas de Dados: A Lista ---
    # Uma lista é criada com colchetes [] e armazena múltiplos itens.
    # Aqui, guardamos os nomes dos módulos do nosso curso.
    course_modules = [
        "Módulo 0: O Ponto de Partida",
        "Módulo 1: A Caixa de Ferramentas",
        "Módulo 2: O Salto para a Eficiência",
        "Módulo 3: Lidando com a Web e APIs"
    ]
    
    # --- Tomando Decisões ---
    if is_active:
        print(f"Bem-vindo(a) à {course_name}!")
        print("----------------------------------------")
        
        # --- Repetindo Tarefas: O Loop 'for' ---
        # Este loop irá passar por cada item da lista 'course_modules'.
        # A cada "passo", o item atual será colocado na variável 'module'.
        print("Conteúdo do Curso:")
        for module in course_modules:
            # O código indentado aqui será executado para cada módulo.
            print(f"- {module}")
            
    else:
        print(f"A {course_name} está em desenvolvimento. Volte em breve!")


# Este bloco de código é uma boa prática fundamental em Python.
# Ele verifica se o arquivo está sendo executado diretamente pelo usuário.
# Se estiver, ele chama a nossa função principal.
if __name__ == "__main__":
    run_school()