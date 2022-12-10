// https://leetcode.com/problems/sort-colors/
// https://cheonhyangzhang.gitbooks.io/leetcode-solutions/content/75_sort_colors__medium.html
public class Solution {
    public void sortColors(int[] nums) {
        int redSt=0, bluSt=nums.length-1;
        int i=0;
        while(i<bluSt+1){
            if(nums[i]==0){
                int tmp = nums[i];
                nums[i] = nums[redSt];
                nums[redSt] = tmp;
                redSt++;
                i++;
                continue;
            }
            if(nums[i] ==2){
                int tmp = nums[i];
                nums[i] = nums[bluSt];
                nums[bluSt] = tmp;
                bluSt--;
                continue;
            }
            i++;
        }
    }
}