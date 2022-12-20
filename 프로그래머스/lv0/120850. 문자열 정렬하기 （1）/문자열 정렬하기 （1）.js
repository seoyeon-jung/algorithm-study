function solution(my_string) {
    // my_string 배열로 만들기
    let my_arr = [...my_string];
    // 빈 배열 (answer이 들어갈 배열)
    let new_arr = [];
    
    // 1. my_string 안에 숫자 고르기
    // isNaN 사용해서 숫자인지 검사 후 filter
    let nums = my_arr.filter((num) => !isNaN(num));
    
    // forEach 사용해서 nums 내부의 숫자 push
    // parseInt : 문자열을 정수로 바꿈
    let answer = nums.forEach((x) => new_arr.push(parseInt(x)));
    
    // 2. 숫자 오름차순 정렬하기
    return new_arr.sort((a, b) => a - b);
}