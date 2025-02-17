class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # from collections import Counter

    # def numTilePossibilities(tiles: str) -> int:
        def backtrack(counter):
            total = 0
            for tile in counter:
                if counter[tile] > 0:
                    counter[tile] -= 1  # Use one tile
                    total += 1 + backtrack(counter)  # Count this sequence and continue
                    counter[tile] += 1  # Restore tile count for other branches
            return total

        return backtrack(Counter(tiles))

# # Test cases
# print(numTilePossibilities("AAB"))  # Output: 8
# print(numTilePossibilities("AAABBC"))  # Output: 188
# print(numTilePossibilities("V"))  # Output: 1
