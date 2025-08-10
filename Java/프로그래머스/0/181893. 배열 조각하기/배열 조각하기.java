import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        int front = 0;
        int back = arr.length - 1;
        
        for (int i = 0; i < query.length; i++){
            if (i % 2 == 0){
                back = front + query[i];
            }else{
                front += query[i];
            }
        }
        
        return Arrays.copyOfRange(arr, front, back + 1);
    }
}