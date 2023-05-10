class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int left = 0;
        int top = 0;
        int right = n;
        int bottom = n;
        int k = 1;
        while (left < right && top < bottom){
            for(int i = left;i < right;i++){
                matrix[top][i] = k;
                k++;
            }
            top++;
            for(int i = top;i < bottom;i++){
                matrix[i][right-1] = k;
                k++;
            }
            right--;

            if(left > right && top > bottom){
                break;
            }

            for(int i = right - 1;i >= left;i--){
                matrix[bottom-1][i] = k;                
                k++;
            }
            bottom--;
            for(int i = bottom-1;i >= top;i--){
                matrix[i][left] = k;
                k++;
            }
            left++;
        }

        return matrix;
    }
}