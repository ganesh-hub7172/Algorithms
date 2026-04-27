from collections import deque

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }
        
        visited = set()
        queue = deque([(0, 0)])
        
        while queue:
            x, y = queue.popleft()
            
            if (x, y) == (m - 1, n - 1):
                return True
            
            visited.add((x, y))
            
            for dx, dy in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if opposite[(dx, dy)] in directions[grid[nx][ny]]:
                        queue.append((nx, ny))
        
        return False