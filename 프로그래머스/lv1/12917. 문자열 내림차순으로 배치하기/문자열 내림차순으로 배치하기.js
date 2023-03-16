function solution(s) {
    // 1. 문자열 나누기 => split('')
    // 2. 나열 후 내림차순 => sort & reverse
    // 3, 다시 문자열로 합치기 => join('')
    
    return s.split('').sort().reverse().join('')
}