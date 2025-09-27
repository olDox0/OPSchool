#atualizado em 2025/09/27-Versão 1.4. Função estável. Introduz dicionários para estruturar dados com pares chave-valor. Melhoria: Nenhuma neste estágio.
"""
Arquivo principal da olDox222 Python School (OPSchool).

Nesta versão, introduzimos os dicionários para estruturar nossos dados
de forma mais organizada, usando pares de chave e valor.
"""

def run_school():
    """
    Função principal que executa a lógica central da escola.
    """
    # --- Estruturas de Dados: O Dicionário ---
    # Um dicionário é criado com chaves {} e armazena pares chave: valor.
    # É perfeito para descrever as propriedades de um único objeto.
    course_info = {
        "name": "olDox222 Python School",
        "version": 1.4,
        "is_active": True,
        "modules": [
            "Módulo 0: O Ponto de Partida",
            "Módulo 1: A Caixa de Ferramentas",
            "Módulo 2: O Salto para a Eficiência",
            "Módulo 3: Lidando com a Web e APIs"
        ]
    }
    
    # --- Tomando Decisões e Acessando Dados ---
    
    # Acessamos os valores do dicionário usando a chave entre colchetes [].
    if course_info["is_active"]:
        print(f"Bem-vindo(a) à {course_info['name']}!")
        print(f"Versão atual: {course_info['version']}")
        print("----------------------------------------")
        
        # Acessamos a lista de módulos que está DENTRO do dicionário.
        print("Conteúdo do Curso:")
        for module in course_info["modules"]:
            print(f"- {module}")
            
    else:
        print(f"O curso {course_info['name']} está em desenvolvimento. Volte em breve!")


# Este bloco de código é uma boa prática fundamental em Python.
# Ele verifica se o arquivo está sendo executado diretamente pelo usuário.
# Se estiver, ele chama a nossa função principal.
if __name__ == "__main__":
    run_school()