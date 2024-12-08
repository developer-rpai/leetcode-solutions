class Solution:
    def diagonalSum(self, mat):
        total_sum = 0  # Initialize the total sum

        for i in range(len(mat)):
            print(mat[i][0])
            print(mat[i][-1]  )
                  

        return total_sum  # Return the calculated total sum
    





input = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()

print(sol.diagonalSum(input))