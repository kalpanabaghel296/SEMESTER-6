const A = [1,3,4,5,8,6,3];
const C = A.forEach((i) => {return i });
console.log("C const printing")
console.log(C);
console.log("....new line.....")
const D = A.map((j)=>{
    return j;
})

console.log("D")
console.log(D);