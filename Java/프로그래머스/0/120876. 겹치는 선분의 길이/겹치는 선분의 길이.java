class Solution {
    public int solution(int[][] lines) {
        int[] map = new int[201];

        for (int[] line : lines) {
            int start = line[0] + 100;
            int end = line[1] + 100;

            for (int i = start; i < end; i++) {
                map[i]++;
            }
        }

        int answer = 0;
        for (int count : map) {
            if (count >= 2) answer++;
        }

        return answer;
    }
}