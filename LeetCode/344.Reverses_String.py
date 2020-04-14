class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        l = len(s)
        while i < l / 2:
            temp = s[i]
            s[i] = s[l-1-i]
            s[l-1-i] = temp
            i += 1

    def reverseString(self, s: List[str]):
        if len(s) < 2:
            return s
        else:
            return self.reverseString(s[1:]) + s[0]