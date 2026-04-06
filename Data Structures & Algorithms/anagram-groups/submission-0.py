'''
anagram -> string that contains exact same characters as another string but the order of characters
may be different

constraints
* all english characters lowercase
* can return output in ANY ORDER


Brainstorming
* count the number of times a character shows up in 1 string
    * tops
    * t: 1
    * o: 1
    * p: 1
    * s: 1
* dictionary
    key: string
    value: frequency dictionary
        key - character
        value - frequency

* dictionary
    key: sorted string alphabetical
    * value: array of anagrams that match the key anagram

* try sorting or re-arranging the letters in alphabetical order for each one and do a string equality
to see if one matches the other
    * act --> act
    * cat --> act
    * pots --> opst
    * stop --> opst
    * hat --> aht

    flip the key value pairs above and see which ones map to the sorted anagram string as you could have
    1 sorted anagram to many unsorted anagrams

    act --> [cat, act]
    opst --> [pots, stop]
    hat --> [hat]

    * O(C log C * N) time complexity solution because of sorting the characters alphabetically
        * N = number of strings
        * C = number of characters


pseudocode
    1. for every string in strings
        2. sort the string in alphabetical order
        3. put sorted string in hash map as the key and the value being a list containing the original string

    2. for each key in the hash map
        * add the list values into the end of the answer array

    3. return answer


'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStringsToAnagrams = {}
        
        for string in strs:
            sortedStr = ''.join(sorted(string))
            if sortedStr not in sortedStringsToAnagrams:
                sortedStringsToAnagrams[sortedStr] = []
            
            sortedStringsToAnagrams[sortedStr].append(string)

        ans = []
        for sortedString in sortedStringsToAnagrams:
            ans.append(sortedStringsToAnagrams[sortedString])

        return ans