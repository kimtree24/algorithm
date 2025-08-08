import java.util.*;
class Solution{
    public int solution(int[] array){
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < array.length; i++){
            map.put(array[i], map.getOrDefault(array[i], 0) + 1);
        }
        int maxCountNum = 0;
        int maxCount = 0;
        int flag = 1;
        for (int num : map.keySet()){
            if (map.get(num) > maxCount){
                maxCountNum = num;
                maxCount = map.get(num);
                flag = 0;
            }else if(map.get(num) == maxCount){
                flag = 1;
            }
        }
        if (flag == 1){
            return -1;
        }else {
            return maxCountNum;
        }
    }
}