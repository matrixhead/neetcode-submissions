class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] =  freq.get(n,0) + 1
        buckets = [[] for i in range(len(nums)+1)]
        for key,v in freq.items():
            buckets[v].append(key)
        res = []
        for i in range(len(buckets)-1,-1,-1):
            bucket =  buckets[i]
            for n in bucket:
                res.append(n)
                if len(res)==k:
                    return res
             

        