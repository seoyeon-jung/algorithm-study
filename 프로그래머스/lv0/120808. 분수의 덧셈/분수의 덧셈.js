function solution(denum1, num1, denum2, num2) {
    // 분모 핪 구하기
    let result_x = (denum1 * num2) + (denum2 * num1)
    // 분자
    let result_y = num1 * num2
    // 최소공배수
    let max_num = 1
    
    // 약분 (최소공배수 계산하기)
    for (let i = 1; i <= result_x; i++) {
        if (result_x % i === 0 && result_y % i === 0) {
            max_num = i
        }
    }
    
    return [result_x / max_num, result_y / max_num]
}