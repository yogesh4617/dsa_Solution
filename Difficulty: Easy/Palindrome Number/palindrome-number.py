class Solution:
    def isPalindrome(self, n):
		# code here
		isPlainDrome = str(n)
        
        if isPlainDrome[::-1] == str(n):
            return True
            
        elif "-" in isPlainDrome and isPlainDrome.replace("-", "") == isPlainDrome[::-1].replace("-", ""):
            return True
                
        else:
            return False