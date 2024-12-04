package com.example.loginplatform.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class AccountController {

    @GetMapping("/signup")
    public String signUp() {
        return "signup";
    }
}
