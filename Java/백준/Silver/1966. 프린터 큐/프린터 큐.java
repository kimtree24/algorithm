import java.util.*;
import java.io.*;

public class Main{
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int testCase = Integer.parseInt(br.readLine());
        
        for(int i = 0; i < testCase; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int docNum = Integer.parseInt(st.nextToken());
            int ansDoc = Integer.parseInt(st.nextToken());
            
            Queue<int[]> queue = new LinkedList<>();
            st = new StringTokenizer(br.readLine());
            
            PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
            
            for(int j = 0; j < docNum; j++){
                int importence = Integer.parseInt(st.nextToken());
                queue.offer(new int[] {j, importence});
                priorityQueue.offer(importence);
            }
            int count = 0;
            
            while(!queue.isEmpty()){
                int[] current = queue.poll();
                int index = current[0];
                int importence = current[1];
                
                if(importence == priorityQueue.peek()){
                    priorityQueue.poll();
                    count++;
                        
                    if(index == ansDoc){
                        System.out.println(count);
                        break; 
                    }
                }else{
                    queue.offer(current);
                }
            }
            
            
            
        }
    }
}