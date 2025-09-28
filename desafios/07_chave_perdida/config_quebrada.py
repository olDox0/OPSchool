# O objetivo deste programa é ler uma configuração de um dicionário.
# Ele tenta ler a configuração do 'usuário', mas a chave está escrita
# de forma errada, causando um erro.

def get_user_config(config):
    """
    Tenta retornar o nome do usuário da configuração.
    """
    # ERRO: O programa procura pela chave 'usuario', mas no dicionário
    # a chave correta é 'user_name'.
    return config['usuario']

if __name__ == "__main__":
    configuracao = {
        "user_name": "olDox222",
        "theme": "dark",
        "version": 1.2
    }
    
    # Esta chamada vai quebrar com um KeyError.
    usuario = get_user_config(configuracao)
    print(f"O usuário configurado é: {usuario}")