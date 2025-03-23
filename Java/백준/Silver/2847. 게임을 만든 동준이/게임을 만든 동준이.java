import java.util.*;
import java.io.*;

public class Main{
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int num = Integer.parseInt(br.readLine());
        
        int[] scoreList = new int[num];
        for(int i = 0; i < num; i++){
            scoreList[i] = Integer.parseInt(br.readLine());
        }
        
        int count = 0;
        for(int i = num-1; i > 0; i--){
            if(scoreList[i] <= scoreList[i-1]){
                int diff = (scoreList[i - 1] - scoreList[i] + 1);
                scoreList[i - 1] -= diff;
                count += diff; 
            }
        }
        
        System.out.println(count);
    }
}