class Solution{
    public int[] solution(int num, int total){

        int centerNum = total / num;
        int[] answer = new int[num];
        int idx = 0;

        if (num % 2 == 1){
            // num이 홀수
            int numRange = num / 2;
            for (int i = centerNum - numRange; i < centerNum + numRange + 1; i++){
                answer[idx++] = i;
            }
        }else{
            // num이 짝수
            int numRange = num / 2;
            for (int i = centerNum - numRange + 1; i < centerNum + numRange + 1; i++){
                answer[idx++] = i;
            }
        }
        return answer;
    }
}