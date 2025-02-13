class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        # Convert nums into a min-heap
        heapq.heapify(nums)
        operations_count = 0

        # Continue operations until the smallest element is at least k
        while len(nums) > 1 and nums[0] < k:
            # Extract the two smallest elements
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            # Compute the new element
            new_element = min(x, y) * 2 + max(x, y)
            
            # Insert the new element back into the heap
            heapq.heappush(nums, new_element)
            
            # Increment the operation count
            operations_count += 1

        return operations_count
    