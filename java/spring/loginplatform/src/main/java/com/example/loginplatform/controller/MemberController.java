package com.example.loginplatform.controller;

import com.example.loginplatform.domain.Member;
import com.example.loginplatform.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class MemberController {

    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @PostMapping("/api/users/create")
    @ResponseBody
    public ResponseEntity<String> create(@RequestBody Member member) {

        if (!memberService.validateEmail(member)) {
            return ResponseEntity.badRequest().body("이메일 형식 잘못됨");
        }

        if (!memberService.hasEmail(member)) {
            return ResponseEntity.badRequest().body("이미 가입한 이메일이 있습니다.");
        }

        memberService.join(member);
        return ResponseEntity.ok("가입 성공");
    }
}
