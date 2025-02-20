class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums)
        result = []
        
        for i in range(n):
            # If the i-th character in the i-th string is '0', add '1' to result, else add '0'
            result.append('1' if nums[i][i] == '0' else '0')
        
        return ''.join(result)
