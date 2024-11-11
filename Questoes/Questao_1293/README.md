## 1293. Shortest Path in a Grid with Obstacles Elimination

### Enunciado:
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

![Exemplo1](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_1293/Ex1.png "Exemplo1")

>**Input:** grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1

>**Output:** 6

![Exemplo2](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_1293/Ex2.png "Exemplo2")

>**Input:** grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1

>**Output:** -1

Entradas e saídas obtidas:

Codigo de teste:
<br>
![Exemplo2](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_1293/CodigoTeste.png "Exemplo2")

Saída obtida:
<br>
![Exemplo2](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_1293/OutputTeste.png "Exemplo2")

Foi utilizado na BFS para resolver o problema, o desafio desta resolução consiste em compreender como se deve realizar a exclusão de um bloco de parede no caminho.
Para um comprrendimento do problema foi utilizado o texto [Eliminando blocos no caminho](https://medium.com/algorithms-digest/shortest-path-in-a-grid-with-obstacles-elimination-ad0c07ed41c2).
<br>
![Submissao](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_1293/Aceita.png "Exercicio Submetido")
