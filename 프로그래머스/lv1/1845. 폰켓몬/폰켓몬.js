function solution(nums) {
    // 1. 중복된 폰켓몬 제거
    // 2-1. 중복 제거한 배열 개수 >= N/2 : answer = N/2
    // 2-2.중복 제거한 배열 개수 < N/2 : answer = 중복 제거한 배열 개수
    var answer = [];
    const max = nums.length / 2; // =N/2
    
    for (let i = 0; i < nums.length; i++) {
        // 중복 제거한 배열 개수 < N/2인 경우
        if (answer.length < max) {
            if(!answer.includes(nums[i])) {
                answer.push(nums[i]);
            }
        }
    }
    return answer.length;
}