// 폰켓몬
const countByArray = (arr) => {
   return arr.reduce((prev, curr) => {
      prev[curr] = ++prev[curr] || 1;
      return prev;
   }, {});
};

function solution(nums) {
   var answer = 0;
   var length = nums.length;
   var countByArray_ = countByArray(nums);

   if (Object.keys(countByArray_).length <= length / 2) {
      //아이템 종류의 개수가 뽑아야 하는 아이템의 개수보다 적을 때
      answer = Object.keys(countByArray_).length;
   } else {
      // 뽑아야하는 아이템의 개수가 아이템의 종류의 개수보다 적을 때
      answer = length / 2;
   }

   return answer;
}
