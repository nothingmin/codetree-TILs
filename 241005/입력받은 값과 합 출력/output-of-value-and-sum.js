const fs = require("fs")
let a,b = fs.readFileSync(0).toString().split(" ")
a= Number(a)
b= Number(b)

print(`${a} ${b} ${a+b}`)