import java.util.*;

class Solution{
    public int solution(int a, int b, int c, int d){
        Map<Integer, Integer> map = new HashMap<>();
        
        int[] numList = {a,b,c,d};

        // 개수 세기
        for (int i = 0; i < 4 ; i++){
            map.put(numList[i], map.getOrDefault(numList[i], 0) + 1);
        }

        // 키 확인

        Set<Integer> keySet = map.keySet();
        List<Integer> keyList = new ArrayList<>(keySet);


        if(map.size() == 1){
            return 1111 * a;
        }else if(map.size() == 2){
            int p = keyList.get(0);
            int q = keyList.get(1);
            if(map.get(p) !=2){
                if(map.get(p) < map.get(q)){
                    int temp = p;
                    p = q;
                    q = temp;
                }
                return (10 * p + q) * (10 * p + q);
            }else{
                return (p + q) * Math.abs(p - q);
            }  
        }else if(map.size() == 3){
            int p = 0;
            for (int key : keyList){
                if(map.get(key) == 2){
                    p = key;
                    break;
                }
            }
            keyList.remove(Integer.valueOf(p));
            int q = keyList.get(0);
            int r = keyList.get(1);
            return q * r;
        }else if(map.size() == 4){
            keyList.sort(null);
            return keyList.get(0);
        }

        return 0;
    }
}