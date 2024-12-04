package com.example.loginplatform.service;

import com.example.loginplatform.domain.AccountType;
import com.example.loginplatform.domain.Member;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest
@Transactional
public class MemberServiceTest {

   @Autowired
   MemberService memberService;

    @Test
    void joinTest() {
        Member member = new Member(1L,"gnjgnjgnj@naver.com", "DDDD", AccountType.BASIC);
        Long id = memberService.join(member);

        Optional<Member> findMember = memberService.findOne(id);

        if (findMember.isPresent()) {
            assertThat(findMember.get().getId()).isEqualTo(id);
            assertThat(findMember.get().getEmail()).isEqualTo(member.getEmail());
        }
    }
}
