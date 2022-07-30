// 행렬 테두리 회전하기
const makeMatrix = (rows, columns) => {
   var num = 1;
   var matrix = [];
   for (var i = 0; i < rows; i++) {
      matrix[i] = [];
      for (var j = 0; j < columns; j++) {
         matrix[i][j] = num;
         num = num + 1;
      }
   }
   return matrix;
};

function solution(rows, columns, queries) {
   var answer = [];
   var matrix = makeMatrix(rows, columns);
   var matrix_tmp = makeMatrix(rows, columns);

   queries.map((query) => {
      var scope = [];
      var y = query[0] - 1; // 2
      var x = query[1] - 1; // 2
      var y1 = query[2] - 1; // 5
      var x1 = query[3] - 1; // 4
      // matrix 회전
      for (var i = x + 1; i <= x1; i++) {
         matrix_tmp[y][i] = matrix[y][i - 1];
         scope.push(matrix[y][i - 1]);
      }
      for (var j = y + 1; j <= y1; j++) {
         matrix_tmp[j][x1] = matrix[j - 1][x1];
         scope.push(matrix[j - 1][x1]);
      }
      for (var k = x; k < x1; k++) {
         matrix_tmp[y1][k] = matrix[y1][k + 1];
         scope.push(matrix[y1][k + 1]);
      }
      for (var l = y; l < y1; l++) {
         matrix_tmp[l][x] = matrix[l + 1][x];
         scope.push(matrix[l + 1][x]);
      }
      answer.push(Math.min(...scope));
      // 원본에 복사
      matrix = JSON.parse(JSON.stringify(matrix_tmp)); // 깊은복사
   });
   return answer;
}
