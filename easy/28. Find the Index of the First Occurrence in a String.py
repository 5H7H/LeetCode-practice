class Solution:
    def charCheck(self, haystack: str, needle: str, i: int) -> bool:
        for j in range(len(needle)):
            if haystack[j+i] != needle[j]:
                return False
        return True

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): #处理needle比haystack长的情景
            return -1
        
        for i in range(len(haystack) - len(needle) + 1): #防止越界，只遍历到len(haystack) - len(needle)
            if haystack[i] == needle[0]:
                if self.charCheck(haystack, needle, i) == True:
                    return i
        return -1