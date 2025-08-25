class Solution {
    public int solution(String binomial) {
        int answer = 0;
        String[] str = binomial.split(" ");
        
        int first = Integer.parseInt(str[0]);
        int third = Integer.parseInt(str[2]);
        
        if (str[1].equals("+")) {
            answer = first + third;
        } else if (str[1].equals("-")) {
            answer = first - third;
        } else {
            answer = first * third;
        }
        
        return answer;
    }
}