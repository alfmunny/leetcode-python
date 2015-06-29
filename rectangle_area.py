__author__ = 'alfmunny'

'''
Question:

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
'''

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        # x: A, C, E, G
        # y: B, D, F, H
        res = abs(A-C)*abs(B-D) + abs(E-G)*abs(F-H)

        if A >= G or B >= H or E >= C or F >= D:
            return res
        else:
            x_a = sorted([A, C, E, G])
            x = x_a[2] - x_a[1]

            y_a = sorted([B, D, F, H])
            y = y_a[2] - y_a[1]
            res = res - x * y

        return res


