import java.util.*;

class Solution {
    public int solution(int[][] dots) {
        int answer = 0;

        for (int i = 0; i < 4; i++) {
            for (int j = i + 1; j < 4; j++) {
                List<Integer> dotNum = new ArrayList<>(Arrays.asList(0, 1, 2, 3));
                dotNum.remove(Integer.valueOf(i));
                dotNum.remove(Integer.valueOf(j));

                int dx1 = dots[i][0] - dots[j][0];
                int dy1 = dots[i][1] - dots[j][1];

                int dx2 = dots[dotNum.get(0)][0] - dots[dotNum.get(1)][0];
                int dy2 = dots[dotNum.get(0)][1] - dots[dotNum.get(1)][1];

                if (dx1 * dy2 == dx2 * dy1) {
                    return 1;
                }
            }
        }

        return 0;
    }
}