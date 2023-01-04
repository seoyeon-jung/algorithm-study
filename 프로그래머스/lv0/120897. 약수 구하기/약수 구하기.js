function solution(n) {
    // 1. n의 약수 계산
    // 2. 약수 오름차순으로 정렬
    
    let answer = [];
    
    for(let i = 1; i <= n; i++) {
        if (n % i === 0) {
            answer.push(i)
        }
    }
    
    return answer
}