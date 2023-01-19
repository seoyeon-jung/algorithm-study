function solution(s){
    // 1. p와 y 개수 구하기 (대,소문자 구별 X) => 전부 소문자로 바꾸기
    // 2. p, y 비교
    // 3. 같으면 true 다르면 false
    // 4. 둘다 없으면 항상 true
    
    s = s.toLowerCase();
    
    let p_len = [...s].filter(s => s === 'p').length;
    let y_len = [...s].filter(s => s === 'y').length;
    
    return p_len === y_len ? true : false
}