class Solution {
    public int min(int a, int b){
        if(a < b){
            return a;
        } else {
            return b;
        }
    }
    
    public int max(int a, int b){
        if(a > b){
            return a;
        } else {
            return b;
        }
    }

    public int maxProduct(int[] nums) {
        int currmin = 1;
        int currmax = 1;
        int max = -1000;
        for(int i = 0; i < nums.length; i++){
            if (nums[i] > max){
                max = nums[i];
            }
        }
        for(int i = 0; i < nums.length; i++){
            if (nums[i] == 0){
                currmin = 1;
                currmax = 1;
            } else {
                int p1 = currmin * nums[i];
                int p2 = currmax * nums[i];
                currmin = min(min(p1,p2),nums[i]);
                currmax = max(max(p1,p2),nums[i]);
                if(currmax > max){
                    max = currmax;
                }
            }
        }

        return max;

    }
}