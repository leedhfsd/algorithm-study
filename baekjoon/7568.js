const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');

const count = parseInt(input.shift());
const result = [];
for (let i = 0; i < count; i++) {
  let weight, height, place = 1;
  [weight, height] = input[i].split(' ').map(Number);
  for (let j = 0; j < count; j++) {
    if(i === j) continue;
    let nextWeight, nextHeight;
    [nextWeight, nextHeight] = input[j].split(' ').map(Number);

    if (weight < nextWeight && height < nextHeight) {
      place++;
    }
  }
  result.push(place);
}

console.log(result.join(' '));
