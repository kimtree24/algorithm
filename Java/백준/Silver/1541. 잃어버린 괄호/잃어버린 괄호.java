import java.util.*;
import java.io.*;

public class Main{
    public static void main(String [] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        
        int sum = 0;
      
        String[] splitedByMinus = line.split("-");
        
        for(int i = 0; i < splitedByMinus.length; i++){
            String[] addition = splitedByMinus[i].split("\\+");
            
            int sumAddition = 0;
            for(int j = 0; j < addition.length; j++){
                sumAddition += Integer.parseInt(addition[j]);
            }
            
            if(i == 0){
                sum = sumAddition; 
            }else{
                sum -= sumAddition;
            }
        }
        System.out.println(sum);
      }
    }