function solution(number) {
    // answer = 삼총사 만드는 방법의 수
    // 1. number 내에서 0이 되는 조합 찾기
    // 2. 그 조합의 개수 세기
    
    let answer = 0;
    
    for(let i = 0; i < number.length; i++) {
        for(let j = i + 1; j < number.length; j++) {
            for (let k = j + 1; k < number.length; k++) {
                if (number[i] + number[j] + number[k] === 0) {
                    answer += 1;
                }
            }
        }
    }
    
    return answer;
}