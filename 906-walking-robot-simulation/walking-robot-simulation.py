class Solution:
    def robotSim(self, commands, obstacles):
        obstacle_set = set((x, y) for x, y in obstacles)
        
        # directions: North, East, South, West
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        dir = 0
        
        x, y = 0, 0
        maxDist = 0
        
        for cmd in commands:
            if cmd == -2:  # turn left
                dir = (dir + 3) % 4
            elif cmd == -1:  # turn right
                dir = (dir + 1) % 4
            else:
                dx, dy = dirs[dir]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacle_set:
                        break
                    x, y = nx, ny
                    maxDist = max(maxDist, x*x + y*y)
        
        return maxDist