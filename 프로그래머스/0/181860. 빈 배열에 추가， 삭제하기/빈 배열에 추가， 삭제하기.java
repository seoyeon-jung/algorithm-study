import java.util.*;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        List<Integer> arrList = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            if (flag[i]) {
                int num = arr[i];
                for (int j = 0; j < num * 2; j++) {
                    arrList.add(num);
                }
            } else {
                int num = arr[i];
                int size = arrList.size();
                
                if (size >= num) {
                    for (int j = 0; j < num; j++) {
                        arrList.remove(size - 1 - j);
                    }
                }
            }
        }
        
        int[] answer = new int[arrList.size()];
        
        for (int i = 0; i < arrList.size(); i++) {
            answer[i] = arrList.get(i);
        }
        
        return answer;
    }
}