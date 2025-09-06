
// 원시타입과 객체타입 메모리 관점

let p1 = 1;
let p2 = p1; //원시타입은 값을 복사함
p2 = 2; //원래의 1값은 메모리에 그대로 남음


let o1 = {name: "kmp"}; // 참조값을 가리키게 됨.
let o2 = o1 // 참조값을 가리킴 즉, o1과 값은 메모리주소값

 o1.name = "klk";
 console.log(o2); // 얘도 바뀌게 됨.


// 객체간의 비교연산는 참조값 기준임
let obj1 = {name: "gogo"};
let obj2 = obj1;
let obj3 = {...obj1}; // 깊은 복사
let obj4 = {name: "gogo"};
console.log(obj1 == obj2); //true
console.log(obj1 === obj3); //false -> 참조값 다름
console.log(obj1 === obj4); //false
//java의 String비교처럼(equals) 하려면 문자열 변형후(js에서 문자열은 기본타입)
console.log(JSON.stringify(obj1) === JSON.stringify(obj3));