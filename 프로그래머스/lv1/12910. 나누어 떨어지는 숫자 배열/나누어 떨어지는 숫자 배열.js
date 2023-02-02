function solution(arr, divisor) {
    // 배열 전체 돌면서 나누기
    // 나누어 떨어지는 값 배열에 추가
    // 하나도 없으면 [-1] 반환
    
    let answer = [];
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % divisor === 0) {
            answer.push(arr[i])
        }
    }
    
    return (answer.length === 0) ? [-1] : answer.sort((a, b) => a - b)
}