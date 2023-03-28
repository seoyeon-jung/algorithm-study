function solution(arr)
{
    // 1. 연속된 숫자 확인
    // 2. 연속된 숫자 제거
    // 3. 새로운 배열 return
    
    let answer = [];
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== arr[i+1]) {
            answer.push(arr[i])
        }
    }
    
    return answer;
}