function solution(s) {
    // 단어가 홀수인지 짝수인지 먼저 계산
    // 홀수면 하나만, 짝수라면 두 글자 return
    let answer = '';
    
    if (s.length % 2 === 0) {
        answer =  s[s.length / 2 - 1] + s[s.length / 2];
    }
    else {
        answer = s[Math.floor(s.length/2)];
    }
    
    return answer;
}