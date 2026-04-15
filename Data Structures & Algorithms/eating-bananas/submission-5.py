class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        output = high

        while low <= high:
            mid = (low + high) // 2

            count = 0
            for b in piles:
                count += math.ceil(b / mid)


            if count <= h: 
                output = mid
                high = mid - 1

            else: low = mid + 1

        return output