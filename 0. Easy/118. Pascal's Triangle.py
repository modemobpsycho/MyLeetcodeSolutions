from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp: list[list[int]] = [[1], [1, 1]]

        if numRows < 3:
            return dp[:numRows]

        for _ in range(numRows - 2):
            next_row: list[int] = [1]

            for i in range(1, len(dp[-1])):
                next_row.append(dp[-1][i] + dp[-1][i - 1])

            next_row += [1]
            dp.append(next_row)

        return dp
