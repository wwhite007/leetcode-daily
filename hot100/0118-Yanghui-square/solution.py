class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            if i == 0:
                output.append([1])
            else:
                row = [1] * (i+1)
                for j in range(i+1):
                    if j == 0 or j == i:
                        continue
                    else:
                        row[j] = output[-1][j] + output[-1][j-1]
                output.append(row)
        return output
        
