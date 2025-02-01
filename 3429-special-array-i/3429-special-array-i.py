class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
            # Iterate through the array and check adjacent pairs
        for i in range(len(nums) - 1):
            # Check if adjacent elements have different parity
            if (nums[i] % 2 == nums[i + 1] % 2):
                return False
        # If no invalid pairs are found, return True
        return True
#         if len(nums)==1:
#             return True 
            
            
#         nums1 = []
#         for i in range(len(nums)+1):
#             for j in range(i+1,len(nums)):

#             if(((nums[i]%2==s[j]/2!=0)) or ((nums[i]%2!= 0) and (nums[j]/2==0))):
# != 0) and (nums[nums[i].appe                    nums1.apnums[i+1s[i]ap                    nums1n nums == nu[j]s1

                 
# # append ka syntex t#hk  we have to sol continur kroveh two pointerhy? 
# lets continue from here tomorrow 

       
       # what d solution wromg aya q k mny jo condition likhi wo har us array pay apply ho sakt jis k 1 y even eleents hn agar odd hn gay to answer sahi nh ayee ga koi or approach use krni paray gi OK
       # kal ystion classs mn karain gay filhal k liy is ka solution otha  k submit krtay hain 