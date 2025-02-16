class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        
        size = 2 * n - 1  # Total size of the sequence
        res = [0] * size  # Initialize with zeros
        used = set()  # Keep track of used numbers

        def backtrack(index):
            # If we fill the sequence, return True
            if index == size:
                return True
            
            # Skip filled positions
            if res[index] != 0:
                return backtrack(index + 1)
            
            # Try placing numbers from n to 1
            for num in range(n, 0, -1):
                if num in used:
                    continue  # Skip if number is already placed

                if num == 1:  # 1 appears only once
                    res[index] = 1
                    used.add(1)
                    if backtrack(index + 1):
                        return True
                    res[index] = 0
                    used.remove(1)
                else:
                    # Ensure both positions are within bounds and empty
                    if index + num < size and res[index + num] == 0:
                        res[index] = res[index + num] = num
                        used.add(num)
                        
                        if backtrack(index + 1):
                            return True

                        # Backtrack
                        res[index] = res[index + num] = 0
                        used.remove(num)
            
            return False  # No valid sequence found at this state

        backtrack(0)
        return res
