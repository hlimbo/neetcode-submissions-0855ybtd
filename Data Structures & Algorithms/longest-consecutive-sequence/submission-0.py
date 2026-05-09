'''
- A consecutive sequence is a sequence of elements
where each element is exactly 1 greater than previous element
- elements you pick from the original array do not need to be next to each other to count

There are dupes in this problem but we don't need to consider it as another path because of the constraint
where the previous element must be exactly 1 less than the current element

A good question to ask during an interview setting is the definition of "consecutive" in the 2nd
sentence of the prompt....

We know a number is a start of the sequence if  number - 1 does not exist in the array
* why is that the case? because if we find a number let's say 5 and there exists a 4 somewhere
else in the list, then 5 cannot be our starting sequence
* similarly, if we find a number bigger than our supposed end number, then that supposed end number
is actually a number somewhere in the middle or beginning of the sequence


- Identify all possible starting sequences by seeing if there is a value num - 1 that exists in the list
- we do this by creating a set of numbers that are from the input list
- for each number in nums, if num - 1 does not exist in numSet, add it to the list of numbers that
are considered to be a potential starting sequence

for each num in nums
 * add num to num set

starting sequences = []
for each num in nums:
    if num - 1 not in num set
        add num to starting sequences

- max_streak = 0
- for each potential starting sequences
    - copy starting sequence
    - set streak to 0
    - while copy exists in numSet
        - increase streak by 1
        - increment copy by 1

    if streak > max_streak
        max_streak = streak

    # max streak can only be big as numSet (excluding duplicates)
    if max_streak == len(numSet)
        break

return max_streak


[5 1 4 3 2 1]
answer = 5

Does that mean we can create a sequence out of order if we wanted to?

- Sorting is out of the question because it turns the overall algo to O(N Log N)
- 


Constraints:
* algo must be in O(n) time


'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)

        startingSequences = []
        # identify starting sequences
        for num in numSet:
            if num - 1 not in numSet:
                startingSequences.append(num)

        maxStreak = 0
        for start in startingSequences:
            copy = start
            streak = 0
            while copy in numSet:
                streak += 1
                copy += 1

            maxStreak = max(streak, maxStreak)

            # stop loop early as the biggest can be only the length of all unique values from the original array
            if maxStreak == len(numSet):
                break

        return maxStreak