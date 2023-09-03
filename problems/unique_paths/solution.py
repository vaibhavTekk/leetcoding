class Solution:
    count = 0
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]

        def helper(i,j,dp):
            if i > m-1 or j > n-1:
                return 0
            if i == m-1 and j == n-1:   
                return 1

            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = helper(i+1,j,dp) + helper(i,j+1,dp)
            return dp[i][j]

        return helper(0,0,dp)
