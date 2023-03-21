function solution(array, commands) {
    // 1. i번째 ~ j번째 자르기
    // 2. 정렬
    // 3. k번째 있는 수 구하기
    
    let answer = []
    
    for (let i = 0; i < commands.length; i++) {
        // commands.length만큼 반복 (k번째 수 구하는 것)
        let list = array.slice(commands[i][0]-1, commands[i]
        							[1]).sort((a,b)=>{return a-b});
        
        answer.push(list[commands[i][2]-1]);
    }
    
    return answer;
}