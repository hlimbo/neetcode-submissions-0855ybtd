'''
input:
    * string s
    * only uppercase english characters
    * int k

* k is used to perform AT MOST k replacements with any other uppercase english characters

task:
* after performing at most k replacements, return length of longest substring
which contains only 1 distinct character

Find the longest repeating substring

* Insight: I can use k to replace a character that breaks the streak
with the same character. For example QQQQQQRQ   K = 1
    - 6 Q's followed by an R which breaks the streak
        - since K > 0, I can decrement K by 1 to replace R with Q to restore the streak


Examples:
* ABC
* K = 0
* Answer: 1

* ABCD
* K = 2
* Answer: 3

The problem with using a frequency counter for a dictionary is that
I don't know where the "holes" in the streak of characters are
and assuming that the max length of it is the frequency is incorrect
because the counting could result in invalid substring...

in 1 pass, I could construct a max frequency counter dictionary
* key = char
* value = max number of times the same character repeats in a row

in 2nd pass
* for each key in max frequency counter
    * compare maxFrequencyCounter[key] + k to maxLength
        - goal: obtain longest repeating character with replacement
        - caveat: ensure maxFrequencyCounter[key] + k is capped at len(s)
        - if min(maxFrequencyCounter[key] + k, len(s)) > maxLength:
            replace maxLength with min(maxFrequencyCounter[key] + k, len(s))


Approach 3: --> the issue with this design is that I'd have to count the number of times streak broken for all other characters i already visited in string resulting in an O(N^2) time complexity....
* dictionary
    * key - char in string
    * value - tuple
        (first_occurrence_index_of_key, last_occurrence_index_of_key, number_of_times_streak_broken + left and right boundaries)


Approach 4:
    * have a moving window for the frequency dictionary
        * before left pointer moves to right, decrement freqDict[s[leftPointer]] by 1
            - left pointer moves to right when number of replacments exceeds k
        * when right pointer moves to right, increment freqDict[s[rightPointer]] by 1
            - look for max frequency and char associated with max frequency here

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # key = character
        # value = number of times character appears in substring window
        freqCounter = {}
        leftPointer, rightPointer = 0, 0
        maxLength = 0
        # this works because s.length can be as small as length 1
        maxChar = s[0]
        maxFreq = 1

        while rightPointer < len(s):
            if s[rightPointer] not in freqCounter:
                freqCounter[s[rightPointer]] = 0

            freqCounter[s[rightPointer]] += 1
            if maxFreq < freqCounter[s[rightPointer]]:
                maxFreq = freqCounter[s[rightPointer]]
                maxChar = s[rightPointer]

            # print(f"maxChar: {maxChar}")
            # print(f"maxFreq: {maxFreq}")
            # print(f"s[rightPointer]: {s[rightPointer]}")

            substrLength = rightPointer - leftPointer + 1
            replacementCount = substrLength - maxFreq
            # print(f"substrLength: {substrLength}")
            # print(f"replacementCount: {replacementCount}")
            if replacementCount <= k:
                maxLength = max(maxLength, min(maxFreq + replacementCount, len(s)))
            else:
                maxLength = max(maxLength, min(maxFreq + k, len(s)))
                # shrink window size
                freqCounter[s[leftPointer]] -= 1
                # reset maxFreq to 0 so that on the next iteration the updated maxFreq can be calculated
                # properly. why? because you could remove 1 count of the most frequently counted character in the window
                maxFreq = 0
                leftPointer += 1

            rightPointer += 1


        return maxLength