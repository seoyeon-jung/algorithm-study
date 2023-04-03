function solution(n) {
    // 1. n 3진법으로 바꾸기
    // 2. 3진법으로 바꾼 n 앞뒤로 뒤집기
    // 2. 다시 10진법으로 바꾸기
    
    let n_reverse = n.toString(3).split('').reverse().join('');
    
    return parseInt(n_reverse, 3);
}