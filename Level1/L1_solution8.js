// 소수 만들기
function solution(nums) {
   var answer = 0;
   const length = nums.length;
   for (let i = 0; i < length; i++) {
      for (let j = i + 1; j < length; j++) {
         for (let k = j + 1; k < length; k++) {
            var sum = nums[i] + nums[j] + nums[k];
            if (isPrime(sum)) answer += 1;
         }
      }
   }
   return answer;
}

const isPrime = (number) => {
   var n = 2;
   while (n * n <= number) {
      if (number % n === 0) {
         return false;
      }
      n = n + 1;
   }
   return true;
};
