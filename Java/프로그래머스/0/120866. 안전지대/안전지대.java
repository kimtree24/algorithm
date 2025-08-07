class Solution {
    public int solution(int[][] board) {
        int count = 0;
        int n = board.length;

        int[] dx = {-1,0,1,-1,1,-1,0,1};
        int[] dy = {-1,-1,-1,0,0,1,1,1};

        int[][] danger = new int[n][n];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == 1){
                    danger[i][j] = 1;
                    for(int k = 0; k < 8; k++){
                        int ni = i + dx[k];
                        int nj = j + dy[k];

                        if(ni >= 0 && ni < n && nj >=0 && nj < n){
                            danger[ni][nj] = 1;
                        }
                    }
                }
            }
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(danger[i][j] == 0){
                    count++;
                }
            }
        }

        return count;
    }
}