import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        
        List<int[]> lines = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            lines.add(new int[]{x, y});
        }
        
        Comparator<int[]> stand = Comparator.comparingInt(a -> a[0]);
        
        Collections.sort(lines, stand);
        
        int total = 0;
        int start = lines.get(0)[0];
        int end = lines.get(0)[1];
        
        for (int i = 1; i < n; i++){
            int nowStart = lines.get(i)[0];
            int nowEnd = lines.get(i)[1];
            
            if (nowStart <= end){
                end = Math.max(end, nowEnd);
            } else{
                total += end-start;
                start = nowStart;
                end = nowEnd;
            }
        }
        
        total += end-start;
        
        System.out.println(total);
        
    }
}