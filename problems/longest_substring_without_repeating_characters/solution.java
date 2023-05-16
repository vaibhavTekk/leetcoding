class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] c = s.toCharArray();
        int n = c.length;
        if (n == 0){
            return 0;
        } else if (n == 1){
            return 1;
        }
        int i = 0;
        int j = 1;
        int max = 0;
        String substr = "" + c[0];
        while(j < n){
            if(!substr.contains(Character.toString(c[j]))){
                substr = substr.concat(Character.toString(c[j]));
                j++;
            } else {
                substr = "" + c[i];
                i++;
                j = i;
            }
            
            if (substr.length() > max){
                max = substr.length();
            }
        }
        return max;
    }
}