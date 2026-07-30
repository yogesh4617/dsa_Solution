class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq={}
        maj=0
        count = 0

        for i in nums:
            freq[i] = freq.get(i, 0)+1

        for i in freq:
            if count < freq[i]:
                maj = i
                count = freq[i]


        return maj


        