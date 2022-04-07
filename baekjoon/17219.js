const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
const [num, count] = input.shift().split(' ').map(Number);
let hash = {};

for (let i = 0; i < num; i++) {
  let [site, password] = input[i].trim().split(' ');
  hash[site] = password;
}
for (let i = num; i < num + count; i++) {
  let site = input[i].trim();
  console.log(hash[site]);
}
