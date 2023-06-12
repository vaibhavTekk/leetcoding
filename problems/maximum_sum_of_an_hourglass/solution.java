class Solution {
    public int maxSum(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        if (rows < 3 || cols < 3){
            return -1;
        }
        int maxsum = 0;
        for(int i = 0;i < rows - 2;i++){
            for(int j = 0; j < cols - 2; j++){
                int sum = 0; 
                for (int k = 0;k < 3; k++){
                    // System.out.print(grid[i+k][j]);
                    sum += grid[i][j+k];
                    // System.out.print(grid[i+k][j+2]);
                    sum += grid[i+2][j+k];
                }
                // System.out.print(grid[i+1][j+1]);
                sum += grid[i+1][j+1];
                if (sum > maxsum){
                    maxsum = sum;
                } 
                // System.out.println(sum);              
            }
        }
        return maxsum;
    }
}