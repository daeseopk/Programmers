// 기능개발
function solution(progresses, speeds) {
   var answer = [];
   var count = 0;
   progresses = progresses.reverse();
   speeds = speeds.reverse();

   while (progresses.length > 0) {
      if (progresses[progresses.length - 1] >= 100) {
         progresses.pop();
         speeds.pop();
         count = count + 1;
         continue;
      } else {
         for (let i = 0; i < progresses.length; i++) {
            if (count !== 0) answer.push(count);
            progresses[i] = progresses[i] + speeds[i];
            count = 0;
         }
      }
   }
   answer.push(count);

   return answer;
}
