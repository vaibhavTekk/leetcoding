import java.io.*;

class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int i = 0;
        int j = 1;
        int max = 0;
        if (n == 1){
            return 0;
        }
        while(j < n){
            System.out.println(i);
            System.out.println(j);
            if (prices[i] < prices[j]){
                int prof = prices[j] - prices[i];
                if (prof > max){
                    max = prof;
                }
            } else {
                i = j;
            }
            j++;
        }
        return max;
    }
}