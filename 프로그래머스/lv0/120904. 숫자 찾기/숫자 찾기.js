function solution(num, k) {
    // num을 문자 타입으로 변환 (toString)
    // k가 includes 인 경우 index+1 값을 return (index는 0부터 시작하니까)
    // k가 없는 경우 -1 return
    
    let answer = num.toString();
    
    if(answer.includes(k)) {
        return answer.indexOf(k) + 1
    }
    else {
        return -1
    }
}