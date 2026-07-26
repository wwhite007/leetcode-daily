from math import isqrt

class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(x: int) -> bool:
            root = isqrt(x)
            return root * root == x

        if is_square(n):
            return 1

        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:
            return 4

        for a in range(1, isqrt(n) + 1):
            if is_square(n - a * a):
                return 2

        return 3
