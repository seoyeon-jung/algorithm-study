class Solution {
    public int solution(int n, int k) {
        int n_sum = 12000 * n;
        int k_sum = 2000 * (k - n/10);
        return n_sum+k_sum;
    }
}