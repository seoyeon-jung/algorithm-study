function solution(n) {
    // 홀수면 '수', 짝수면 '박' 출력
    var answer = [];
    let i = 0;
    
    for (let i = 0; i < n; i++) {
        if (i % 2 === 0) {
            answer.push('수')
        }
        else {
            answer.push('박')
        }
    }
    
    return answer.join('');
}