class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        
        StringBuilder sb = new StringBuilder();
        
        String[] str1_arr = str1.split("");
        String[] str2_arr = str2.split("");
        
        for (int i = 0; i < str1.length(); i++) {
            answer += str1_arr[i] + str2_arr[i];
        }
        
        return answer;
    }
}