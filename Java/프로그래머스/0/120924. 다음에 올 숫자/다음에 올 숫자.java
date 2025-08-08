class Solution{
    public int solution(int[] common){
        int firstTerm = common[1] - common[0];
        int secondTerm = common[2] - common[1];
        int lastNum = common[common.length-1];

        // 등차수열 판단
        if(firstTerm == secondTerm){
            return lastNum + firstTerm;
        }else{
            int term = secondTerm / firstTerm;
            return term * lastNum;
        }
    }
}