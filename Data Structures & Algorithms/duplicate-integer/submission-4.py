class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortednums = sorted(nums)

        for index in range(len(sortednums) - 1):
            if sortednums[index] == sortednums[index + 1]: return True
        
        return False