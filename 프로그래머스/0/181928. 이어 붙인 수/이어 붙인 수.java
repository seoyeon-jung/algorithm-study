class Solution {
    public int solution(int[] num_list) {
        String e = "", o = "";
        
        for (int i = 0; i < num_list.length ; i++) {
            if (num_list[i] % 2 == 0) {
                e += num_list[i];
            } else {
                o += num_list[i];
            }
        }
        
        return Integer.parseInt(e) + Integer.parseInt(o);
    }
}