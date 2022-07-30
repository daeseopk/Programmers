// 로또 최고 순위와 최저 순위
function solution(lottos, win_nums) {
   var answer = [];
   var answer_tmp = [];
   var numOfZero = lottos.filter((element) => element === 0).length;
   console.log(numOfZero);
   var matchNum = 0;
   win_nums.map((win_num) => {
      lottos.find((lotto) => {
         if (lotto === win_num) {
            matchNum = matchNum + 1;
         }
      });
   });
   answer_tmp.push(matchNum + numOfZero, matchNum);
   answer_tmp.map((answer_) => {
      if (parseInt(answer_) === 2) {
         answer.push(5);
      } else if (parseInt(answer_) === 3) {
         answer.push(4);
      } else if (parseInt(answer_) === 4) {
         answer.push(3);
      } else if (parseInt(answer_) === 5) {
         answer.push(2);
      } else if (parseInt(answer_) === 6) {
         answer.push(1);
      } else {
         answer.push(6);
      }
   });
   return answer;
}
