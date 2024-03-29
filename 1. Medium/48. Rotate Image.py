from typing import List


class Solution:
    def rotate(self, x: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(x)):
            for j in range(i, len(x)):
                x[i][j], x[j][i] = x[j][i], x[i][j]
        for i in range(len(x)):
            x[i] = x[i][::-1]
