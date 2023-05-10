class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n];
        int[] postfix = new int[n];
        for(int i = 0; i < n; i++){
            if (i == 0){
                prefix[i] = nums[i];
                postfix[n - i - 1] = nums[n-i-1];
            } else {
                prefix[i] = nums[i] * prefix[i-1];
                postfix[n-i-1] = nums[n-i-1]*postfix[n-i];
            }
        }
        int arr[] = new int[n];
        for(int i = 0;i <n;i++){
            if (i == 0){
                arr[i] = postfix[i+1];
            }else if (i == n-1) {
                arr[i] = prefix[i-1];
            } else {
                arr[i] = prefix[i-1] * postfix[i+1];
            }
        }
        return arr;
    }
}