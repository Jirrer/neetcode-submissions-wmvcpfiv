class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            nums[index] = (nums[index], index)

        nums = sorted(nums)

        for n in range(len(nums)):
            l = n + 1
            h = len(nums) - 1

            while (l <= h):
                mid = (l + h) // 2

                outcome = nums[mid][0] + nums[n][0]

                if outcome == target: return sorted([nums[mid][1], nums[n][1]]) 
                elif outcome < target: l = mid + 1
                else: h = mid - 1

        return [0,0]