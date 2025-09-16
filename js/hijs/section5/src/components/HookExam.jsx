
// hook이라는 것은 원래 리액트의 use~의 기능들은 class로 작성해서 써야함.
// 하지만 이후에 함수단위로도 쓸수 있게 한것이 react hook이고
// 지금까지 useState, useRef등등을 쓴 것도 hook임. 이때 나만의 커스텀hook도 제작가능

// react hook은 반드시 리액트 컴포넌트, 커스텀 훅에서 작성
// 조건문, 반복문안에서 쓸 수 없음.
import { useState } from "react";


// 함수이름에 앞에 use~ 접두사를 쓰면 커스텀 훅작성 가능
// 폴더 hooks안에서 정의하는 것이 일반적임.
function useInput() {
    const [input, setInput] = useState("");

    const onChange = (e) => {
        setInput(e.target.value);
    }

    return [input, onChange];
}

const HookExam = () => {
    const [input, onChange] = useInput();

    return <div>
        HookExam
        <input value={input} onChange={onChange}/>
        </div>
};

export default HookExam;