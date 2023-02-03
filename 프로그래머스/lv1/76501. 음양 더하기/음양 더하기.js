function solution(absolutes, signs) {
    // 1. true, false 로 양수/음수 구별하기
    // => true면 그냥 + / false면 - 붙이기
    // 2. 구별한 수 전부 더하기
    
    let answer = 0;
    
    for (let i = 0; i < absolutes.length; i++) {
        if (signs[i] === true) {
            answer = answer + absolutes[i]
        }
        else {
            answer = answer - absolutes[i]
        }
    }
    
    return answer;
}