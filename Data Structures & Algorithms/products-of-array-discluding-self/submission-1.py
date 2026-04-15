class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        pre, suf = [1], [1]

        for x in range(1, len(nums)):
            pre.append(pre[-1] * nums[x - 1])

        for x in range(len(nums) - 2, -1, -1):
            suf.append(suf[-1] * nums[x + 1])

        for x in range(len(nums)):
            output.append(pre[x] * suf[len(nums) - (x + 1)])

        return output