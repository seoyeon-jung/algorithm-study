function solution(numbers) {
    // numbers 0 ~ 9 사이에 없는 거 찾기
    // 찾아서 더하기
    
    let answer = 0;
    
    for (let i = 0; i < 10; i++) {
        if (!(numbers.includes(i))) {
            answer += i;
        }
    }
    
    return answer;
}