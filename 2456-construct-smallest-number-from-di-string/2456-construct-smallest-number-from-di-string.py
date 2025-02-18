class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        stack = []
        result = []
        
        # We iterate over the pattern + 1 to handle the last number as well.
        for i in range(n + 1):
            # Always push the current number (1 to 9)
            stack.append(i + 1)
            
            # When we reach the end of the pattern or encounter 'I', we pop all numbers
            # from the stack because we need them to be in the correct order.
            if i == n or pattern[i] == 'I':
                while stack:
                    result.append(str(stack.pop()))
        
        # Join the result list to form the final string.
        return ''.join(result)
