class Solution:
    def isPalindrome(self, s: str) -> bool:
        hel = "".join(char for char in s if char.isalnum()).lower()
        # Check if the string is identical to its reverse
        return hel == hel[::-1]