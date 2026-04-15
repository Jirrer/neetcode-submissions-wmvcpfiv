class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index in range(len(numbers)):
            low = index + 1
            high = len(numbers) - 1

            while (low <= high):
                mid = (low + high) // 2
                output = numbers[index] + numbers[mid]
                
                if output == target: return [min(index + 1, mid + 1), max(index + 1, mid + 1)]
                elif output < target: low = mid + 1
                else: high = mid - 1