"use strict";


// object 객체 const는 객체안의 내용을 변경가능
const person1 = {
    name: 'kim',
    age: 25,
    phone: "010"
};

console.log(typeof person1);
console.log(person1);

// 접근 방법
console.log(person1.name, person1['name']);



//배열
const array = [true, 3.13, 'hello'];
console.log(typeof array);
console.log(array, array.length);

//접근방법
console.log(array[0], array[1]);

for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
}

for (const item of array) {
    console.log(item);
}
