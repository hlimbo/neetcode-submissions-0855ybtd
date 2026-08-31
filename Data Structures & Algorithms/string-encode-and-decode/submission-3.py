'''

inputs:
* list of strings

task:
* write an algo to encode a list of strings into a string
* write an algo to decode a list of strings in string format back into a list of strings


I need to guarantee that the list of strings machine 1 has will be the same list of strings
that machine 2 gets (character by character)

Questions
* will I be supporting A-Z and 0-9 characters?
* do I need to support punctuation marks, non-alphanumeric characters?
* how about characters for localization if we wanted to support spanish or chinese letters?
* how about supporting for \n \r\n \t escape characters?
* do you want to encode trailing and leading whitespace ?

Constraints
* 0 <= strs.length < 100
* <= strs[i].length < 200
* strs[i] can contain possible characters out of 256 valid ASCII characters


For the encoding process special characters
* I will use the ␄ (End of Transmission) special character to mark that the stringified list of strings is finished encoding. This would be placed as the last character in the encoded string to communicate to the decoding function when it should stop decoding. https://www.ascii-code.com/4
* I will use the ␞ (Record Separator) special character to separate between the strings in the list when it is being stringified. https://www.ascii-code.com/30

Special Cases
* empty list
    * it will have a ␄ (End of Transmission) special character
    * if the decoder sees this 1 character, it will interpret the list as empty and return empty list in the decoder
* strings that are empty in the string list
    * it will have a NUL (␀) (https://www.ascii-code.com/0) character followed by End of Transmission special character as its encoding if it is the last item in the list
    * otherwise it will be a NUL character followed by Record Separator character in the encoding
    * this informs the decoder that the current record is an empty string

Encode Process
* for each string in the list
    if string length is zero
        - put nul character followed by record separator character if not the last string in list
        - otherwise put the nul character followed by end of transmission charaacter in the string instead

    else
        for each character in string
            - put character in end of string
            - if at last character AND not last string -> append Record Separator character
    
        if last string in list
            - append End of Transmission character

Decode Process
* for each character in encoded string
    * Special Case Empty String
        * store temp empty string to list if it encounters a nul character followed by either a record separator or end of transmission character
    * Happy Path:
        * assume that we start with the current string record
        * use a temp string variable to append characters until we reach either the Record Separator or End of Transmission special characters
    * once either special character is reached, store temp string variable into strings list variable

'''


NUL = "␀"
EOT = "␄"
RS = "␞"


class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for i in range(len(strs)):
            s = strs[i]
            if len(s) == 0:
                encodedStr += NUL
            else:
                for c in s:
                    encodedStr += c
            
            if i < len(strs) - 1:
                encodedStr += RS
            elif i == len(strs) - 1:
                encodedStr += EOT


        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedStrs = []
        tempStr = ""
        for c in s:
            if c == RS or c == EOT:
                decodedStrs.append(tempStr)
                tempStr = ""
            elif c != NUL:
                tempStr += c

        return decodedStrs