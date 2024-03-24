from TERMINAIS import *
from AVL import *


# REMOCAO TERMINAIS
Arquivo_corpus = 'corpus.txt'
remover_palavras_terminais(Arquivo_corpus)

# ADICAO DE PALAVRAS
Arvore = AVLTree()
with open(Arquivo_corpus, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    Palavras: set = texto.split()
    for palavra in Palavras:
        Arvore.inserir(palavra)


# BUSCAR
        
import gradio as gr

def TelaBusca(texto):
    resul = str(Arvore.Buscar(texto))
    return "RESULTADOS:\n" + resul + ""

demo = gr.Interface(fn=TelaBusca, inputs="text", outputs="text")
demo.launch()