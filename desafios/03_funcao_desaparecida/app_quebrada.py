# O objetivo deste programa é criar uma classe que se configura
# ao ser inicializada. No entanto, uma parte do código foi
# acidentalmente removida durante uma refatoração.

class SimpleApp:
    def __init__(self):
        print("Inicializando o aplicativo...")
        
        # O programa tenta chamar um método para configurar os 'widgets'
        # mas a definição do método está faltando!
        self.setup_widgets()
        
        print("Aplicativo configurado com sucesso!")

    # A linha abaixo foi comentada por engano.
    # def setup_widgets(self):
    #     print("Configurando os widgets...")
    #     self.widgets_are_ready = True

if __name__ == "__main__":
    app = SimpleApp()