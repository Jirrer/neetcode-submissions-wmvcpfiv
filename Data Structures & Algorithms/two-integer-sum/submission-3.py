class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tupleNums = list(enumerate(nums))

        sortedNums = sorted(tupleNums, key = lambda item: item[1])

        for index in range(len(sortedNums) - 1):
            low = index + 1
            high = len(sortedNums) - 1

            while (low <= high):
                mid = (low + high) // 2

                output = sortedNums[index][1] + sortedNums[mid][1]

                if output == target: return [min(sortedNums[index][0], sortedNums[mid][0]), max(sortedNums[index][0], sortedNums[mid][0])]
                elif output < target: low = mid + 1
                else: high = mid - 1
