class Solution:
    def __init__(self):
        pass

    def getRow(self, rowIndex):
        res = [1] * (rowIndex+1)
        for i in range(1, rowIndex):
            for j in range(rowIndex-1, i-1, -1):
                res[j] += res[j+1]
        return res

if __name__ == '__main__':
    s = Solution()
    for i in range(0, 10):
        print "row index:", i
        print s.getRow(i)
        

