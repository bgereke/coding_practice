# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.
 

# Note: You may assume the string contains only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = {}
        for i, char in enumerate(s):
            if char not in visited and char not in s[(i+1):]:
                return i
            else:
                visited[char] = 0
        return -1