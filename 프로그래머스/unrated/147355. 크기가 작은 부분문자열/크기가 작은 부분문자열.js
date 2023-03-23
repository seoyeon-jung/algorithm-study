function solution(t, p) {
    // 1. p의 길이와 같은 부분 문자열 구하기
    // 2. 부분문자열 <= p 인 것들 횟수 구하기
    // 3. 횟수를 return
    
    let answer = 0;
    
    for (let i = 0; i <= t.length - p.length; i++) {
        let num = t.substr(i, p.length);
        
        if (Number(num) <= Number(p)) {
            answer += 1
        }
    }
    
    return answer;
}