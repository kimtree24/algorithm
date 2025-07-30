import java.util.*;

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        List<String> stringSet = new ArrayList<>();
        stringSet.add("aya");
        stringSet.add("ye");
        stringSet.add("woo");
        stringSet.add("ma");
        
        for (int i = 0; i < babbling.length; i++){
            Boolean isValid = true;
            
            for (int j = 0; j < stringSet.size(); j++ ){
                
                if(babbling[i].contains(stringSet.get(j)+stringSet.get(j))){
                    isValid = false;
                    break;
                }
            }
            if (!isValid){
                continue;
            }
            
            for (int j = 0; j < stringSet.size(); j++){
                babbling[i] = babbling[i].replace(stringSet.get(j), " ");
            }
            if (babbling[i].trim().equals("")){
                answer++;
            }
            
        }
        
        return answer;
    }
}