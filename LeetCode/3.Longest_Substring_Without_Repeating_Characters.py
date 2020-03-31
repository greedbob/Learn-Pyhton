class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        line = {}
        length, max_length = 0, 0
        i = 0
        while i < len(s):
            if s[i] not in line:
                line[s[i]] = i
                length += 1
            else:
                length = 0
                i = line[s[i]]
                new_line = line.copy()
                for key in new_line.keys():
                    if new_line[key] <= new_line[s[i]]:
                        line.clear()
            i += 1
            if length > max_length:
                max_length = length
        return max_length

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        line = {}
        length = 0
        for i, letter in enumerate(s):
            if letter in line:
                new_line = line.copy()
                for key in new_line.keys():
                    if new_line[key] <= new_line[letter]:
                        del line[key]
            line[letter] = i
            i += 1
            length = len(line) if len(line) > length else length
        return length


s = "dvdfaw"
solution = Solution()
ans = solution.lengthOfLongestSubstring_2(s)
print(ans)
