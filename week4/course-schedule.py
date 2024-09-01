# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.



from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def can_finish(i, graph, visited, stack):
            visited[i] = True
            stack[i] = True
            for j in graph[i]:
                if stack[j]:
                    return False
                if not visited[j]:
                    if not can_finish(j, graph, visited, stack):
                        return False
            stack[i] = False
            return True

        graph = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            graph[i].append(j)
        
        visited = [False] * numCourses
        stack = [False] * numCourses

        for i in range(numCourses):
            if not visited[i]:
                if not can_finish(i, graph, visited, stack):
                    return False
        return True
