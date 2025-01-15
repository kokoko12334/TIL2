package com.example.loginplatform.service;

import com.example.loginplatform.domain.AccountType;
import com.example.loginplatform.domain.Member;
import com.example.loginplatform.repository.MemberRepository;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.bean.override.mockito.MockitoBean;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.*;

@ExtendWith(SpringExtension.class)
@ContextConfiguration(classes = MemberService.class)
public class MemberServiceTest {

    @Autowired
    MemberService memberService;

    @MockitoBean
    private MemberRepository memberRepository;

    @Test
    void joinTest() {

        //given
        Member member = new Member(1L,"ko", "gnjgnjgnj@naver.com", "DDDD", "010-1234-1234", "Seoul");
        member.setType(AccountType.BASIC);

        //when
        when(memberRepository.save(any(Member.class))).thenReturn(member);
        when(memberRepository.findById(anyLong())).thenReturn(Optional.of(member));
        Long id = memberService.join(member);
        Optional<Member> findMember = memberService.findMemberById(id);

        //then
        if (findMember.isPresent()) {
            assertThat(findMember.get().getId()).isEqualTo(id);
            assertThat(findMember.get().getEmail()).isEqualTo(member.getEmail());
        }
    }
}
