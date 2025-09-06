
//5가지 배열 변형

// 1.filter => 콜백조건을 만족하는 요소를 배열로 반환
let arr1 = [
    {name: "이전환", hobby: "운동"},
    {name: "이수이", hobby: "운"},
    {name: "이전히", hobby: "아가"},
]

const newArr1 = arr1.filter((item) => {
        if (item.hobby === "운동") {
            return true;
        }
    }
)
console.log(newArr1);

//2.map: 배열의 모든요소를 순회하면서 각각 콜백함수를 시행하고난 결과를 배열로 반환

let arr2 = [100, 1000, 10000];

const mapArr = arr2.map((item) => {
    return item * 2;
})
console.log(mapArr);

//3. sort(사전순 정렬)
let arr3 = ["b", "a", "c"];
arr3.sort();
console.log(arr3); // "a", "b", "c"


let arr4 = [10, 5, 3];
arr4.sort();
console.log(arr4); //[10, 3, 5]인데 이유는 사전순 정렬이기때문에
// -> 모두 문자열로 변경이후에 "10"과 "3을" 비교하면 10의 맨앞이 "1"을 먼저 비교해서 3이 뒤에옴

//따라서 콜백으로 비교하는 것을 설정해야 함(오름차순)
arr4.sort((a, b) => {
    if(a > b) {
        // b가 앞에 와라
        return 1;
    } else if (a < b) {
        // b가 뒤에 가라
        return -1;
    } else {
        return 0;
    }
    }
)
console.log(arr4);

// 4. toSorted: 정렬하고 새로운 배열 반환 얘도 사전순임
let arr5 = ["c", "b", "a"];
const sorted = arr5.toSorted();
console.log(sorted);

// 5. join
let arr6 = ["hi", "hello", "my", "name"];

console.log(arr6.join(" ")); // 기본값은 ","임