function solution(n) {
    const answer = [];
    
    // 약수 개수와 동일
    for (let i = 0; i <= n; i++) {
        if (n % i === 0) {
            answer.push(i);
        }
    }
    return answer.length;
}