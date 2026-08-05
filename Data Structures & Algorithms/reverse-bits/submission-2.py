class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            print(f"n is {bin(n)}")
            bit = n & 1
            n = n >> 1
            res = res << 1
            res = res | bit
            print(f"res is {bin(res)}")
        
        return res
        