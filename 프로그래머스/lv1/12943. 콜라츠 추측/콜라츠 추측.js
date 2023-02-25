function solution(num) {
    // return => 작업 반복한 횟수
    // 짝수 => 2로 나누기
    // 홀수 => *3 + 1
    
    // 1. answer (count 하기) 정의
    let answer = 0;
    
    // 2. 횟수 반복하면서 1로 만들기
    while (num != 1) {
        if (num % 2 === 0) {
            num = num / 2;
        }
        else {
            num = num * 3 + 1;
        }
        answer += 1;
    }
    // 3. 500번 횟수 반복하겨 안되면 -1 return
    if (answer >= 500) {
        return -1;
    }
    // 3. 횟수 return
    else {
        return answer;
    }
}