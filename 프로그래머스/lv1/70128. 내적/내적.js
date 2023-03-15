function solution(a, b) {
    // a[i] * b[i] 를 계속 더하면 된다
    let answer = 0;
    
    for (let i = 0; i < a.length; i++) {
        answer += a[i] * b[i]
    }
    
    return answer;
}