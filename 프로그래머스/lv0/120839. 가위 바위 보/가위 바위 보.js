function solution(rsp) {
    // 가위 2, 바위 0, 보 5
    // rsp 순서대로 배열 
    // new_arr 생성해서 가위바위보 조건문 만들기
    // 조건 만족 시 new_arr에 result push
    // return new_arr.join('')
    
    let rsp_arr = [...rsp];
    let new_arr = [];
    
    for (let i = 0; i < rsp_arr.length; i++) {
        if (rsp_arr[i] === '2') {
            new_arr.push('0')
        }
        else if (rsp_arr[i] === '0') {
            new_arr.push('5')
        }
        else if (rsp_arr[i] === '5') {
            new_arr.push('2')
        }
    }
    
    return new_arr.join('')
}