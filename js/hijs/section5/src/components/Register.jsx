import { useState, useRef } from "react";
let a = 0;

const Register = () => {
    console.log("register 렌더링");
    const [input, setInput] = useState({
        name:"dd",
        birth:"",
        country:"",
        bio:""
    });

    // useRef는 리렌더링안함
    // 리렌더링이 되면 내부에서 정한 let은 항상 초기화가 되어서
    // 이를 보완한것이 useRef임. 이떄 위와 같이 a를 전역변수로 할수는 있음.
    // 하지만 전역은 모든곳에서 접근가능해서 나중에 버그같은 것이 발생할 수 있음.
    const refObj = useRef(0);
    console.log(refObj);

    const inputRef = useRef();
    
    const onChange = (e) => {
        a++
        console.log(a);
        setInput({
            ...input,
            [e.target.name]: e.target.value
            
        })
    }

    const onChangeName = (e) => {
        setInput({
            ...input,
            name: e.target.value
        })
    }

    const onChangeBirth = (e) => {
        setInput({
            ...input,
            birth: e.target.value
        })
    }

    const onChangeCountry = (e) => {
        setInput({
            ...input,
            country: e.target.value
        })
    }

    const onSubmit = () => {
        if(input.name === "") {
            console.log(inputRef.current); //ref로 돔요소를변수로써 가능
            inputRef.current.focus();
        }
    }

    return (
        <div>
            register

            <button onClick={() => {
                refObj.current++;
                console.log(refObj.current);
            }}>하이</button>
            <div>
                <input ref={inputRef} name="name" value={input.name} onChange={onChange} placeholder="이름"/>
            </div>
            <div>
                <input name="birth" type="date" onChange={onChange}/>
            </div>

            <div>
                <select name="country" onChange={onChange}>
                    <option value="kr">한국</option>
                    <option>미국</option>
                    <option>일본</option>
                </select>
                {input.country}
            </div>
            
            <div>
                <button onClick={onSubmit}>제출</button>
            </div>
        </div>
        
    );
};


export default Register;

