class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s # Edge case if only one row

        res = ""
        for r in range(numRows): # For each row in number of rows
            increment = 2 * (numRows -1) # Use this algorithm for finding the number of steps
            for i in range(r, len(s), increment): # For each char while in bounds of the steps, strong length, and rows
                res += s[i] # Increment the character to result
                if (r > 0  and r < numRows - 1 and 
                    i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        return res