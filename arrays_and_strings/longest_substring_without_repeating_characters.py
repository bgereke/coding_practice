# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    #sliding hashmap
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        char_map = {}
        start = 0
        for stop in range(len(s)):
            if s[stop] in char_map:
                start = max(start, char_map[s[stop]])
            ans = max(ans, stop - start + 1)
            char_map[s[stop]] = stop + 1
        return ans