const fs = require("fs")
let input = fs.readFileSync(0).toString().split("\n")
a= Number(input[0])
b= Number(input[1])

console.log(`${a*b}`)