class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        for num in range(n+1):
            # count bits for num
            count = 0
            while num > 0:
                if num & 1 == 1:
                    count += 1
                num = num >> 1
            counts.append(count)

        return counts