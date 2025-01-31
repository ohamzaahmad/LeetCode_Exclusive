class Solution:
    def finalString(self, s: str) -> str:
        result =[]
        # 2 pointer approach
        for char in s: # check character by char in string
            if char  == 'i':
                # first pointer on index 1
                left = 0
                # Second on last
                right = len(result)-1
                # initiated infinite until condition met
                while left < right:
                    # tuple unpacking technique by swapping value
                    result[left], result[right] = result[right], result[left]
                    # changing pointer by increasing 1 for left and decreasing 1 for left side
                    left += 1
                    right -=1
            else:
                # else simply add that character which is abviously other than "i" to array
                result.append(char)
        # if the loops condition breaks after meeting the condition, it will join all character(stored in result array: collection of array) to make single word.
        return "".join(result)