class Solution {
    public int solution(int a, int b) {
        String ab = String.valueOf(a) + String.valueOf(b);
        int abab = 2 * a * b;
        
        if (Integer.parseInt(ab) >= abab) {
            return Integer.parseInt(ab);
        } else {
            return abab;
        }
    }
}