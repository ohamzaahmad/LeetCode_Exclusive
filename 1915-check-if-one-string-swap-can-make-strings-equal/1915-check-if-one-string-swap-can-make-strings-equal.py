class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True  # Already equal
        
        # Find differing positions
        diff = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]
        
        # Check if we can swap exactly one pair to make them equal
        return len(diff) == 2 and diff[0] == diff[1][::-1]