// 오픈채팅방
function solution(record) {
   var answer = [];
   var uid = {};
   record.map((record) => {
      if (record.split(" ")[0] !== "Leave") {
         uid[record.split(" ")[1]] = record.split(" ")[2];
      }
   });
   record.map((record) => {
      var log = record.split(" ")[0];
      var userId = record.split(" ")[1];
      if (log === "Enter") {
         answer.push(`${uid[userId]}님이 들어왔습니다.`);
      } else if (log === "Leave") {
         answer.push(`${uid[userId]}님이 나갔습니다.`);
      }
   });
   return answer;
}
