import java.util.*;

class Solution {
    public int[] solution(int[][] score) {
        int n = score.length;
        int[] sum = new int[n];
        int[] rank = new int[n];

        for (int i = 0; i < n; i++) {
            sum[i] = score[i][0] + score[i][1];
        }

        for (int i = 0; i < n; i++) {
            int tempRank = 0;
            for (int j = 0; j < n; j++) {
                if (sum[j] > sum[i]) tempRank++;
            }
            rank[i] = tempRank + 1;
        }

        return rank;
    }
}