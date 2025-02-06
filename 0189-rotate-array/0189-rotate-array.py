class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ex: [1,2,3,4], k=2
        # to reduce the iteration bcz of its circular path
        k %=len(nums)
        def ReverseSolution(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        ReverseSolution(0,len(nums)-1)
        # [->(4,3,2,1)]
        ReverseSolution(0,k-1)
        #  [->(3,4,) 2,1]
        ReverseSolution(k,len(nums)-1)
        # [3,4, ->(1,2)]