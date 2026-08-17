class Solution:
	def maxProduct(self,arr):
		# code here
		max_Produt=-9999999
		L_to_R = 1
		R_to_L = 1
		n = len(arr)
		
		for i in range(n):
		    # 1 calculate the prefix product
		    L_to_R*=arr[i]
		    
		    # 2 calculate the suffix product 
		    R_to_L*=arr[n-1-i]
		    
		    # Find the max value
		    max_Produt = max(max_Produt, L_to_R, R_to_L)
		    
		    # 4 if the value hits 0, reset the value into 1
		    if L_to_R == 0:
		        L_to_R = 1
		        
		    if R_to_L == 0:
		        R_to_L = 1
		        
		        
        return max_Produt