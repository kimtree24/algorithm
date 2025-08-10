class Solution {
    public String solution(String code) {
        int mode = 0;
        StringBuilder sb = new StringBuilder();
        
        for (int idx = 0; idx < code.length(); idx++){
            if(mode == 0){
                if(code.charAt(idx) != '1'){
                    if(idx % 2 == 0){
                        sb.append(code.charAt(idx));
                    }
                }else if(code.charAt(idx) == '1'){
                    mode = 1;
                }
            }else if(mode == 1){
                if(code.charAt(idx) != '1'){
                    if(idx % 2 != 0){
                        sb.append(code.charAt(idx));
                    }
                }else if(code.charAt(idx) == '1'){
                    mode = 0;
                }
            }
        }
        
        if(sb.length() == 0){
            return "EMPTY";
        }else{
            return sb.toString();
        }
    }
}