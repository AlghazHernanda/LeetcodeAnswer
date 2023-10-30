# https://medium.com/codex/solving-graph-problems-course-schedule-374ead04cfcd
# https://leetcode.com/problems/course-schedule/

from collections import deque 
# solusi
class Solution:
       
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # jika panjang prerequisites == 0
        if len(prerequisites) == 0:
            return True
        
        graph = [[] for _ in range(numCourses)]
        
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
            
        
        queue = deque()
        
        for i in range(0, len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0 

        while len(queue) > 0:
            current = queue.popleft()
            
            if indegree[current] == 0:
                count += 1
                
            if not graph[current]:
                print(f'{current} doesnt exit in {graph}')
                continue
                        
            for neighbour in graph[current]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                
        
        return True if count == numCourses else False