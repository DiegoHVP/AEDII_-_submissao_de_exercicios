# Sistema de Autocompletar Palavras usando Árvore AVL

Este projeto consiste na implementação de um sistema de autocompletar palavras utilizando uma árvore AVL, uma estrutura de dados de Processamento de Linguagem Natural (PLN).

## Etapas do Projeto

### Pré-processamento do Corpus

1. **Converter todo o texto para minúsculas**: Isso garante consistência na análise, evitando diferenças entre palavras maiúsculas e minúsculas.
   
2. **Remover pontuação e caracteres especiais**: Eliminar esses elementos ajuda a simplificar o texto, focando apenas nas palavras.
   
3. **Dividir o texto em palavras**: Isso permite o processamento individual de cada palavra.
   
4. **Remover palavras de parada/stop words**: Se desejado, é possível remover palavras comuns que não contribuem significativamente para o significado do texto.

### Construção da Árvore AVL

Nesta etapa, todas as palavras únicas do corpus são inseridas em uma árvore AVL, garantindo que a estrutura permaneça balanceada para otimizar as operações de busca.

### Autocompletar

Foi implementada uma função que percorre a árvore AVL e retorna palavras que começam com um determinado prefixo. A função para de buscar na árvore assim que encontra um nó que não corresponda ao prefixo.


## Ferramentas Utilizadas

- Para pré-processamento do corpus, foi utilizada a bibliotecas RE.
- A implementação da árvore AVL pode ser feita em linguagens Python.
- Um front minimo usando a biblioteca Gradio
- Para a análise de desempenho, foram utilizadas técnicas de medição de tempo.

## Resultados

Os resultados obtidos demonstraram que a árvore AVL oferece tempos de busca mais eficientes em comparação com a lista e a árvore binária não balanceada, especialmente em grandes conjuntos de dados. Além disso, a altura da árvore AVL permaneceu relativamente baixa, mesmo para grandes volumes de dados, o que contribui para uma busca mais rápida.

Este projeto foi desenvolvido por Diêgo Henrique Viana Pereira como parte dos requisitos da disciplina Algoritimo e Estrutura de Dados 2 (AED-II), sob a orientação do professor Ivanovitch Medeiros Dantas da Silva.
