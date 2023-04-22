function solution(name, yearning, photo) {
    // name당 yearning 파악하기
    // photo의 배열 안에서 각 배열의 그리움 점수 합치기
    // result 배열 안에 push
    
    let result = [];
    
    for (let i of photo) {
        let score = 0; // yearning 점수
        
        for (let j = 0; j < name.length; j++) {
            // name과 yearning 매칭
            if (i.includes(name[j])) {
                score += yearning[j];
            }
        }
        result.push(score)
    }
    
    return result
}