class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums): return 0
        
        arr = sorted(nums)

        count, most = 1, 1
        for i in range(1, len(nums)):
            if arr[i - 1] == arr[i]: continue
            elif arr[i - 1] == arr[i] - 1: count += 1
            else: count = 1
            
            if count > most: most = count

        return most
        