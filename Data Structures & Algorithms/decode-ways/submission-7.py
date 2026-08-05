class Solution:
    def numDecodings(self, s: str) -> int:
        slen = len(s)
        b = 0
        if s[0]== "0":
            return 0

        if s[-1] != "0":
            b = 1
        if slen == 1:
            return b
        a = 1 + b if s[-2] in "12" and s[-1] in "0123456" else b if s[-2] != "0" else 0
        # print(a)
        # print(b)

        for i in range(slen-3,-1,-1):
            sc = 0 
            if s[i] != "0":
                sc = a
            dc = 0
            print(f"considering {s[i:i+2]}")
            if (s[i] == "2" and s[i+1] in "0123456" ) or s[i] == "1":
                print("taken")
                dc = b
            b = a
            a = sc + dc
        return a

    


