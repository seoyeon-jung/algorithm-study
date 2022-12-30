function solution(cipher, code) {
    // code의 배수번째 글자만 진짜 암호
    // 1. code의 배수 계산
    // => cipher 전체를 배열로 바꿔서 순서 계산해보기
    // 2. cipher 중에 배수번째만 골라오기
    // 3. 골라온 글짜를 새로운 배열에 담기
    // 4. return 새로운 배열
    
    let cipher_arr = [...cipher];
    let new_arr = [];
    
    cipher_arr.forEach((n, i) => {
        if ((i + 1) % code === 0) {
            new_arr.push(cipher_arr[i])
        }
    })
    
    return new_arr.join("")
}