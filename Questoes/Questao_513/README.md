## 513. Find Bottom Left Tree Value

### Enunciado:
Given the root of a binary tree, return the leftmost value in the last row of the tree.

![Exemplo1](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_513/Ex1.png "Exemplo1")

![Exemplo2](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_513/Ex2.png "Exemplo2")

Entradas e saídas obtidas:

### Caso de teste 1:
<br>
![Teste1](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_513/Case1.png "Teste1")

### Caso de teste 2:
<br>
![Teste2](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_513/Case2.png "Teste2")

Foi utilizado uma DFS simples para resolver este problema, o desafio deste problema é encontrar qual camada da árvore a DFS está visitando, para isso é utilizado uma variável auxiliar, uma vez que a cada etapa da recursão ela visitou o da esquerda primeiro
<br>
![Submissao](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_513/Aceito.png "Exercicio Submetido")
