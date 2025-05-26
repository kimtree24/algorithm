import java.util.*;
import java.io.*;

public class Main{
    static class FastWay {
        int start;
        int end;
        int weight;
        public FastWay(int start, int end, int weight){
            this.start = start;
            this.end = end;
            this.weight = weight;
        }
    }
    
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int num = Integer.parseInt(st.nextToken());
        int lenWay = Integer.parseInt(st.nextToken());
        
        List<FastWay> fastWays = new ArrayList<>();
        
        for (int i = 0; i < num; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            
            if(end > lenWay || end-start <= weight){
                continue;
            }
            
            fastWays.add(new FastWay(start, end, weight));
        }
        
        int[] road = new int[lenWay + 1];
        Arrays.fill(road, Integer.MAX_VALUE);
        road[0] = 0;
        
        for(int i = 0; i <= lenWay; i++){
            if(i>0){
                road[i] = Math.min(road[i], road[i-1] + 1);
            }
            
            for (FastWay fw : fastWays){
                if (fw.start == i){
                    road[fw.end] = Math.min(road[fw.end], road[i] + fw.weight);
                }
            }
        }
        System.out.println(road[lenWay]);
    }
}