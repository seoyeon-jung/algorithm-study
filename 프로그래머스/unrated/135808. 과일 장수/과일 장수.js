function solution(k, m, score) {
    // 1. score 오름차순 정리
    // => 비싼 것부터 묶일 수 있어서
    // 2. m개씩 묶기
    // 3. 이익 계산 (최저 점수 * m * 상자 개수)
    
    if (score.length < m) return 0;
    
    let answer = 0;
    score.sort((a, b) => a - b);
    
    while (score.length >= m) {
        const box = score.splice(score.length - m, m);
        const prize = m * box[0];
        
        answer += prize;
    }
    
    return answer;
}