import './App.css'
import Button from './components/Button';
import Footer from './components/Footer';
import Header from './components/Header';
import Main from './components/Main';

//화살표 함수
const Header2 = () => {
  return (
    <header>
      <h1>Header2</h1>
    </header>
  )
};

function App() {
  const buttonProps = {
    text: "메일",
    color: "blue",
    a: "a",
    b: "b"
  }
  return (
    <>
    <Button text={"메일"} color={"red"}/>
    <Button text={"카페"} color={"blue"}/>
    <Button text={"블로그"} />
    <Button {...buttonProps} />
    <Button text={"블로그"}>
      <div>자식 요소</div>
    </Button>
    </>
  )
}

export default App