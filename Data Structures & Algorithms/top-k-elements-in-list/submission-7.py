class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:  hashmap[n] = 1 + hashmap.get(n, 0)
        
        arr = (sorted(list(hashmap)))

        output = []

        for i in range(k):
            maxKey = max(hashmap, key=hashmap.get)

            hashmap.pop(maxKey)

            output.append(maxKey)
        
        return output