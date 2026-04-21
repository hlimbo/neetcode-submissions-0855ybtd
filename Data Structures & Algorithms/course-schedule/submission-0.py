'''
Inputs:
* numCourses --> number of courses required to take
* prerequisites is a list of dependencies  between course A and B
    * prerequisites[i] = [a,b] (you need to take course B before you can take course A)
Output:
* true if you can finish all courses
    * can happen if all courses don't have pre-reqs
    * can happen if the dependency graph is acyclic
* false if you cannot finish all courses
    * this scenario can happen if you have a circular dependency
            pre-reqs = [a,b], [b,a]

Data Structures Needed
* coursesToDeps hashmap
    * key course
    * value - array of course dependencies
* depsToCourses hashmap
    * key dependency
    * value - array of courses one may be able to take next
* noCourseDepsList
    * list of courses a person can immediately take
* coursesTakenSet
    * a set of courses a student has already done

'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        
        coursesToDeps = {}
        depsToCourses = {}
        coursesTaken = set()
        noCourseDepsList = []

        # build coursesToDeps and depsToCourses adj lists
        for i in range(numCourses):
            coursesToDeps[i] = set()
            depsToCourses[i] = set()

        # add in prerequisites
        for preReq in prerequisites:
            courseA, courseB = preReq
            coursesToDeps[courseA].add(courseB)
            depsToCourses[courseB].add(courseA)

        # figure out which courses have no pre-reqs initially
        for i in range(numCourses):
            numDependencies = len(coursesToDeps[i])
            if numDependencies == 0:
                noCourseDepsList.append(i)
        
        courseIndex = 0
        while courseIndex < len(noCourseDepsList):
            currCourse = noCourseDepsList[courseIndex]

            # cyclic dependency?
            if currCourse in coursesTaken:
                print("I returned false here")
                return False

            coursesTaken.add(currCourse)

            # update number of prereqs required when finish taking a course
            nextCoursesToTake = depsToCourses[currCourse]
            for nextCourse in nextCoursesToTake:
                coursesToDeps[nextCourse].remove(currCourse)
                canTakeCourse = len(coursesToDeps[nextCourse]) == 0
                if canTakeCourse:
                    noCourseDepsList.append(nextCourse)

            courseIndex += 1

        return len(coursesTaken) == numCourses