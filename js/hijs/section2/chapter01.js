// 1. Falsy한 값 -> false로 판단하는 값들

let f1 = undefined;
let f2 = null;
let f3 = 0;
let f4 = -0;
let f5 = NaN;
let f6 = "";
let f7 = 0n; // bigInteger

// 2. Truthy한 값 -> 위의 7개를 제외한 모든거

let t1 = [];
let t2 = {};
let t3 = () => {};

if(t1) {
    console.log("[]는 True");
}

if(t2) {
    console.log("{}는 True");
}

if(t3) {
    console.log("화살표 함수는 True");
}