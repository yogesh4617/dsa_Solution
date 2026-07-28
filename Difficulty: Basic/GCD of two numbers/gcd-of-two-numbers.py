class Solution:
    def gcd(self, a, b):
        # code here
        while True:
            if b != 0:
                temp = a % b
                a = b
                b = temp
            else:
                return a