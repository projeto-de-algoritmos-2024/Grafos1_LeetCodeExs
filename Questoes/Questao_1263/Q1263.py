from collections import deque

class State:
    def __init__(self, box_x, box_y, player_x, player_y, pushes):
        self.box_x = box_x
        self.box_y = box_y
        self.player_x = player_x
        self.player_y = player_y
        self.pushes = pushes

def is_valid(x, y, grid):
    x_max, y_max = len(grid), len(grid[0])
    return 0 <= x < x_max and 0 <= y < y_max and grid[x][y] != '#'

def can_reach(player_x, player_y, target_x, target_y, box_x, box_y, grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(player_x, player_y)])
    visited = set([(player_x, player_y)])
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == (target_x, target_y):
            return True
        for dir_x, dir_y in directions:
            new_x, new_y = x + dir_x, y + dir_y
            if is_valid(new_x, new_y, grid) and (new_x, new_y) not in visited and (new_x, new_y) != (box_x, box_y):
                visited.add((new_x, new_y))
                queue.append((new_x, new_y))
    
    return False

def bfs(start, target, box, grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    start_state = State(box[0], box[1], start[0], start[1], 0)
    queue = deque([start_state])
    visited = set([(start_state.box_x, start_state.box_y, start_state.player_x, start_state.player_y)])
    
    while queue:
        state = queue.popleft()

        if (state.box_x, state.box_y) == target:
            return state.pushes

        for dir_x, dir_y in directions:
            new_box_x, new_box_y = state.box_x + dir_x, state.box_y + dir_y

            if is_valid(new_box_x, new_box_y, grid):
                new_player_x, new_player_y = state.box_x - dir_x, state.box_y - dir_y
                
                if is_valid(new_player_x, new_player_y, grid) and (new_box_x, new_box_y, new_player_x, new_player_y) not in visited:
                    if can_reach(state.player_x, state.player_y, new_player_x, new_player_y, state.box_x, state.box_y, grid):
                        new_state = State(new_box_x, new_box_y, new_player_x, new_player_y, state.pushes + 1)
                        visited.add((new_state.box_x, new_state.box_y, new_state.player_x, new_state.player_y))
                        queue.append(new_state)
    
    return -1

def minPushesToMoveBox(grid):
    x_max, y_max = len(grid), len(grid[0])
    
    start, target, box = None, None, None
    for i in range(x_max):
        for j in range(y_max):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'T':
                target = (i, j)
            elif grid[i][j] == 'B':
                box = (i, j)

    return bfs(start, target, box, grid)

## Exemplos de teste local!
##Exemplo 1
grid = [["#","#","#","#","#","#"],
        ["#","T","#","#","#","#"],
        ["#",".",".","B",".","#"],
        ["#",".","#","#",".","#"],
        ["#",".",".",".","S","#"],
        ["#","#","#","#","#","#"]]

print(minPushesToMoveBox(grid))

##Exemplo 2
grid = [["#","#","#","#","#","#"],
        ["#","T","#","#","#","#"],
        ["#",".",".","B",".","#"],
        ["#","#","#","#",".","#"],
        ["#",".",".",".","S","#"],
        ["#","#","#","#","#","#"]]

print(minPushesToMoveBox(grid))

##Exemplo 3
grid = [["#","#","#","#","#","#"],
        ["#","T",".",".","#","#"],
        ["#",".","#","B",".","#"],
        ["#",".",".",".",".","#"],
        ["#",".",".",".","S","#"],
        ["#","#","#","#","#","#"]]

print(minPushesToMoveBox(grid))

## Descomente esta classe, e comente os exemplos acima para testar no LeetCode
##class Solution:
##    def minPushBox(self, grid: List[List[str]]) -> int:
##        return (minPushesToMoveBox(grid))