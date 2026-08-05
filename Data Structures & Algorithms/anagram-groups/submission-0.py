class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sig = defaultdict(list)
        for s in strs:
            t = [0] * 26
            for c in s:
                i = ord(c) - ord("a")
                t[i] = t[i] + 1
            sig[tuple(t)].append(s)
        return list(sig.values())

        