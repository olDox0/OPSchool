# Solução do Desafio 07: A Chave Perdida

## O Diagnóstico
O `KeyError` ocorre porque tentamos acessar a chave `'usuario'` no dicionário, mas essa chave não existe. As chaves em um dicionário devem ser correspondências exatas. O dicionário `configuracao` possui a chave `'user_name'`, mas não `'usuario'`.

## O Processo de Correção
Existem duas maneiras de corrigir isso, ambas válidas.

**Solução 1: Corrigir a Chave**
A solução mais direta é usar a chave correta que existe no dicionário.

**Código Corrigido (`config_quebrada.py`):**
```python
def get_user_config(config):
    # Usamos a chave correta 'user_name'.
    return config['user_name']
	
Solução 2: Acessar de Forma Segura (Método .get())
Uma maneira mais robusta e "Pythônica" de acessar dicionários é usar o método .get(). Ele nunca causa um KeyError. Se a chave não existir, ele retorna None (ou um valor padrão que você pode especificar).

Código Corrigido e Robusto:


def get_user_config(config):
    # O .get() tenta pegar 'usuario'. Se falhar, tenta 'user_name'.
    # Se ambos falharem, retorna "Desconhecido".
    return config.get('usuario', config.get('user_name', "Desconhecido"))