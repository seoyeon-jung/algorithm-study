function solution(seoul) {
    // seoul 배열 안을 돌면서 kim을 찾아야 한다.
    // 1. 배열 안에서 kim 찾기
    // 2. kim 찾아서 그 배열의 위치 return
    
    for (let i = 0; i < seoul.length; i++) {
        if (seoul[i] === 'Kim') {
            return `김서방은 ${i}에 있다`
        }
    }
}