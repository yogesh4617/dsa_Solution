class Solution:
	def maxProduct(self,arr):
		# code here
      max_product = float('-inf')
      left_to_right = 1
      right_to_left = 1
      n = len(arr)

      for i in range(n):
          # 1. Calculate prefix product (left to right)
          left_to_right *= arr[i]

          # 2. Calculate suffix product (right to left)
          right_to_left *= arr[n - 1 - i]

          # 3. Update the maximum product found so far
          max_product = max(max_product, left_to_right, right_to_left)

          # 4. If we hit a 0, reset the running product to 1
          if left_to_right == 0:
              left_to_right = 1
          if right_to_left == 0:
              right_to_left = 1

      return max_product
