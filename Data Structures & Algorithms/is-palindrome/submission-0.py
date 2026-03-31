# examples
# racecar is a palindrome
# quick learner is not a palindrome

# Was it a car or   a cat I saw?
# wasitacaroracatisaw

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumerics = "abcdefghijklmnopqrstuvwxyz0123456789"
        # strips out all non-alphanumeric values from s
        copy = []
        for c in s:
            if c.lower() in alphanumerics:
                copy.append(c.lower())

        i, j = 0, len(copy) - 1
        while i < j:
            if copy[i] != copy[j]:
                return False
            i += 1
            j -= 1
        
        return True