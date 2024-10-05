package hello.hello_spring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {

    @GetMapping("hello")
    public String Hello(Model model){
        model.addAttribute("data", "kmp");
        return "hello";

    }

    @GetMapping("hellow-mvc")
    public String helloMvc(@RequestParam("name") String name, Model model){
        model.addAttribute("name", name);
        return "hello2";
    }
    
    @GetMapping("hello-string")
    @ResponseBody // view 참고 안하고 그냥 바로 문자열
    public String helloString(@RequestParam("name") String name){
        return "hello" + name;
    }

    @GetMapping("hello-api")
    @ResponseBody // getName에서 get뒤에 것을 기준으로 json 키값설정 문자면 그냥 문자 근데 객체이면 json수정
    public Hello helloAPi(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setName(name); // getName에서 get뒤에 것을 기준으로 json 키값설정
        return hello;

    }

    static class Hello {
        private String name;
        private String kmp;

        public String getName() {
            return name;
        }

        public String getKmp() {
            return kmp;
        }

        public void setName(String name){
            this.name = name;
        }

    }

}
