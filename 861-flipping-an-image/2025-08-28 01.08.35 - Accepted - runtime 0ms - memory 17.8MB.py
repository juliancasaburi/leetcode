class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            l, r = 0, len(i) - 1

            while l <= r:
                # Invert the bit using XOR with 1
                i[l], i[r] = i[r] ^ 1, i[l] ^ 1
                l += 1
                r -= 1

        return image
