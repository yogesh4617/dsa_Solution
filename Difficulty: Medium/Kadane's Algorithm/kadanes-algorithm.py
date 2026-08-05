class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        final_ans = -99999999
        prev_ans = 0
        
        for i in arr:
            
            current_sum = max(i, i + prev_ans)
            
            prev_ans = current_sum
            
            if final_ans < prev_ans:
                final_ans = prev_ans
                
                
        return final_ans