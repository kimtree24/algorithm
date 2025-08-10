import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> numList = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        q.add(5);
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            if (cur > r) continue;
            if(cur >= l){
                numList.add(cur);
            }
            
            int next0 = cur * 10;
            int next5 = cur * 10 + 5;
            if (next0 <= r){
                q.add(next0);
            }
            if (next5 <= r){
                q.add(next5);
            }
        }
        if (numList.isEmpty()) return new int[]{-1};

        int[] result = new int[numList.size()];
        for(int i = 0; i < numList.size(); i++){
            result[i] = numList.get(i);
        }
        return result;
    }
}