class Solution {
    public int solution(String number) {
        int num = 0;
        
        for(int i = 0; i < number.length(); i++) {
            num += Integer.parseInt(number.substring(i, i+1));
        }
        
        int answer = num % 9;
        
        return answer;
    }
}