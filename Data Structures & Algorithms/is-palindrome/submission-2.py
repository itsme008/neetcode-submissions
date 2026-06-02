class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s)<0:
            return False

        s = re.sub('[^A-Za-z0-9]+', '', s).lower()
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            
            left+=1
            right-=1

        return True