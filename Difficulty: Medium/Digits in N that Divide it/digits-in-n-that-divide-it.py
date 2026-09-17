class Solution:    
    def divisibleByDigits(self,s):
        #code here
        count = 0
        remainders = [0] * 10
        
        for ch in s:
            x = ord(ch) - ord('0')
        
            for d in range(1, 10):
                remainders[d] = (remainders[d] * 10 + x) % d
        
        for ch in s:
            digit = ord(ch) - ord('0')
        
            if digit != 0 and remainders[digit] == 0:
                count += 1
        
        return count