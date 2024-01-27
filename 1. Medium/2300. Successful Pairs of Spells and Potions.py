from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        lst = []
        potions.sort()
        ln: int = len(potions)
        for i in spells:
            t = bisect_left(potions, success / i)
            lst.append(ln - t)
        return lst
