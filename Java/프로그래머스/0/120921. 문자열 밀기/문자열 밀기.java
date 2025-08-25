class Solution {
    private String rotateRight(String str) {
        int len = str.length();
        String rotatedStr = str.charAt(len - 1) + str.substring(0, len - 1);
        return rotatedStr;
    }

    public int solution(String A, String B) {
        if (A.length() != B.length()){
            return -1;
        }
        if (A.equals(B)){
            return 0;
        } 

        String rotated = A;
        for (int i = 1; i <= A.length(); i++) {
            rotated = rotateRight(rotated);
            if (rotated.equals(B)) {
                return i;
            }
        }

        return -1;
    }
}