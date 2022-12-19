function solution(n, t) {
    // 1시간에 2배씩 증가
    // 항상 n의 t 제곱만큼 세균이 증가한다 => 틀림 (잘못된 생각)
    // n * 2 ) * 2 ) * 2 ... 2를 t만큼 곱함
    // 반복문 사용해서 계속 2 곱하기
    
    let answer = n;
    
    for (let i = 0 ; i < t; i++) {
        answer *= 2
    }
    
    return answer;
}