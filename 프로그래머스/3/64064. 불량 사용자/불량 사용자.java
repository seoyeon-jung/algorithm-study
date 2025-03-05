import java.util.*;

class Solution {
    String[] userIds; // 전체 id 배열
    String[] bannedIds; // 불량 id 배열
    boolean[] visited; // 방문 여부 boolean
    // 조건 만족하는 id들 넣을 hash set
    HashSet<HashSet<String>> result = new HashSet<>();
    
    public int solution(String[] user_id, String[] banned_id) {
        // 초기화
        userIds = user_id;
        bannedIds = banned_id;
        visited = new boolean[userIds.length];
        
        dfs(new HashSet<>(), 0);
        
        return result.size();
    }
    
    private void dfs(HashSet<String> set, int depth) {
        if (depth == bannedIds.length) {
            result.add(set);
            return;
        }
        
        for (int i = 0; i < userIds.length; i++) {
            if (set.contains(userIds[i])) {
                continue;
            }
            
            if (check(userIds[i], bannedIds[depth])) {
                set.add(userIds[i]);
                dfs(new HashSet<>(set), depth + 1);
                set.remove(userIds[i]);
            }
        }
    }
    
    private boolean check(String userId, String bannedId) {
        if (userId.length() != bannedId.length()) {
            return false;
        }
        
        boolean match = true;
        
        for (int i = 0; i < userId.length(); i++) {
            if (bannedId.charAt(i) != '*' && userId.charAt(i) != bannedId.charAt(i)) {
                match = false;
                break;
            }
        }

        return match;
    }
}