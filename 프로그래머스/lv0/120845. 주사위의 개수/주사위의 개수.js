function solution(box, n) {
    // 가로 10, 세로 8, 높이 6 / 모서리 3 => 12개
    // 가로 3개 세로 2개 높이는 2 => 3 * 2 * 2 = 12
    // 가로/세로/높이 모서리로 나눈 값끼리 곱하기
    
    let a = Math.floor(box[0] / n);
    let b = Math.floor(box[1] / n);
    let c = Math.floor(box[2] / n);
    
    return a * b * c;
}