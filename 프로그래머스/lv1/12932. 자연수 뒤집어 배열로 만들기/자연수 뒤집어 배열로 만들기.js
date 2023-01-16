function solution(n) {
    // 1. n 순서 뒤집기 (reverse)
    // 2. 배열 형태로 바꾸기
    
    let result = [];  // return 할 배열 형태
    let n_arr = String(n).split('').reverse().map(num => Number(num));
    
    for (let i = 0; i < n_arr.length; i++) {
        result[i] = Number(n_arr[i])
    }
    
    return result;
}