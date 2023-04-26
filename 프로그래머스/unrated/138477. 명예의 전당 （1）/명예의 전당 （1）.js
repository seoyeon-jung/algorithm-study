function solution(k, score) {
    // 1. k일 이후부터는 k+1일차 들어오는 score와 기존 점수 비교
    // 2. 비교 후 작은 점수는 삭제
    // => k일차만큼 최하위 점수를 anwer 배열에 담기
    
    let answer = []; // 최하위 점수
    let honor_place = [];  // 명예의 전당
    
    // 모든 점수 돌면서 비교
    for (let i = 0; i < score.length; i++) {
        // k일 보다 작으면 그냥 명예의 전당에 넣기
        if (i < k) {
            honor_place.push(score[i])
        }
        
        // k일 이후 점수 비교하기
        if (score[i] > Math.min(...honor_place)) {
            // 가장 작은 수 honor_place에서 삭제
            honor_place.pop()
            honor_place.push(score[i])
            honor_place.sort((a, b) => b - a) // 내림차순 정렬
        }
        answer.push(Math.min(...honor_place)) // 최하위 점수를 answer에 push
    }
    return answer;
}