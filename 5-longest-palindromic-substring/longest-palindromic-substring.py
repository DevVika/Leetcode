class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize variables
        res = " "
        resLen = 0 
        # For each character in the string
        for i in range(len(s)):
            # Starts both pointers in the center
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Odd palindrome
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # Even palindrome
            l, r = i, i + 1 # Does not start both pointers in the center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res


            
