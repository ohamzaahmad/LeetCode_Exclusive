class Solution:
    def finalString(self, s: str) -> str:
        result = []  # A list to hold the characters
        
        for char in s:
            if char == 'i':
                result.reverse()  # Reverse the list when encountering 'i'
            else:
                result.append(char)  # Append other characters normally
                
        return "".join(result)  # Convert the list to a string at the end
