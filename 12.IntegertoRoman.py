class Solution:
    def intToRoman(self, num: int) -> str:
        ret = ''
        tempval = num // 1000
        for i in range(num // 1000):
            ret += 'M'
        num = num % 1000
        tempval = num // 100
        ret += self.singleDigittoRoman(tempval, 'C', 'D', 'M')
        num = num % 100
        tempval = num // 10
        ret += self.singleDigittoRoman(tempval, 'X', 'L', 'C')
        num = num % 10
        tempval = num 
        ret += self.singleDigittoRoman(tempval, 'I', 'V', 'X')
        return ret
    
    def singleDigittoRoman(self, num, str_one,\
                           str_five, str_ten):
        ret = ''
        if num == 0:
            pass
        elif num > 0 and num < 4:
            for i in range(num):
                ret += str_one
        elif num == 4:
            ret == str_one + str_five
        elif num > 4 and num < 9:
            ret = str_five
            for i in range(num - 5):
                ret += str_one
        elif num == 9:
            ret = str_one + str_ten
        return ret
