# Neetcode solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A 

        l, r = 0, len(A) - 1
        while True: # could be improved by checking for a deterministic while as this one
        # isn't good practice
            # midpoint for A
            i = (l + r) // 2
            # subtract by 2 because arrays start at index 0 (this is for B)
            j = half - i - 2

            # we use -infinity and positive infinity to handle the cases
            # where the indexed positions reference out of bounds items
            # using these help with the min and max calculations later on..
            Aleft = A[i] if i >= 0 else float("-infinity")
            # go too far right off bounds
            Aright = A[i+1] if i+1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            # go too far right off bounds
            Bright = B[j+1] if j+1 < len(B) else float("infinity")

            # found the correct partition
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2 != 0:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # reducing left partition of A
            elif Aleft > Bright:
                r = i - 1
            # increase left partition of A
            else:
                l = i + 1
                