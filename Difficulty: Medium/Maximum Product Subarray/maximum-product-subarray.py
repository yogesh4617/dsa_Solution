class Solution:
	def maxProduct(self,arr):
		# code here
		
		max_product=float('-inf')
		
		left_to_right=1
		right_to_left=1
		
		n=len(arr)
		
		for i in range(n):
		    
            left_to_right *= arr[i]
            
            right_to_left *= arr[n - 1 - i]
            
            max_product = max(max_product, left_to_right, right_to_left)
            
            if left_to_right == 0:
                left_to_right = 1
            if right_to_left == 0:
                right_to_left = 1
		 
        return max_product         