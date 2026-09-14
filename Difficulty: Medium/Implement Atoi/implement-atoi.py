class Solution:
    def myAtoi(self, s):
        # code here
        
        Int_max = 2**31 -1
        Int_min = -2**31
        
        only_int = ""
        
        s = s.strip()
        string_len = len(s)
        
        sign = 1
        
        if string_len == 1 and "-" in s:
            return 0
        
        for i in s:
            
            if (i == "-" or i == "+") and only_int == "" :
                
                if i == "-":
                    sign = -1
                
            elif i.isdigit():
                only_int += i
                
            else:
                break
            
            
        if not only_int:
            return 0
            
            
        num = int(only_int)*sign

            
        if Int_max < num:
            return Int_max
            
        if num < Int_min:
            return Int_min
            
        return num