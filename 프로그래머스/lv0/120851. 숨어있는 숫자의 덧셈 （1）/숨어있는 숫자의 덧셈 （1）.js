function solution(my_string) {
    let answer = 0;
    const nums = my_string.split('')
    
    for (let i = 0; i < nums.length ; i++) {
        // 숫자인 경우에만 answer에 추가
        if (Number(nums[i])) {
            answer += Number(nums[i])
        }
    }
    
    return answer
}