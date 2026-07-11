'''

String get(String key, int timestamp)
    -> returns a value that was set previously with timestamp_prev <= timestamp
    -> if there are multiple values, it returns the value associated with the largest
    timestamp_prev
    -> if there are no values it returns empty string

Knowns
* can store multiple values using same key
* storage occurs based on key and timestamp
* all the timestamps of set are strictly increasing!

Questions
* can you store multiple values for the same key and same timetamp?
    * I assume no because in the constraints it said all timestamps 
    are strictly increasing
* can you store multiple values for the same key but different timestamp?
    yes


Data Structure
- hashmap
    key - key string
    - hashmap
        timestamp - int secondary key
        value

- hashmap 2 -- can't use this data structure because the end user might request a timestamp
value that's less than the max timestamp...
    key - key string
    value - max timestamp from the previous set

Set
    * lookup[key][timestamp] = value <-- pseudocode for it
    * if a key already exists for this lookup
        * replace hashmap 2's key value pair with the new timestamp as its strictly increasing

get
    * obtain length of lookup[key] as that will hold multiple timestamp to value pairs
    * since timestamp is contrained between 0 to 10^7 we can further constrain it to
        be between 0 to max(lookup[key]) where we obtain the max timestamp set so far...

    - happy case the exact key and timestamp found a value
        -> return lookup[key][timestamp]
    
    - key doesn't exist case
        -> return ""

    - timestamp doesn't exist case
        - lookup into hashmap 2 to find the max timestamp from a previous set
            - use that max timestamp to obtain the previous one and return the previous time stamp's value for that key
            - this ensures you always using the largest timestamp_prev

    Linear approach would be to check each timestamp going from requested timestamp
        down to 0
            and return the first one that has the value

    Use Binary Search to locate the largest previous timestamp
        search space is between 0 to requested timestamp
        * check if requested timestamp exists a value
            - if no, then 
'''


class TimeMap:

    def __init__(self):
        # outer key - key string
        # inner key - int timestamp
        # value - value string
        self.lookup = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.lookup:
            self.lookup[key] = {}

        self.lookup[key][timestamp] = value    

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.lookup:
            return ""

        if timestamp not in self.lookup[key]:
            lower, upper = 0, timestamp - 1
            mid = (lower + upper) // 2
            
            timestamp_prev = mid
            while lower <= upper:
                mid = (lower + upper) // 2
                if mid in self.lookup[key]:
                    timestamp_prev = mid
                    lower = mid + 1
                else:
                    if upper not in self.lookup[key]:
                        upper -= 1
                    else:
                        timestamp_prev = upper
                        break
                    if lower not in self.lookup[key]:
                        lower += 1
                
            # sanity check to ensure value exists in the key timestamp pair
            # if not, then return empty string
            if timestamp_prev not in self.lookup[key]:
                return ""

            return self.lookup[key][timestamp_prev]

        return self.lookup[key][timestamp]
        
    def printTable(self):
        for k in self.lookup:
            for t in selfself.lookup[k]:
                print(f"{k} - {t} - {self.lookup[k][t]}")
        print()
