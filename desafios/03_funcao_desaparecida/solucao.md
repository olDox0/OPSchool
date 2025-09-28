# Solução do Desafio 03: A Função Desaparecida

## O Diagnóstico
O erro `AttributeError: 'SimpleApp' object has no attribute 'setup_widgets'` é uma das mensagens de erro mais claras do Python. Ele significa exatamente o que diz: o programa tentou chamar o método `self.setup_widgets()`, mas ao procurar por uma função com esse nome dentro da classe `SimpleApp`, não encontrou nenhuma.

Isso geralmente acontece por dois motivos: um erro de digitação no nome da função, ou, como neste caso, a função foi acidentalmente comentada ou deletada durante uma edição do código (um erro de refatoração muito comum).

## O Processo de Correção
A solução é simplesmente restaurar a função que está faltando.

**Código Corrigido (`app_quebrada.py`):**
```python
class SimpleApp:
    def __init__(self):
        print("Inicializando o aplicativo...")
        
        self.setup_widgets()
        
        print("Aplicativo configurado com sucesso!")

    # A solução é descomentar este bloco de código.
    def setup_widgets(self):
        print("Configurando os widgets...")
        self.widgets_are_ready = True

if __name__ == "__main__":
    app = SimpleApp()