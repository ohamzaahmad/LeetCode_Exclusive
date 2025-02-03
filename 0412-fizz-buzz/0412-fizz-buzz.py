class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result =[]
        for zero_index in range(n):
            array_index = zero_index+1
            if not array_index % 3 and not array_index % 5:
                result.append("FizzBuzz")
            elif not array_index % 3:
                result.append("Fizz")
            elif not array_index % 5:
                result.append("Buzz")
            else:
                result.append(str(array_index))
        
        return result