
// push
let arr1 = [1, 2, 3];
arr1.push(1);
const newLength = arr1.push(1, 2, 3, 4);
console.log(newLength);

// pop
const popedItem = arr1.pop();
console.log(popedItem);


// shift 앞에꺼 pop
const shiftted = arr1.shift();
console.log(shiftted);

//unshift 맨끝에 새로운 요소 추가
arr1.unshift("ddd");

//slice [:] part임 0 ~ end-1만큼 파이썬이랑 같음

let arr2 = [1, 2, 3, 4, 5];
console.log(arr2.slice(1, 3)); 
console.log(arr2.slice(-3));

//concat 배열 합침
arr3 = [1, 2, 3];
arr4 = [4, 5, 6];
console.log(arr4.concat(arr3));

// const start = new Date();
// const cnt = 100000;
// let arr = [];
// for (let i = 0; i < cnt; i++) {
//     arr.unshift(i);
// }

// const end = new Date();

// console.log(`걸린시간: ${end - start}ms`);
// console.log(arr.length);