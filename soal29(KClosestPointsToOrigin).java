// https://leetcode.com/problems/k-closest-points-to-origin/
// https://velog.io/@timevoyage/leetcode-973-K-Closest-Points-to-Origin

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] squares = new int[points.length][2];

        for (int i=0; i < points.length; i++) {
            squares[i][0] = i;
            squares[i][1] = points[i][0] * points[i][0] + points[i][1] * points[i][1];
        }

        Arrays.sort(squares, (int[] a, int[] b) -> { return a[1] - b[1];});

        List<int[]> res = new ArrayList<>();
        for (int i=0; i < k; i++) {
            int index = squares[i][0];
            res.add(new int[]{points[index][0], points[index][1]});
        }

        return res.toArray(new int[res.size()][2]);
    }
}