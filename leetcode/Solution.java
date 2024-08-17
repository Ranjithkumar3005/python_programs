import java.util.*;

class Solution {
    public int func(int[] nums, int k) {
        int[] dum = new int[k];

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] <= nums[i + 1]) {
                for (int j = nums[i]; j <= nums[i + 1]; j++) {
                    dum[j - 1]++;
                }
            } else {
                for (int j = nums[i]; j >= nums[i + 1]; j--) {
                    dum[j - 1]++;
                }
            }
        }

        int max1 = Arrays.stream(dum).max().getAsInt();

        for (int i = 0; i < dum.length; i++) {
            if (dum[i] == max1) {
                return i + 1;
            }
        }

        return -1; // default return value (should not reach here based on the given logic)
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.func(new int[]{2, 4, 1, 3}, 5));
    }
}
