//단락 평가
//개념: And연산자에서 앞에가 False면 뒤를 판단안함.
// or 연산자에서 앞에가 먼저 True면 뒤를 판단안함.

let varA = false;
let varB = true;

console.log(varA && varB);
console.log(varB || varA);

//단락 평가 활용

function printName(person) {
    if (!person) {
        return;
    }
    console.log(person.name);
}

// 단락평가를 이용하여 and연산자에서 false가 앞에오면 undefined값이 name에 전달됨.
function refactoring(person) {
    const name = person && person.name;
    console.log(name || "name없음"); // name이 falsy하면 뒤에거를 선택한다고 생각
}

person = {};
refactoring(person);