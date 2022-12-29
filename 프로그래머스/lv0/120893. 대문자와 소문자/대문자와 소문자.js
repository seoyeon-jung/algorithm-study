function solution(my_string) {
    let arr = [...my_string]
    let new_arr = [];  // 새로운 배열 생성
    
    arr.forEach((x) => {
        // toUpperCase 대문자로 변환
        // toLowerCase 소문자로 변환
        if (x === x.toUpperCase()) {
            new_arr.push(x.toLowerCase())
        }
        else {
            new_arr.push(x.toUpperCase())
        }
    })
    
    return new_arr.join('')
    
}