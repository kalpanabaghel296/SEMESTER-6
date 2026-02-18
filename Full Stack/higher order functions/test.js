const A = [1,5,9,11,55,88];

function abc(x){
 return x>5;
}

// const B = A.filter(abc);
// console.log(B);

// const B = A.map(abc);
// console.log(B);

const B = A.reduce((sum,i)=>{
    return sum+i;
},0); // 0 is teh initialize of sum variable
console.log(B);


// const B = A.map((x)=>{
//     return x+5;
// });
// console.log(B);