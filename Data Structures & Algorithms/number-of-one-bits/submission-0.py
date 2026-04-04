'''
    - check if the rightmost bit is set
        - n & 1 == 1
        
        0000011
        0000001 &
        ----------
              1
    
        0010
        0001 &
        -------
           0

    - to check the next bit we shift the bits to the right by 1
    n = n >> 1

'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            
            n = n >> 1

        return count