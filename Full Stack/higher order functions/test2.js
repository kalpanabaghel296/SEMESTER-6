//return all teh titles

const products = require('./products.js');

// const A = products.map((i)=>{
// return i.title;
// });

//console.log(A);

//q-2
// const B = products.map((i)=>{
//     return {id:i.id, title:i.title,category:i.category,price:i.price}
// });
// console.log(B);

//q-3 get the category electrnucs and rating>=4;
//pipelining method
//const C = products.filter((i)=>i.category === 'electronics').filter((j)=>j.rating.rate>=4);
const C = products.filter((i)=>{
   return i.rating.rate>=4 & i.category === 'electronics';
});

console.log(C);