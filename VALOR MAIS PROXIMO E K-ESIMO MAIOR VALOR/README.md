## Descrição da solução
Este repositório contém implementações de algoritmos relacionados a árvores BST. Os algoritmos implementados são 'findClosestValue' e 'findKthLargestValue'.

#### findClosestValue
Este algoritmo encontra o valor mais próximo de um determinado alvo em uma BST. Ele utiliza um método recursivo chamado 'getValueTree' para percorrer a árvore e atualizar o valor mais próximo conforme necessário.

#### findKthLargestValue
Este algoritmo encontra o k-ésimo maior valor em uma arvore. Ele utiliza um método recursivo chamado getKesimo que percorre em ordem reversa para encontrar o k-ésimo maior valor.


## Complexidade: 
- findClosestValue: A complexidade deste algoritmo é O(h), onde h é a altura da árvore. Isso porque o algoritmo percorre a árvore da raiz até a folha mais distante em um caminho único.
- findKthLargestValue: A complexidade deste algoritmo depende da altura árvore + valor de K. No pior caso (quando usamos K-esimo menor valor), a árvore se assemelha a uma lista encadeada, a complexidade é O(n), onde n é o número de nós na árvore. Isso ocorre porque o algoritmo percorre todos os nós da árvore. No melhor caso (quando escolhemos o maior valor), a complexidade é O(h), onde h é a altura da árvore. Em casos gerais que sua comlexidade esta ligada ao K-esimo valor. Seu comportamento segue o O(h+k).
 

## Instruções passo a passo para executar a solução
Para executamos o algorimo pode se usar o [Colab](https://colab.research.google.com/). Ao abrir havera varios blocos de codigos, o que devem ser executados sera os dois primeiros, onde sera implementa a BST e os dois ultimos que serão resposnsaveis pela implementação da função e execução de um algoritomo de teste unitarios, segue abaixo o link para Notebook.

- [Find closest Value in BST](https://colab.research.google.com/github/DiegoHVP/AED-II/blob/main/VALOR%20MAIS%20PROXIMO%20E%20K-ESIMO%20MAIOR%20VALOR/challenge_01_closestvalue.ipynb)

- [Find Kth Largest Value in BST](https://colab.research.google.com/github/DiegoHVP/AED-II/blob/main/VALOR%20MAIS%20PROXIMO%20E%20K-ESIMO%20MAIOR%20VALOR/challenge_02_kth_largest.ipynb)


#### Apresentação do algoritimo
Nesse curto video tento apresentar o comportamento função, sua implementação e sua complexidade
[![Watch the video](https://i9.ytimg.com/vi/tfXwZ_-J_I0/mqdefault.jpg?sqp=COjm8LAG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGEggXChlMA8=&rs=AOn4CLCVT8pOYld6WPO5OJEhtAbgDYJAIw)](https://youtu.be/tfXwZ_-J_I0)


##### Estrutura do repositório
- README.md: Este arquivo contendo informações sobre o repositório.
- challenge_01_closestvalue.ipynb: O arquivo Python que demonstra exemplos de uso dos algoritmos e implemetação da findClosestValue
- challenge_02_kth_largest.ipynb: O arquivo Python que demonstra exemplos de uso dos algoritmos e implemetação da findKthLargestValue.