class Solution:
    def getSum(self, a: int, b: int) -> int:

        result = 0
        carry = 0
        for i in range(32):
            abit = a & 1
            a = a >> 1
            bbit = b & 1
            b = b >> 1
            rbit = abit ^ bbit ^ carry
            carry = (abit & bbit) | carry & (abit ^ bbit)
            rbit = rbit << i
            result |= rbit
        is_neg = (1<<31 & result) != 0 
        if is_neg:
            ret = -1 << 32
            return ret | result
            


        return result



        