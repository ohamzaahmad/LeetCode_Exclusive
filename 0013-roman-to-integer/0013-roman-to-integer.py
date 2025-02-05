class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        res = 0
        # // len => 4
        # // arr = [1,2,3,4] len = 4
        # // index  0,1,2,3  last index 3
        # // out of bound hone k liye 4
        # // i+1<
        # // I I I => 3
        # // 0 1 2
        for i in range(len(s)):
            # // validation for if length of array is bigger and if value is larger than next one        
            if (i+1 < len(s)) and (roman[s[i]] < roman[s[i+1]]):
                # IM
                # 999 
                # -100 + 1000 => 900 => CM => CMXCIX
                # 500 + 100+ 100+100+ 100+ 50+10+10+10+10+9
                # D     C    C    C    C   L  X   X  X  X IX
                #999 1000
                #99 -> -10+100 -> 90 -> XCIX
                #9 -> -1+10
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res