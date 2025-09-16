import './App.css'
import { useState } from 'react'

// state 변화, props, 부모컴포넌트가 리렌더링 되면 즉 count -> APP 리렌더링 그러면 Bulb도 리런데링 됨
const Bulb = ({light}) => {
  console.log(light);
  return (
  <div>{light === "ON" ? <h1 style={{backgroundColor: "orange"}}>ON</h1> : <h1>OFF</h1>}</div>
  );
};


// state 변화, props, 부모컴포넌트가 리렌더링 되면 
// 즉 count -> APP 리렌더링 그러면 Bulb도 리런데링 됨
// 따라서 부모컴포넌트를 감싼 다른것으로 하고 여기에 따로 두는 것이 나음.
const Counter = () => {
  const [state2, setState] = useState(0);
  return (
    <>
    <h1>{state2}</h1>
    <button onClick={() => {
      setState(state2 + 1); //setState를 하면 App컴포넌트를 다시 렌더링 함. 이를 리렌더링이라고 함. 왜냐하면 APP에 useState에 state2가 있으니까
    }}>클릭</button>
    </>
  )
}



function App() {
  
  const state1 = useState(0);//초기값, 함수(setter, 상태변화 함수)가 담긴 배열을 리턴함.
  console.log(state1);

  const [state2, setState] = useState(0);
  console.log(state2);
  
  const [light, setLight] = useState("OFF");

  return (
    <>
    <div>
      {/* <h1>{light}</h1> */}
      <Bulb light={light}/>
      <button onClick={() => {
        setLight(light === "ON" ? "OFF" : "ON");
      }}>
        전구끄기/켜기
      </button>
    </div>
    {/* <h1>{state2}</h1>
    <button onClick={() => {
      setState(state2 + 1); //setState를 하면 App컴포넌트를 다시 렌더링 함. 이를 리렌더링이라고 함. 왜냐하면 APP에 useState에 state2가 있으니까
    }}>클릭</button> */}
    <Counter/>
    </>
  )
}

export default App