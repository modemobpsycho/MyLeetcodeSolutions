class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(int(''.join(digits)) + 1))
