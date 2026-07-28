class Solution:
    def getLastDigit(self, a, b):

        if b == "0":
            return 1

        base = int(a[-1])

        exp = 0
        for digit in b:
            exp = (exp * 10 + int(digit)) % 4

        if exp == 0:
            exp = 4

        return pow(base, exp, 10)