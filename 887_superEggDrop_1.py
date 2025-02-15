class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        memo = dict()

        def dp(k, n):
            if k == 1: return n
            if n == 0: return 0

            if (k, n) in memo:
                return memo[(k, n)]

            res = float('inf')
            for i in range(1, n+1):
                res = min(res, max(dp(k, n-i), dp(k-1, i-1) + 1))
            
            memo[(k, n)] = res
            return res

        return dp(k, n)


if __name__ == "__main__":
    assert Solution().superEggDrop(2, 6) == 3