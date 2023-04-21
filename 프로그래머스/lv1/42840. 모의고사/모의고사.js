function solution(answers) {
    // 수포자1: 1 2 3 4 5 반복
    // 수포자2: 2 1/2/3/4/5 순서 반복
    // 수포자3: 3 1 2 4 5 순서대로 2번씩 반복
    const One = [1, 2, 3, 4, 5];
    const Two = [2, 1, 2, 3, 2, 4, 2, 5];
    const Three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    // 수포자 1~3의 점수
    const score = [0, 0, 0];
    
    // 맞춘 문제 개수 구하기
    for (let i = 0; i < answers.length ; i++) {
        if (One[i % One.length] === answers[i]) {
            score[0]++
        }
        if (Two[i % Two.length] === answers[i]) {
            score[1]++
        }
        if (Three[i % Three.length] === answers[i]) {
            score[2]++
        }
    }
    
    const answer = [];
    const maxScore = Math.max(...score); // 가장 많이 맞춘 사람
    
    // 가장 많이 맞춘 사람을 answer에 담기
    for (let j = 0 ; j < score.length ; j++) {
        if (score[j] === maxScore) {
            answer.push(j + 1);
        }
    }
    
    return answer;
}