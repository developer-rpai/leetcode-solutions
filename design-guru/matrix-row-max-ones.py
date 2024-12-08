class Solution:
    def findMaxOnesRow(self, mat):
        maxOnesIdx, maxOnesCount = 0, 0  # Initialize tracking variables
        
        for i, value in enumerate(mat):
            max_row = 0 
            row_track = 0
            for j in value:
                if j == 1:
                    max_row += 1
                
                if max_row > maxOnesCount:
                    row_track = i

            maxOnesIdx = max(maxOnesIdx, row_track)
            maxOnesCount = max(maxOnesCount, max_row)


        return [maxOnesIdx, maxOnesCount]  







input = [[1, 0], [1, 1], [0, 1]]
input2 = [[1, 0, 1], [0, 0, 1], [1, 1, 0]]
input3 = [[0, 1, 1], [0, 1, 1], [1, 1, 1]]
sol = Solution()

print(sol.findMaxOnesRow(input))