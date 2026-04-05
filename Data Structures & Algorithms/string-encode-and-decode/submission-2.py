'''
Task
* create an algo to encode a list of strings INTO A STRING
1. create an encode function --> converts list of strings into a string
2. create a decode function --> converts string into list of strings


knowns:
* string can be empty
* string max size is 100
* string list size between 0 and 200

Convert the characters into numbers that are separated by commas? ==> encoded

* comma would separate the ascii numbers apart
* semicolon acts as a separator between separate strings

convert numbers back into characters ==> decoded

Questions:
1. should the strings have a separator character so it knows that its in list format?
2. is semicolon a valid ASCII character? Can I use carraige return as a separator here?
3. can the string have an arbitrary amount of whitespace?

1st approach
* use a non-ascii character to separate...

2nd approach
1. ascii character to number table
2. number to ascii character table

-- encoding --
* convert each ascii character to its numerical value and store each number in a string separated by commas
* strings from original list is separated by semicolons

-- decoding --
* split ascii numbers by semicolons
* for each string represented as a comma separated ascii values, split by commas
* convert numbers back to characters by using a number to ascii character table

'''


class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for j in range(len(strs)):
            s = strs[j]

            # add empty string case here -- first value in comma separated list will be length of string
            output += str(len(s))
            if len(s) > 0:
                output += ","

            for i in range(len(s)):
                c = s[i]
                output += str(ord(c))
                if i < len(s) - 1:
                    output += ","
            
            if j < len(strs) - 1:
                output += ";"

        return output

    def decode(self, s: str) -> List[str]:
        # edge case if nothing was passed in at all...
        if len(s) == 0:
            return []
        
        str_list = []

        # split by strings -- semicolon
        str_numbers = s.split(";")
        str_char_list = []
        # split by character numbers -- commas
        for str_num in str_numbers:
            str_char_list.append(str_num.split(","))

        for str_chars in str_char_list:
            str_decoded = ""

            # start at 1 because index 0 will always have string length encoded for the empty string case
            for i in range(1,len(str_chars)):
                str_num = str_chars[i]
                str_decoded += chr(int(str_num))
            
            str_list.append(str_decoded)

        return str_list