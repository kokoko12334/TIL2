package com.example.loginplatform.controller;

import com.example.loginplatform.domain.AccountType;
import com.example.loginplatform.domain.Member;
import com.example.loginplatform.dto.responseformat.ApiResponse;
import com.example.loginplatform.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/account")
public class AccountController {

    private final MemberService memberService;

    @Autowired
    public AccountController(MemberService memberService) {
        this.memberService = memberService;
    }

    @PostMapping("/register")
    public ApiResponse<Long> register(@RequestBody Member member) {

        member.setType(AccountType.BASIC);
        Long id = memberService.join(member);

        if (id == -1) {
            ApiResponse.error("실패", HttpStatus.BAD_REQUEST);
        }
        return ApiResponse.customSuccess("성공", 1L);
    }

}
