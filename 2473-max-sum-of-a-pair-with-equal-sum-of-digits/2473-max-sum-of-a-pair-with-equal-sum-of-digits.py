class Solution:
    def maximumSum(self, nums: List[int]) -> int:
   
    
    
        def digit_sum(n):
            return sum(int(d) for d in str(n))  # Calculate sum of digits
        
        digit_map = defaultdict(list)  # Dictionary to store numbers by their digit sum
        max_sum = -1  # Default value if no pair is found

        # Group numbers by their digit sum
        for num in nums:
            dsum = digit_sum(num)
            digit_map[dsum].append(num)

        # Find the max sum among pairs
        for values in digit_map.values():
            if len(values) > 1:
                values.sort(reverse=True)  # Sort in descending order
                max_sum = max(max_sum, values[0] + values[1])  # Take the largest two numbers
        
        return max_sum

        