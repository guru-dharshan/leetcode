class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        sr=s[::-1]
        if(s==sr):
            return True
        return False
        
        