## 1263. Minimum Moves to Move a Box to Their Target Location

### Enunciado:
A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the following rules:

- The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
- The character '.' represents the floor which means a free cell to walk.
- The character '#' represents the wall which means an obstacle (impossible to walk there).
- There is only one box 'B' and one target cell 'T' in the grid.
- The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
- The player cannot walk through the box.

Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

![ExemploVisal](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_1263/Ex1.png "ExemploVisual")

### Exemplo 1
>**Input:** grid = Input: grid =  
>                [["#","#","#","#","#","#"],  
>                ["#","T","#","#","#","#"],  
>                ["#",".",".","B",".","#"],  
>                ["#",".","#","#",".","#"],  
>                ["#",".",".",".","S","#"],  
>                ["#","#","#","#","#","#"]]  

>**Output:** 3

### Exemplo 2
>**Input:** grid = Input: grid =  
>                [["#","#","#","#","#","#"],  
>                ["#","T","#","#","#","#"],  
>                ["#",".",".","B",".","#"],  
>                ["#","#","#","#",".","#"],  
>                ["#",".",".",".","S","#"],  
>                ["#","#","#","#","#","#"]]  

>**Output:** -1

### Exemplo 3
>**Input:** grid =  
>               [["#","#","#","#","#","#"],  
>               ["#","T",".",".","#","#"],  
>               ["#",".","#","B",".","#"],  
>               ["#",".",".",".",".","#"],  
>               ["#",".",".",".","S","#"],  
>               ["#","#","#","#","#","#"]]  
>**Output:** 5

Entradas e saídas obtidas:

Codigo de teste:
<br>
![TestesRodados](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_1263/CodigoTeste.png "TestesRodados")

Saída obtida:
<br>
![SaidasObtidas](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_1263/OutputTeste.png "SaidasObtidas")

Foi utilizado uma BFS para resolver o problema, o desafio desta resolução é muito semelhante ao problema também resolvido neste módulo de questões do Leet Code.
Porém neste, ligeiramente diferente, podemos encontrar um algoritmo que determina se o player consegue alcançar a caixa para então movê-la
<br>
![Submissao](https://github.com/projeto-de-algoritmos-2024/Grafos1_LeetCodeExs/blob/master/Questoes/Questao_1263/Aceito.png "Exercicio Submetido")
