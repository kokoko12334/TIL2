// 1. 배열 순회
let arr = [66,66, 3];

for (let i=0; i<arr.length; i++) {
    console.log(arr[i]);
}

for(let item of arr) {
    console.log(item);
}

// 2. 객체 순회
let person = {
    name: "kmp",
    age: 11,
    phone: 111,
}

let keys = Object.keys(person);

for (let key of keys) {
    console.log(key, person[key]);
}

let values = Object.values(person);
console.log(values);

for (let key in person) {
    console.log(key);
}
// let .. in은 객체에서만 쓸수 있고 배열에다 쓰면 index가 반환됨
for (let item in arr) {
    console.log(item);
}