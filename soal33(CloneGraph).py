# https://leetcode.com/problems/clone-graph/
# https://programs.programmingoneonone.com/2021/08/leetcode-clone-graph-problem-solution.html

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        new_root = Node(node.val, [])
        self.rBfs(deque([node]), set([id(node)]), {id(node): new_root})
        return new_root
        
    def rBfs(self, deq, seen, lut):
        # for i in range(len(deq)):
        #     new_val = lut[id(deq[0])]
        #     for j in deq[0].neighbors:
        #         if id(j) not in lut:
        #             lut[id(j)] = Node(j.val, [])
        #         new_val.neighbors.append(lut[id(j)])
        #         if id(j) not in seen: 
        #             deq.append(j)
        #             seen.add(id(j))
        #     deq.popleft()
        if deq: self.rBfs(deq, seen, lut)