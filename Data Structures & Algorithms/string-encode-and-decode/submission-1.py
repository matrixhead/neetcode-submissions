class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret = (f"{ret}{len(s)}#{s}")
        return ret


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while True:
                if s[j] == '#':
                    break
                j = j+1
            slen = int(s[i:j])
            res.append(s[j+1:j+1+slen])
            i = j+1+slen
        return res


