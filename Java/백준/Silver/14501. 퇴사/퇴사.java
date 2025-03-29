import java.util.*;
import java.io.*;

public class Main{
    static int N;
    static int[] T, P;
    static int max = 0;
    
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        N = Integer.parseInt(br.readLine());
        T = new int[N];
        P = new int[N];
        
        for(int i = 0; i < N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            T[i] = Integer.parseInt(st.nextToken());
            P[i] = Integer.parseInt(st.nextToken());
        }
        getMax(0,0);
        System.out.println(max);
        }
    public static void getMax(int day, int profit){
        if (day >= N){
            max = Math.max(max, profit);
            return;
        }
        getMax(day+1, profit);
        
        if (day + T[day] <= N){
            getMax(day+T[day], profit + P[day]);
        }
    }
    }