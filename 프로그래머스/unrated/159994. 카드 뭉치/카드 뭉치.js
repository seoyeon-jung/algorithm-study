function solution(cards1, cards2, goal) {
    // 카드 순서대로 사용, 재사용 불가, 순서 변경 불가
    // goal 안에 cards1, cards2 가 있으면 Yes
    // 없으면 No 출력
    
    let w1 = 0; // cards1 안에 있는 word
    let w2 = 0; // cards2 안에 있는 word
    
    // goal length만큼 for문 돌리기
    for (let word of goal) {
        // w1와 일치하면 w1++
        if (cards1[w1] === word) {
            w1++;
        }
        // w2와 일치하면 w2++
        else if (cards2[w2] === word) {
            w2++;
        }
        // 일치하지 않다는 의미이므로 No 출력
        else return "No";
    }
    return "Yes"
}