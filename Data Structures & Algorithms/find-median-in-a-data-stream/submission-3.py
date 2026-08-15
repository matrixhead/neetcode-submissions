from typing import List

class MaxHeap:
    def __init__(self, values:Optional[List[int]] = None):
        if values:
            self.heapify(values)
        else:
            self.heap:List[int] = []

    def length(self)->int:
        return len(self.heap)

    def heapify(self, values:List[int]):
        self.heap = values.copy()
        for i in range((len(self.heap)//2)-1,-1,-1):
            self.sift_down(i)

    def sift_up(self,idx:int):
        while idx > 0:
            parent_idx = (idx-1)//2
            val = self.heap[idx]
            parent = self.heap[parent_idx]
            if parent < val:
                self.heap[parent_idx] = val
                self.heap[idx] = parent
                idx = parent_idx
            else:
                break

    def sift_down(self,idx:int):
        hlen = len(self.heap)
        while idx < hlen:
            if idx*2 + 2 < hlen:
                child1idx = idx*2 + 1
                child2idx = idx*2 + 2
                largestidx = child1idx if self.heap[child1idx] > self.heap[child2idx] else child2idx 
                if self.heap[idx] < self.heap[largestidx]:
                    temp = self.heap[idx] 
                    self.heap[idx] = self.heap[largestidx]
                    self.heap[largestidx] = temp
                    idx = largestidx
                else:
                    break
            elif idx*2+1 < hlen:
                childidx = idx*2+1
                if self.heap[idx] < self.heap[childidx]:
                    temp = self.heap[idx] 
                    self.heap[idx] = self.heap[childidx]
                    self.heap[childidx] = temp
                    idx = childidx
                else:
                    break
            else:
                break


    def insert(self,element:int):
        self.heap.append(element)
        self.sift_up(len(self.heap)-1)

    def peek(self)->Optional[int]:
        if self.heap:
            return self.heap[0]
        return None

    def extract(self)->Optional[int]:
        if not self.heap:
            return None
        ret = self.heap[0]
        self.heap[0] = self.heap[-1] 
        self.heap.pop()
        self.sift_down(0)
        return ret

class MinHeap:
    def __init__(self, values:Optional[List[int]] = None):
        if values:
            self.heapify(values)
        else:
            self.heap:List[int] = []
    
    def length(self)->int:
        return len(self.heap)

    def heapify(self, values:List[int]):
        self.heap = values.copy()
        for i in range((len(self.heap)//2)-1,-1,-1):
            self.sift_down(i)

    def insert(self,element:int):
        self.heap.append(element)
        self.sift_up(len(self.heap)-1)

    def sift_up(self,idx:int):
        while idx > 0:
            parent_idx = (idx-1)//2
            val = self.heap[idx]
            parent = self.heap[parent_idx]
            if parent > val:
                self.heap[parent_idx] = val
                self.heap[idx] = parent
                idx = parent_idx
            else:
                break

    def sift_down(self,idx:int):
        hlen = len(self.heap)
        while idx < hlen:
            if idx*2 + 2 < hlen:
                child1idx = idx*2 + 1
                child2idx = idx*2 + 2
                minidx = child1idx if self.heap[child1idx] < self.heap[child2idx] else child2idx 
                if self.heap[idx] > self.heap[minidx]:
                    temp = self.heap[idx] 
                    self.heap[idx] = self.heap[minidx]
                    self.heap[minidx] = temp
                    idx = minidx
                else:
                    break
            elif idx*2+1 < hlen:
                childidx = idx*2+1
                if self.heap[idx] > self.heap[childidx]:
                    temp = self.heap[idx] 
                    self.heap[idx] = self.heap[childidx]
                    self.heap[childidx] = temp
                    idx = childidx
                else:
                    break
            else:
                break
                
    def peek(self)->Optional[int]:
        if self.heap:
            return self.heap[0]
        return None
        
    def extract(self)->Optional[int]:
        if not self.heap:
            return None
        ret = self.heap[0]
        self.heap[0] = self.heap[-1] 
        self.heap.pop()
        self.sift_down(0)
        return ret


class MedianFinder:

    def __init__(self):
        self.minheap = MinHeap()
        self.maxheap = MaxHeap()
        

    def addNum(self, num: int) -> None:
        lmax = self.maxheap.peek()
        rmin = self.minheap.peek()


        if (lmax is None) or num <= lmax:
            self.maxheap.insert(num)
        else:
            self.minheap.insert(num)
        minhlen = self.minheap.length()
        maxhlen = self.maxheap.length()
        unbalanced_by = maxhlen - minhlen
        if unbalanced_by == 2:
          val = self.maxheap.extract()
          if val is None:
            val = 0
          self.minheap.insert(val)
        if unbalanced_by == -2:
          val = self.minheap.extract()
          if val is None:
            val = 0
          self.maxheap.insert(val)
            


        
        

    def findMedian(self) -> float:
        minhlen = self.minheap.length()
        maxhlen = self.maxheap.length()
        if minhlen > maxhlen:
            val = self.minheap.peek()
            if val is not None:
                return val
        elif minhlen < maxhlen:
            val = self.maxheap.peek()
            if val is not None:
                return val
        val1 = self.minheap.peek() 
        val2 = self.maxheap.peek() 
        assert val1 is not None
        assert val2 is not None
        return (val1+val2)/2
            
        
        