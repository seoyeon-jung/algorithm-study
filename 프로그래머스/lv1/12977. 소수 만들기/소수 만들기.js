function isPrime(n) {
    for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }

  return true;
}

function solution(nums) {
    // 3개의 수를 더했을 때 소수가 되어야 한다
    // nums 돌면서 3개의 수 더하는 경우의 수 생각하기
    // 소수이면 answer에 +1
    // answer return
    
    var answer = 0;
    for(i = 0; i < nums.length -2; i++) {
      for(j = i + 1; j < nums.length -1; j++) {
        for(k = j + 1; k < nums.length; k++) {
          if(isPrime(nums[i] + nums[j] + nums[k])) {
            answer++;
          }
        }
      }
    }
    return answer;
}