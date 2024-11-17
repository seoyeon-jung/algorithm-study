class Solution {
    public StringBuilder solution(String my_string, int s, int e) {
        String[] newStr = my_string.split("");
        StringBuilder answer = new StringBuilder();
        
        for (int i = 0; i < newStr.length; i++) {
            if (i == s) {
                for (int j = e; j >= s; j--) {
                    answer.append(newStr[j]);
                }
            }
            if (i < s || i > e) {
                answer.append(newStr[i]);
            }
        }
        
        return answer;
    }
}