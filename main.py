#atualizado em 2025/10/01-Versão 6.8. Reversão. Remove a tentativa de syntax highlighting para estabilizar a aplicação.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewLabel
from kivy.clock import Clock
import io
from contextlib import redirect_stdout
import os

class OPSchoolLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.populate_lesson_tree)

    def populate_lesson_tree(self, dt=0):
        tree = self.ids.lesson_tree
        docs_node = tree.add_node(TreeViewLabel(text='Módulos Principais'))
        if os.path.exists('docs'):
            for filename in sorted(os.listdir('docs')):
                if filename.endswith('.md'):
                    tree.add_node(TreeViewLabel(text=filename), docs_node)

        challenges_node = tree.add_node(TreeViewLabel(text='Desafios Práticos'))
        if os.path.exists('desafios'):
            for dirname in sorted(os.listdir('desafios')):
                if os.path.isdir(os.path.join('desafios', dirname)):
                    tree.add_node(TreeViewLabel(text=dirname), challenges_node)

    def load_selected_lesson(self):
        node = self.ids.lesson_tree.selected_node
        if not node or not node.parent_node: return
        
        parent_text = node.parent_node.text
        lesson_text = node.text
        
        self.ids.lesson_content.text = "Selecione uma lição ou desafio."
        self.ids.code_input.text = "# O código do desafio aparecerá aqui."
        
        path_to_instructions = ""
        if parent_text == 'Módulos Principais':
            path_to_instructions = os.path.join('docs', lesson_text)
        elif parent_text == 'Desafios Práticos':
            path_to_instructions = os.path.join('desafios', lesson_text, 'INSTRUCOES.md')
            
        if os.path.exists(path_to_instructions):
            with open(path_to_instructions, 'r', encoding='utf-8') as f:
                self.ids.lesson_content.text = f.read()

        if parent_text == 'Desafios Práticos':
            challenge_file_map = {
                '01_ambiente_quebrado': 'programa.py', '02_acesso_negado': 'web_scraper_quebrado.py',
                '03_funcao_desaparecida': 'app_quebrada.py', '04_refatoracao_incompleta': 'processador_texto.py',
                '05_variavel_condicional': 'validador.py', '06_ultimo_da_fila': 'processador_lista.py',
                '07_chave_perdida': 'config_quebrada.py', '08_arquivo_fantasma': 'leitor_de_notas.py',
                '09_gramatica_quebrada': 'calculadora_simples.py'
            }
            filename = challenge_file_map.get(lesson_text)
            if filename:
                path_to_code = os.path.join('desafios', lesson_text, filename)
                if os.path.exists(path_to_code):
                    with open(path_to_code, 'r', encoding='utf-8') as f:
                        self.ids.code_input.text = f.read()

    def run_code(self):
        code_to_run = self.ids.code_input.text
        output_terminal = self.ids.terminal_output
        f = io.StringIO()
        try:
            with redirect_stdout(f):
                exec(code_to_run)
            output = f.getvalue()
            output_terminal.text = output if output else "Executado com sucesso (sem saída)."
        except Exception as e:
            output_terminal.text = f"Erro na execução:\n{e}"

class OPSchoolApp(App):
    def build(self):
        return OPSchoolLayout()

if __name__ == '__main__':
    OPSchoolApp().run()