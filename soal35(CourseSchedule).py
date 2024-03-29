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

        # jika panjang Que masih lebih dari 0, jalankan looping ini
        while len(queue) > 0:
            current = queue.popleft()
            
            # jika index indegree == 0
            if indegree[current] == 0:
                # count + 1
                count += 1
                
            # jika bukan graph 
            if not graph[current]:
                print(f'{current} doesnt exit in {graph}')
                continue

                      # jika neighbpur di graph
            for neighbour in graph[current]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                
        # jadikan True kalo count == numCourses
        return True if count == numCourses else False