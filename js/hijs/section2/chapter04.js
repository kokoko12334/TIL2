// 1. Spread 연산자 ...배열, 객체로 풀어쓰는거

let arr1 = [1, 2, 3];
let arr2 = [4, ...arr1, 5 ,6];
console.log(arr2);

let obj = {
    a: 1,
    b: 2,
}

let obj2 = {
    ...obj,
    4:3,
};
console.log(obj2);

function funA(a, b, c) {
    console.log(a, b, c);
}

funA(...arr1);

// 2. Rest 매개변수 인풋에서 ...연산 배열에 저장함
// 단, rest뒤에 매개변수 추가는 못하고 rest변수는 마지막에 적어야 함.
function funcB(one, ...rest) {
    console.log(one);
    console.log(rest);
}

funcB("dd", ...arr1);





