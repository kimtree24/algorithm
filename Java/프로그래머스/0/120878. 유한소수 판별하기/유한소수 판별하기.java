class Solution {
    public int solution(int a, int b) {

        int gcdNum = gcd(a, b);
        int boonmo = b / gcdNum;

        while (boonmo % 2 == 0){
            boonmo /= 2;
        } 
        while (boonmo % 5 == 0){
            boonmo /= 5;
        }

        if(boonmo == 1){
            return 1;
        }else{
            return 2;
        }
    }

    private int gcd(int a, int b) {
        if (b == 0){
            return a;
        }
        return gcd(b, a % b);
    }
}