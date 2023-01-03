function solution(array) {
    // 1. 가장 큰 수 먼저 넣기
    // 2. 가장 큰 수의 인덱스도 찾아서 넣기
    // max라는 변수를 설정해서 max와 가장 큰 수 비교하기
    
    let answer = [];
    let max = 0;
    
    for (let i = 0; i < array.length; i++) {
        max = array[max] > array[i] ? max : i
    }
    
    answer.push(array[max])
    answer.push(max)
    
    return answer
}