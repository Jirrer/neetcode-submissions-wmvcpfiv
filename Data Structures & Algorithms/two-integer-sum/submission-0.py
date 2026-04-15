class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newNums = [None] * len(nums)

        for n in range(len(nums)):
            newNums[n] = (nums[n], n)

        sortedNums = sorted(newNums)

        for x in range(len(sortedNums)):
            l = x + 1
            h = len(sortedNums) - 1

            while (l <= h):
                mid = (l + h) // 2

                output = sortedNums[x][0] + sortedNums[mid][0]

                if output == target: return sorted([sortedNums[mid][1], sortedNums[x][1]])
                elif output < target: l = mid + 1
                else: h = mid - 1

