# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# **map pic not provided** 

# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

#my original solution
class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        seq_len = len(height)
        if seq_len < 3:
            return 0
        past_max = height[0]
        fut_max = max(height[2:])
        for i, h in enumerate(height[1:-1]):
            if h < past_max and h < fut_max:
                trapped += min(past_max, fut_max) - h
            else: 
                if h > past_max:
                    past_max = h
                if h >= fut_max:
                    fut_max = max(height[(i+2):])
        return trapped

