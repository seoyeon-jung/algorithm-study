function solution(x) {
    // 1. x의 자릿수의 합 구하기
    // 2. x를 x의 자릿수의 합으로 나누기
    // 3. 나눠지면 true, 아니면 false return
    
    let new_arr = String(x).split(""); // x를 배열로 나누기
    let sum = 0; // 자릿수의 합
    
    // 1번
    for (let i = 0; i < new_arr.length; i++) {
        sum += Number(new_arr[i]);
    }
    
    // 2번-3번
    return (x % sum === 0) ? true : false
}