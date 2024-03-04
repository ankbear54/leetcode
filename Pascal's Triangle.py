class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ass = []
        for i in range(0, numRows):
            row = [1] * (i + 1)
            for j in range(i + 1):
                if j != 0 and j != i:
                     row[j] = ass[i-1][j-1] + ass[i-1][j]
            ass.append(row)
 
        return ass