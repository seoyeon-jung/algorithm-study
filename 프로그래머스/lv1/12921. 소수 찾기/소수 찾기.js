function solution(n) {
    // 1. 소수 배열
    let answer = [];
    
    // 소수인지 판별하는 함수
function isPrime (n) {
    for(let x of answer) {
        if(x > Math.sqrt(n)) return true
        if(Number.isInteger(n / x)) return false
    }
    return true
}
    
    // 2. 1 ~ n 소수 찾기
    for (let i = 2 ; i <= n ; i++) {
        if (isPrime(i)) answer.push(i)
    }
    
    return answer.length;
}