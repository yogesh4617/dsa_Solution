class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefixMap = {}

        prefixSum = 0
        maxLen = 0

        for i in range(len(arr)):

            prefixSum += arr[i]

            if prefixSum == k:
                maxLen = i + 1

            if (prefixSum - k) in prefixMap:
                length = i - prefixMap[prefixSum - k]
                maxLen = max(maxLen, length)

            if prefixSum not in prefixMap:
                prefixMap[prefixSum] = i

        return maxLen
