class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            tmp = []
            for c in str(x):
                tmp.append(c)
            return tmp == tmp[::-1]

solution = Solution()

print(solution.isPalindrome(-121))