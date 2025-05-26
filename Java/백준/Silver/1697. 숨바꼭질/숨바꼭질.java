import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int SP = Integer.parseInt(st.nextToken());
        int DP = Integer.parseInt(st.nextToken());
        
        int MAX = 100001;
        boolean[] visited = new boolean[MAX];
        int[] time = new int[MAX];
      
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(SP);
        visited[SP] = true;
        time[SP] = 0;
        
        while(!queue.isEmpty()){
            int current = queue.poll();
            
            if (current == DP){
                System.out.println(time[current]);
                return;
            }
            int[] nextPoint = new int[3];
            nextPoint[0] = current - 1;
            nextPoint[1] = current + 1;
            nextPoint[2] = current * 2;
            
            for(int next : nextPoint){
                if(next >=0 && next < MAX && !visited[next]){
                    queue.offer(next);
                    visited[next] = true;
                    time[next] = time[current] + 1;
                }
            }
        }
    }
}