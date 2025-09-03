// 1. if 조건문
let num = 10;

if (num >= 10) {
    console.log("num은 10 이상입니다.");
}


let animal = "dog";
switch (animal){
    case "dog": {
        console.log("dog");
        break; //break안쓰면 조건 일치하는부분부터 쭈욱 출력함.
    }
    case "cat": {
        console.log("cat");
        break;
    }
    case "tiger": {
        console.log("tiger");
        break;
    }
    case "snake": {
        console.log("snake");
        break;
    }
    default: {
        console.log("nonononoo");
    }
}


for (let i=0; i < 10; i++) {
    setTimeout(() => {console.log(i)}, 1000);
    
}