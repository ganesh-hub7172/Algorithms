class Solution:
    def separateSquares(self, squares):
        def area_below(h):
            area = 0.0
            for x, y, l in squares:
                if h <= y:
                    continue
                elif h >= y + l:
                    area += l * l
                else:
                    area += (h - y) * l
            return area

        total = 0.0
        for x, y, l in squares:
            total += l * l

        target = total / 2.0

        # Binary search range
        low = min(y for x, y, l in squares)
        high = max(y + l for x, y, l in squares)

        for _ in range(60):  # enough for precision 1e-5
            mid = (low + high) / 2.0
            if area_below(mid) < target:
                low = mid
            else:
                high = mid

        return low