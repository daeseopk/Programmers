// 프린터
function solution(priorities, location) {
   var answerTmp = [];
   while (priorities.length !== 0) {
      if (priorities[0] >= Math.max(...priorities)) {
         answerTmp.push(priorities[0]);
         priorities.splice(0, 1);
         if (location === 0) return answerTmp.length;
         location = location - 1;
      } else {
         var temp = priorities[0];
         for (var j = 0; j < priorities.length - 1; j++) {
            priorities[j] = priorities[j + 1];
         }
         priorities[priorities.length - 1] = temp;
         if (location === 0) location = priorities.length - 1;
         else location = location - 1;
      }
   }
}
