function solution(a, b) {
    // 최솟값=a 최댓값=b
    // a 와 b 사이를 for문으로 돌면서 answer에 더하기
    
    let answer = 0;
    
    let num_min = Math.min(a, b);
    let num_max = Math.max(a, b);
    
    for (let i = num_min; i <= num_max; i++) {
        answer += i;
    }
    
    return answer;
}