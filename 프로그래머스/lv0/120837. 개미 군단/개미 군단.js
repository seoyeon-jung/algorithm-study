function solution(hp) {
    // 장군개미 : 5 / 병정 개미 : 3 / 일개미 : 1
    // 23인 경우 : 장군 * 4 + 병정 * 1
    // 최소한의 병력으로 구성하는 방법 찾기
    
    let ant1 = Math.floor(hp / 5);
    let ant2 = Math.floor((hp % 5) / 3);
    let ant3 = Math.floor((hp %  5) % 3);
    
    const answer = ant1 + ant2 + ant3;
    
    return answer;
}