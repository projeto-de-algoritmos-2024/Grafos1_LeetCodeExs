from collections import deque

class Step:
    def __init__(self, pos_x, pos_y, distance, obstacle_max):
        self.x = pos_x
        self.y = pos_y
        self.distance = distance
        self.obstacle_max = obstacle_max

def shortPath(grid, k):
    x_max, y_max = len(grid), len(grid[0])
    
    start_step = Step(0, 0, 0, k)
    queue = deque([start_step])
    
    visited = set((start_step.x, start_step.y, start_step.obstacle_max))
   
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        step = queue.popleft()
      
        if step.x == x_max - 1 and step.y == y_max - 1:
            return step.distance
        
        for dir_x, dir_y in directions:
            new_x, new_y = step.x + dir_x, step.y + dir_y
            
            if 0 <= new_x < x_max and 0 <= new_y < y_max:
                new_obstacles_max = step.obstacle_max - grid[new_x][new_y]
                
                if new_obstacles_max >= 0 and (new_x, new_y, new_obstacles_max) not in visited:
                    new_step = Step(new_x, new_y, step.distance + 1, new_obstacles_max)
                    visited.add((new_step.x, new_step.y, new_step.obstacle_max))
                    queue.append(new_step)

    return -1

## Exemplos de teste local!
##Exemplo 1
grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
print(shortPath(grid, k))

##Exemplo 2
grid = [[0,1,1],[1,1,1],[1,0,0]]
k = 1
print(shortPath(grid, k))

## Descomente esta classe, e comente os exemplos acima para testar no LeetCode
##class Solution:
##    def shortestPath(self, grid: List[List[int]], k: int) -> int:
##        return shortPath(grid, k)