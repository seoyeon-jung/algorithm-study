import java.util.*;

class Solution {
    public String[] solution(String[] strArr) {
        List<String> arr = new ArrayList<>();
        
        for (String str: strArr) {
            if (!str.contains("ad")) {
                arr.add(str);
            }
        }
        
        String[] answer = arr.toArray(String[]::new);
        return answer;
    }
}