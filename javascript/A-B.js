// const fs = require("fs");
// const inputData = fs.readFileSync(0, "utf8").toString().split(" ");

// const A = parseInt(inputData[0]);
// const B = parseInt(inputData[1]);

// console.log(A + B);

// let fs = require("fs");
// let input = fs.readFileSync(0, "utf8").toString().split(" ");

// let num = Number(input);

// for (let i = 1; i <= num; i++) {
//   console.log(i);
// }

// 백준에선 경로를 "/dev/stdin" 이렇게 지정해주어야 한다.
(v = require("fs").readFileSync("/dev/stdin")), console.log(v[0] - v[2] - 96);
