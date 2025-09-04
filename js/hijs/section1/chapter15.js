// 1. 객체 생성

let obj1 = new Object();
let obj2 = {}; // 이것도 객체임 객체리터럴이라고 함


//2. 객체 프로퍼티(객체 속성)
let person = {
    name: "이금기",
    age: 27,
    hobby: "운동",
    extra: () => {console.log("extra")},
    10: 20,
    "like cat": true,
}
console.log(person.extra)
person.extra();
console.log(person["like cat"])
console.log(person["age"])
console.log(person.name);
console.log(person.kmp); // undefined

//3. 새로운 프로퍼티 추가방법
person.gogo = "111";
console.log(person.gogo);


//4. 삭제
delete person.name;
delete person["like cat"];
console.log(person.name); // undefined
console.log(person["like cat"]); // undefined

//5. 조회
let result1 = "name" in person;
console.log(result1);



