import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 테스트케이스 수
        int testCase = Integer.parseInt(br.readLine());
        
        // 각 테스트케이스 마다 루프
        for (int i = 0; i < testCase; i++){
            // 각 테스트케이스에 있는 날들
            int numDay = Integer.parseInt(br.readLine());
            // 날짜 만큼 배열 생성
            int[] price = new int[numDay];
            
            StringTokenizer st = new StringTokenizer(br.readLine());
            
            // 각 날짜마다 가격 넣어서 배열 생성
            for (int j = 0; j < numDay; j++){
                price[j] = Integer.parseInt(st.nextToken());
            }
            
            // 출력할 결과 값(차익)
            long result = 0;
            // 최고 가격
            int max = 0;
            
            // 루프 뒤에서 부터 돌며 최고 가격을 갱신하던가, 아니면 차익을 내던가
            for (int k = numDay-1; k >=0; k--){
                if (price[k] > max){
                    max = price[k];
                }else{
                    result += (max-price[k]);
                }
            }
            System.out.println(result);
        }
    }
}