from AVL import *
import time

Arquivo_corpus = 'corpus.txt'

# ADICAO DE PALAVRAS
ArvoreTeste = AVLTree()
with open(Arquivo_corpus, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    Palavras: set = texto.split()
    for palavra in Palavras:
        ArvoreTeste.inserir(palavra)
    
    times_list = []
    times_avl = []

    for palavra in Palavras:
        start = time.time()
        palavra in Palavras
        end = time.time()
        times_list.append(end - start)

        start = time.time()
        ArvoreTeste.contem(palavra)
        end = time.time()
        times_avl.append(end - start)
        
    # numero de elementos do corpus
    TamX = list(range(1, len(Palavras) + 1))

import plotly.express as px

times_list_ms = [t * 1000 for t in times_list]
times_avl_ms = [t * 1000 for t in times_avl]

fig = px.scatter(x=[TamX], y=times_list_ms, labels={"x": "Elemento corpus nº", "y": "Tempo (ms)"},
                 title="Lista vs. AVL", template="plotly_dark")
fig.add_scatter(x=TamX, y=times_avl_ms, mode='markers', name='AVL', marker=dict(size=8))

# Update axes properties
fig.update_xaxes(showline=True, linewidth=1, linecolor="gray")
fig.update_yaxes(showline=True, linewidth=1, linecolor="gray")
# Change the name in the legend
fig.update_traces(name="List", selector=dict(name="wide_variable_0"))

# Show the figure
fig.show()