import java.util.*;

class Solution {
    public Integer[] solution(int[] numlist, int n) {
        Integer[] arr = new Integer[numlist.length];
        for(int i = 0; i < arr.length; i++){
            arr[i] = numlist[i];
        }
        
        Arrays.sort(arr, (a,b)->{
            int diffA = Math.abs(a - n);
            int diffB = Math.abs(b - n);
            if (diffA == diffB){
                return b - a;
            }
            return diffA - diffB;
        });
            
        return arr;
        
    }
}