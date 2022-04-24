const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(' ').map(BigInt);
let [a, b, c] = input;

const mod = function(b) {
  if (b === BigInt(0)) return BigInt(1);
  if (b === BigInt(1)) return a % c;

  let tmp = mod(b / BigInt(2));
  tmp = (tmp * tmp) % c;
  if (b % BigInt(2) === BigInt(0)) {
    return tmp % c;
  } else {
    return (tmp * a) % c; 
  }
}
console.log(parseInt(mod(b)));
