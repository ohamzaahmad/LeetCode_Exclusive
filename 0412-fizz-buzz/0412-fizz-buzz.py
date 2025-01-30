class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result =[]

        for array_index in range(n):
            fake_i = array_index + 1

            #if divisible by 3 and NOT 5
            if fake_i % 3 == 0 and fake_i % 5 != 0:
                result.append("Fizz")
            # if divisible by 5 and NOT 3
            elif fake_i % 5 == 0 and fake_i % 3 != 0:
                result.append("Buzz")
            # if divisible by both 3 and 5
            elif fake_i % 3 == 0 and fake_i % 5 == 0:
                result.append("FizzBuzz")
            else:
                result.append(str(fake_i))
        return result
