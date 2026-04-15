class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        outputs = []

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2

            count = 0
            for b in piles:
                count += math.ceil(b / mid)

            if count <= h: outputs.append(mid)

            if count <= h: high = mid - 1
            else: low = mid + 1



        return min(outputs)