class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = []
        n = len(positions)
        
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
        
        # Sort by position
        robots.sort()
        
        stack = []
        
        for robot in robots:
            pos, health, direction, idx = robot
            
            if direction == 'R':
                stack.append(robot)
            else:
                # direction == 'L'
                while stack and stack[-1][2] == 'R' and health > 0:
                    top = stack[-1]
                    
                    if top[1] < health:
                        stack.pop()
                        health -= 1
                    elif top[1] > health:
                        top[1] -= 1
                        health = 0
                    else:
                        stack.pop()
                        health = 0
                
                if health > 0:
                    stack.append([pos, health, direction, idx])
        
        # Sort by original index
        stack.sort(key=lambda x: x[3])
        
        result = []
        for robot in stack:
            result.append(robot[1])
        
        return result