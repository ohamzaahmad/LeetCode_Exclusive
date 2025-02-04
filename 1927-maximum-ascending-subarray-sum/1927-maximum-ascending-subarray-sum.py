

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Initialize max_sum to store the maximum sum found
        max_sum = 0  
        # Initialize current_sum with the first element
        current_sum = nums[0]  

        # Iterate through nums starting from the second element
        for i in range(1, len(nums)):  
            if nums[i] > nums[i - 1]:  # If ascending, add to current sum
                current_sum += nums[i]  
            else:  # If not ascending, update max_sum and reset current_sum
                max_sum = max(max_sum, current_sum)  
                current_sum = nums[i]  # Start new subarray

        # Final update in case the last subarray was the max
        return max(max_sum, current_sum)  
