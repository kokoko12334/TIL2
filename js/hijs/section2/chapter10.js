// 1. Date
let date1 = new Date();
console.log(date1);

let date2 = new Date("1111-01-18"); //특정날짜지정가능
console.log(date2);

let date3 = new Date("2025/01/18/10:10:10"); //년월일은 /.- 가능 시간은 :로구분
let date4 = new Date(1996, 1, 15, 3, 33, 33);
console.log(date3);
console.log(date4);

// 2. 타임스탬프: 특정시간이 1970.01.01 00시 00분 00초(UTC)로 부터 ms가 지났는지 의미하는 숫자값
let ts1 = date1.getTime();
console.log(ts1);

// 타입스탬프를 이용하여 Date객체 생성가능
let date5 = new Date(ts1);
console.log(date5);

// 3. 시간 요소 추출
let year = date1.getFullYear();
let month = date1.getMonth() + 1; // month는 js에서 0부터 시작함
let date = date1.getDate();

let hour = date1.getHours();
let minute = date1.getMinutes();
let secondes = date1.getSeconds();

console.log(year, month, date, hour, minute, secondes);

//4. 시간 수정하기
date1.setFullYear(2023);
date1.setMonth(3); // 3월로 수정하는 거임 나머지도 setter를 이용
console.log(date1);


//5. 여러 포멧으로 출력하기
console.log(date1.toDateString()); // 년월일만
console.log(date1.toTimeString()); // 시분초만

console.log(Intl.DateTimeFormat().resolvedOptions().locale); //기본 로케일 확인
console.log(date1.toLocaleString()); // 인자가 없으면 위의 기본값으로 맞게 출력
console.log(date1.toLocaleString("bn")); //인자로 특정국가에 맞게 출력가능
console.log(date1.toLocaleString("ja")); //인자로 특정국가에 맞게 출력가능

//https://stackoverflow.com/questions/52549577/javascript-get-the-complete-list-of-locales-supported-by-the-browser

