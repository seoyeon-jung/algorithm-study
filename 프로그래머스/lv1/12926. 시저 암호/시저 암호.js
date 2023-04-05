function solution(s, n) {
    // 아스키 코드 이용하기
    let answer = '';
    
    for (let i = 0; i < s.length; i++) {
        let s_askii = s.charCodeAt(i); // 아스키코드로 변환
        if (s_askii >= 65 && s_askii <= 90) {
            s_askii += n;
            if (s_askii > 90) {
                s_askii -= 26; // 소문자인 경우
            }
        }
        else if (s_askii >= 97 && s_askii <= 122) {
            s_askii += n;
            if (s_askii > 122) {
                s_askii -= 26; // 대문자인 경우
            }
        }
        s_string = String.fromCharCode(s_askii); // 문자열로 변환
        answer += s_string;
    }
    
    return answer;
}