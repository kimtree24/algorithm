import java.util.*;

class Solution {
    public String solution(String polynomial) {
        String[] tokens = polynomial.split(" ");
        
        int numOfX = 0;
        int numOfNum = 0;
        
        for (String token : tokens){
            if(token.equals("+")){
                continue;
            }
            
            if(token.contains("x")){
                
                String coef = token.substring(0, token.length() - 1);
                
                if(coef.equals("")){
                    numOfX += 1;
                }else{
                    numOfX += Integer.parseInt(coef);
                }
            }else{
                numOfNum += Integer.parseInt(token);
            }
        }
        
        if(numOfX == 0){
            return Integer.toString(numOfNum);
        }else if(numOfNum == 0){
            return (numOfX == 1 ? "x" : numOfX + "x");
        }else{
            return (numOfX == 1 ? "x" : numOfX + "x") + " + " + numOfNum;
        }
    }
}