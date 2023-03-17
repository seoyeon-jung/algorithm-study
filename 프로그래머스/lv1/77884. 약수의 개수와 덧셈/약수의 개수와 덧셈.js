function Divisor(num) {
    // 1. left~right 약수 개수 구하기
    // 1-1. 약수 개수 구하는 함수 만들기
    // 1-2. 그 함수 적용해서 전체 숫자의 약수 개수 구하기
    let index = 1;  // 약수 개수 구하기 위한 숫자
    let count_num = 0; // 약수 개수
    
    while (index <= num) {
        if (num % index === 0) {
            count_num += 1;
        }
        index +=1;
    }
    
    return count_num;
}

function solution(left, right) {
    // 2. 짝수면 더하고 홀수는 빼기
    let answer = 0;
    
    // left~right 전체 더해야 하므로 for문 사용
    for (let i = left; i <= right; i++) {
        let num = Divisor(i);
        
        // 짝수면 더하고, 홀수면 빼기
        if (num % 2 === 0) {
            answer += i;
        }
        else {
            answer -= i;
        }
    }
    
    return answer;
}