# https://leetcode.com/problems/insert-interval/
# https://medium.com/coding-memo/leetcode-insert-interval-c6db9681ff52

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        flag = False # mark whether inserted         
        # filter empty init
        if n==0: return [newInterval]
        # filter < start or > end
        if newInterval[1]<intervals[0][0]: return [newInterval]+intervals
        if newInterval[0]>intervals[n-1][1]: return intervals+[newInterval]        
        # overlap: newInterval[0]<=curr[1] or newInterval[1]>=curr[0]
        # compare new with curr when traversing, 
        #     if there is overlapping, 
        #         update the value in new using curr, and keep passing the modified new down
        for i in range(n):
            curr = intervals[i]
            if newInterval[0]>curr[1]: res.append(curr) # curr | new, not overlapping
            elif newInterval[0]<=curr[1]<=newInterval[1] or \
            curr[0]<=newInterval[1]<=curr[1]: # must be overlapping
                # print(curr, newInterval)
                newInterval[0] = min([newInterval[0], curr[0]])
                newInterval[1] = max([newInterval[1], curr[1]])   
            else: # newInterval[1]<curr[0] 
                # this and the future curr from inervals will > new
                # new | curr, not overlapping
                if not flag: # mark the merged used
                    res.append(newInterval) # push newInterval (modified or not) into the array
                    flag = True
                res.append(curr)              
        # if merged not used at end push it here
        if not flag: res.append(newInterval)
        return res