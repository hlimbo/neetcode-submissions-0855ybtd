'''
pre-requisites
[a,b]
* take b first, then you can take a

numCourses = number courses you need to take labeled from 0 to numCourses - 1

Output:
* return a valid ordering of courses you can take to finish all courses
* if its not possible to finish all courses, return empty array


* When is it not possible to finish all courses
* when there is a cyclic dependency between prerequisites
* example
[a,b]
[b,c]
[c,a]
* this example returns empty array

* If there are 0 pre-reqs: return list of courses in asc order


* You have to find courses that have zero pre-reqs
* You need a way to determine all the pre-reqs of a given course
    - dictionary A where key is the course and value is set of pre-reqs you need to take
    - dictionary B where key is the course pre-req and value is set of courses you maybe able to take next 
* You need a way to reduce the number of pre-reqs for a given course
    - remove the pre-req from Dictionary A's set by looking the course taken by key
* You need a way to detect when there exists a cyclic dependency between courses and pre-reqs
    - if you take all courses with no pre-reqs left and that count is less than numCourses, then return empty array

Pseudocode
- init dictionary A with all courses and empty set for each key
- init dictionary B with all courses and empty set for each key
- gather dictionary A (course to PreReqs)
- gather dictionary B (prereqs to courses that may be taken next)
- get all courses that have zero pre-reqs from dictionary A
    - store it in a deque data structure which will act like a queue 

while deque is not empty
    - get next course from deque
    - add it to my list of courses to take
    - do a lookup in dictionary B to find all courses that depend on this "next course"
    - for those courses
        - do a lookup in dictionary A and remove the next course taken as a pre-req for each one
        - if pre-req length of that key course is zero, add it to the deque (queue) to get taken in the future

if len(courses_taken) < numCourses:
    return []

return courses_taken
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [courseIndex for courseIndex in range(numCourses)]
        
        courseToPreReqs = {}
        preReqToCourses = {}
        for courseIndex in range(numCourses):
            courseToPreReqs[courseIndex] = set()
            preReqToCourses[courseIndex] = set()

        for prereq in prerequisites:
            courseIndex, requirement = prereq
            courseToPreReqs[courseIndex].add(requirement)
            preReqToCourses[requirement].add(courseIndex)

        courseQueue = deque()

        for courseIndex in courseToPreReqs:
            prereqs = courseToPreReqs[courseIndex]
            count = len(prereqs)
            if count == 0:
                courseQueue.append(courseIndex)

        courseList = []
        while len(courseQueue) > 0:
            courseToTake = courseQueue.popleft()
            courseList.append(courseToTake)

            availableCourses = preReqToCourses[courseToTake]
            for availableCourse in availableCourses:
                courseToPreReqs[availableCourse].remove(courseToTake)
                if len(courseToPreReqs[availableCourse]) == 0:
                    courseQueue.append(availableCourse)

        if len(courseList) < numCourses:
            return []

        return courseList
        