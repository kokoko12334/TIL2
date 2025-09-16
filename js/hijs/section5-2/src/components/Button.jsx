//매개변수에 children을 쓰면 안에 있는 자식태그를 의미 무조건 children이라고 해야 함.
const Button = (props) => {
    console.log(props);
    return (
        <button onClick = {(e) => {
            //e는 합성 이벤트객체로 서로 다른 브라우저에서 통합된 핸들링 가능
            console.log("클릭");
        }}style={{color: props.color}}>
            {props.text} 버튼 클릭 {props.color}
            {props.children} 
        </button>
        
    )
};
//react 19버전 이상부터 default기능이 사라져서 props대신에 구조분해 할당방식인 {text, color="black"}이런식으로 작성해야 함.


export default Button;