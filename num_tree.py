__author__ = 'alfmunny'


'''

Question:

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

Hints:

F(i) = G(i-1)*G(n-i)

G(n) = F(1) + F(2) + ... + F(n-1) + F(n)
G(n) = G(0)*G(n-1) + G(1)*G(n-2) + G(2)*G(n-3) + ... + G(n-2)*G(1) + G(n-1)*G(0)
.
.
.
G(3) = G(0)*G(2) + G(1)*G(1) + G(2)*G(0)
G(2) = G(0)*G(1) + G(1)*G(0)
G(1) = 1
G(0) = 1
'''

class Solution():

    def __init__(self):
        pass

    def numTrees(self, n):
        G_row = [0]*(n + 1)
        G_row[0] = G_row[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                G_row[i] += G_row[j]*G_row[i-j-1]
        return G_row[n]

s = Solution()
print s.numTrees(3)
print s.numTrees(4)
print s.numTrees(5)
