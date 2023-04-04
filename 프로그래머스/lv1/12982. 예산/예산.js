function solution(d, budget) {
    // d의 합과 budget이 동일한지 확인
    // 동일하면 d.length만큼이 answer
    // 동일하지 않으면 최소 부서 생각
    var answer = 0;
    let d_sum = 0;  // d의 전체 합
    d.sort((a, b) => a - b);
    
    for (let i = 0; i < d.length; i++) {
        answer++;
        d_sum += d[i];
        
        if (d_sum > budget) {
            answer--;
        }
    }
    
    return answer;
}