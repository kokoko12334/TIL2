package hello.hello_spring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {


    // 인덱스에서 가장먼저 우선순위가 / 가 있으면 index.html은 무시되고 여기를 우선순위로 함.
    @GetMapping("/")
    public String hone(){
        return "home";
    }
}
