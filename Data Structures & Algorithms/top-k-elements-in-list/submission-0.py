class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first hash represents number frequency in nums
        # second hash flips the first hash in reverse
        # key = number of times a number in nums appears
        # value = array of nums in nums that share the same frequency
        # can keep track of the max frequency
        # and then count down by 1 and if that key exists in the 2nd hash 
        # use the numbers found in that by key and decrement k by the found amount

        numFreqs = {}
        freqsPerNums = {}
        maxFrequency = 0

        for num in nums:
            if num not in numFreqs:
                numFreqs[num] = 0
            numFreqs[num] += 1

        for num in numFreqs:
            freq = numFreqs[num]
            if freq not in freqsPerNums:
                freqsPerNums[freq] = []
            freqsPerNums[freq].append(num)
            maxFrequency = max(maxFrequency, freq)

        ans = []
        while k > 0 and maxFrequency > 0:
            if maxFrequency in freqsPerNums:
                for num in freqsPerNums[maxFrequency]:
                    ans.append(num)
                
                k -= len(freqsPerNums[maxFrequency])
            
            maxFrequency -= 1
        


        return ans