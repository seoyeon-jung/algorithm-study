function solution(numbers, direction) {
    // 오른쪽이면 오른쪽으로 한칸씩 이동 => 마지막 숫자 -> 첫번째로 이동
    // 왼쪽이면 왼쪽으로 한칸씩 이동 => 첫번째 숫자 -> 마지막으로 이동
    // => 조건문 사용해서 왼쪽/오른쪽 구별 후 이동
    
    if (direction === "right") {
        // 마지막 인덱스의 숫자를 제거한 후 맨 앞에 추가
        // pop : 마지막 요소 제거
        // unshift : 맨 앞에 추가
        numbers.unshift(numbers.pop())
    }
    else {
        // 맨 첫번째 인덱스의 숫자를 제거한 후 맨 뒤에 추가
        // shift : 첫번째 요소 제거
        numbers.push(numbers.shift())
    }
    
    return numbers
}