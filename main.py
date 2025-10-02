#atualizado em 2025/10/02-Versão 7.8. Correção. Corrige a função de conversão para Markdown e o carregamento de arquivos.
import re, os, io
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewLabel
from kivy.clock import Clock
from contextlib import redirect_stdout
from pygments.lexers import PythonLexer

def markdown_to_bbcode(md_text):
    """Converte texto Markdown simples para o formato BBCode do Kivy."""
    # Títulos
    md_text = re.sub(r'^##\s*(.*)', r'[b][size=20]\1[/size][/b]', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^#\s*(.*)', r'[b][size=24]\1[/size][/b]', md_text, flags=re.MULTILINE)
    
    # Negrito (com asteriscos escapados)
    md_text = re.sub(r'\*\*(.*?)\*\*', r'[b]\1[/b]', md_text)
    
    # Itálico (com asterisco escapado)
    md_text = re.sub(r'\*(.*?)\*', r'[i]\1[/i]', md_text)
    
    # Código
    md_text = re.sub(r'`(.*?)`', r'[font=RobotoMono-Regular][color=c0c0c0]\1[/color][/font]', md_text)
    return md_text

class OPSchoolLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Atribui o objeto lexer ao CodeInput DEPOIS que ele foi criado.
        self.ids.code_input.lexer = PythonLexer()
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
        
        # --- Reseta os painéis ---
        self.ids.lesson_content.text = "Carregando..."
        self.ids.code_input.text = "# Selecione um desafio para ver o código."
        self.ids.solution_content.text = "# A solução só está disponível para desafios."
        
        path_to_instructions = ""
        
        # --- CORREÇÃO: Lógica com ELIF ---
        if parent_text == 'Módulos Principais':
            path_to_instructions = os.path.join('docs', lesson_text)
            self.ids.code_input.text = "# Esta é uma lição teórica. Selecione um desafio para praticar."
    
        elif parent_text == 'Desafios Práticos':
            # Define o caminho para as instruções do desafio
            path_to_instructions = os.path.join('desafios', lesson_text, 'INSTRUCOES.md')
            
            # Carrega o código do desafio
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

            # Carrega a solução do desafio
            path_to_solution = os.path.join('desafios', lesson_text, 'solucao.md')
            if os.path.exists(path_to_solution):
                with open(path_to_solution, 'r', encoding='utf-8') as f:
                    self.ids.solution_content.text = f.read()

        # --- Carrega o conteúdo das instruções no final ---
        if os.path.exists(path_to_instructions):
            # ABRIMOS COM UTF-8, POIS AGORA GARANTIMOS QUE OS ARQUIVOS ESTÃO CORRETOS
            with open(path_to_instructions, 'r', encoding='utf-8') as f:
                self.ids.lesson_content.text = markdown_to_bbcode(f.read())
        else:
            self.ids.lesson_content.text = f"Arquivo de instruções não encontrado para '{lesson_text}'."
        if parent_text == 'Desafios Práticos':
            path_to_solution = os.path.join('desafios', lesson_text, 'solucao.md')
            if os.path.exists(path_to_solution):
                with open(path_to_solution, 'r', encoding='utf-8') as f:
                    self.ids.solution_content.text = markdown_to_bbcode(f.read())
               
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