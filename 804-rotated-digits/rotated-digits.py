class Solution:
    def rotatedDigits(self, n):
        good_count = 0
        
        for num in range(1, n + 1):
            s = str(num)
            is_valid = True
            is_good = False
            
            for ch in s:
                if ch in '347':
                    is_valid = False
                    break
                if ch in '2569':
                    is_good = True
            
            if is_valid and is_good:
                good_count += 1
        
        return good_count