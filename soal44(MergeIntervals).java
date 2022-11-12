// https://leetcode.com/problems/merge-intervals/
// https://levelup.gitconnected.com/java-algorithms-merge-intervals-leetcode-24a3277cfa28

class Solution {
   public int[][] merge(int[][] intervals)
{
   Arrays.sort(intervals, (a, b) ->
   {
      if (a[1] == b[1])
      {
         return a[0] - b[0];
      }

      return a[1] - b[1];
   });

   LinkedList<int[]> list = new LinkedList<>();
   for (int[] interval : intervals)
   {
      if (!list.isEmpty() && list.getLast()[1] >= interval[0])
      {

         while (!list.isEmpty() && list.getLast()[1] >= interval[0])
         {
            interval[0] = Math.min(list.getLast()[0], interval[0]);
            interval[1] = Math.max(list.getLast()[1], interval[1]);
            list.removeLast();
         }
      }

      list.addLast(interval);
   }

   int pos = 0;
   int[][] answer = new int[list.size()][];
   for (int[] inteval : list)
   {
      answer[pos++] = inteval;
   }

   return answer;
}
}