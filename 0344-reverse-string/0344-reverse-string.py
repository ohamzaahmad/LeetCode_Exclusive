class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # left =0
        # right= len(s)-1
        left, right = 0, len(s)-1 # tuple unpacking method
        while left<right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
           # tuple is like list: tuple is unchangeable: support indexing, faster than list
