class Solution:
    def findSubsets(self, arr):
        # code here
        ans = []
        arr.sort()
            
        def back_track(index, current):
            
            ans.append(current[:])

            for i in range(index, len(arr)):

                if i > index and arr[i] == arr[i-1]:
                    continue

                current.append(arr[i])

                back_track(i + 1, current)

                current.pop()

                
            return
            
        back_track(0, [])
        return ans
