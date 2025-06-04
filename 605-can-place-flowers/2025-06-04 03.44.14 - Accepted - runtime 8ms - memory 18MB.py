class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = 0
        i = 0
        length = len(flowerbed) - 1

        while ((i <= length) and (placed != n)):
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == length) or (flowerbed[i + 1] == 0)

            if flowerbed[i] == 0 and empty_left and empty_right:
                placed += 1
                i += 2
            else:
                i += 1

        return placed == n
