function solution(s) {
    // 1. 문자열의 길이가 4 또는 6인지 확인
    if (s.length !== 4 && s.length !== 6) return false;
        
    // 2. 숫자로만 구성되어있는지 확인
    for (let i = 0; i < s.length; i++) {
        if(isNaN(Number(s[i]))) return false;
    }
    
    // 위의 조건 제외한 경우 모두 true
    return true;
}