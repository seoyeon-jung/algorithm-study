function solution(numbers) {
    // 두 개씩 곱해보고 최댓값 선정하기 (Math.max() 이용)
    // 조건 1) 양수x양수 , 음수x음수
    // 조건 2) 절댓값이 큰 수끼리 곱해야 최댓값
    
    let answer = [];
    
    for (let i = 0 ; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            answer.push(numbers[i] * numbers[j])
        }
    }
    
    return Math.max(...answer)
}