import java.util.*;
import java.io.*;

public class Main{
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));    
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int numN1 = Integer.parseInt(st.nextToken());
        int numN2 = Integer.parseInt(st.nextToken());
        
        String N1 = br.readLine();
        String N2 = br.readLine();
        
        int T = Integer.parseInt(br.readLine());
        
        StringBuilder sb = new StringBuilder();
        for(int i = numN1 - 1; i >= 0; i--){
            sb.append(N1.charAt(i));
        }
        sb.append(N2);

        char[] ants = sb.toString().toCharArray();
        
        while(T > 0){
            for(int i = 0; i < ants.length - 1; i++){
                if(N1.indexOf(ants[i]) != -1 && N2.indexOf(ants[i+1]) != -1){
                    char temp = ants[i];
                    ants[i] = ants[i + 1];
                    ants[i + 1] = temp;
                    i++;
                }
            }
            T--;
        }
        
        System.out.println(String.valueOf(ants));
    }
}