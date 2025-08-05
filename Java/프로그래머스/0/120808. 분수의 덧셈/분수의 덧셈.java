class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int boonmo = denom1 * denom2;
        int boonja = (numer1 * denom2) + (numer2 * denom1);

        for (int i = boonja; i >= 2; i--){
            if(i > boonja || i > boonmo) continue;

            if(boonja % i == 0 && boonmo % i == 0){
                boonja = boonja / i;
                boonmo = boonmo / i;
            }
        }
        int[] answer = {boonja, boonmo};
        return answer;
    }
}