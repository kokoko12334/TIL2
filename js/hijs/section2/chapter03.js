// 구조분해 할당
let arr = [1, 2, 3];

let [one, two, three, four = 4] = arr; // 이렇게 한번에 하는 것을 구조분해 할당
//이때 four는 범위를 초과해서 기본값 지정 가능
console.log(one, two, three, four);


let person = {
    name: "dlwjdg",
    age: 26,
    hobby: "운동",
}
let {name, age, hobby} = person;
console.log(name, age, hobby);


// 객체 구조 분해 할당을 이용해서 함수의 매개변수를 받는 방법
const func = ({name, age, hobby, extra}) => {
    console.log(name, age, hobby, extra);
};

func(person);//객체로 넘겨야 함.

const func1 = ([a, b, c]) => {
    console.log(a, b, c);
}

func1([1,2,3]);


