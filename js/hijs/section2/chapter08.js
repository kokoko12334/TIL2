
// 1. forEach 배열에서는 인자가 정해짐 -> 인덱스, 아이템, 배열

let arr1 = [10, 100, 1000];

arr1.forEach((item, idx, arr) => {
        console.log(idx, item + 1);
    }
);

// 2. includes
let arr2 = [1, 2, 3];
let isInclude = arr2.includes(3);
console.log(isInclude);

// 3. indexOf: 값에 대한 인덱스 반환
let a = arr2.indexOf(2);
console.log(a);

// 4. findIndex: 콜백함수를 만족하는 거

let arr3 = [2, 3, 3, 4];
arr3.findIndex((item, idx, arr3) => { //일단 forEach처럼 3개 변수 가능
    console.log(item, idx, arr3);
    }
);

// true로 해야함. 그리고 맨 앞에꺼만, 없으면 -1반환
const findIndex = arr3.findIndex((item) => {
        if (item == 3) return true;
    }
);
// 한줄로 할경우
const findIndex2 = arr3.findIndex(item => item == 3);
console.log(findIndex);
console.log(findIndex2);

// 5. find: 인덱스가 아니라 객체 그 자체

let arr5 = [
    {name: "이이"},
    {name: "ㅇㅇㅇ"}
]

const finded = arr5.find((item) => item.name === "이이");
console.log(finded);





