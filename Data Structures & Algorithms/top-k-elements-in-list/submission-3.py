class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            if n in freq: freq[n] += 1
            else: freq[n] = 1

        listFreq = sorted(freq.items(), reverse = True, key = lambda item: item[1])
        
        output = [item[0] for item in listFreq]

        return output[:k]