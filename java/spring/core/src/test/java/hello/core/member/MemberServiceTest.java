package hello.core.member;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class MemberServiceTest {

    MemberService memberService = new MemberServiceImpl();

    @Test
    void joinTest() {
        //given
        Member member = new Member(1L, "memberA", Grade.VIP);

        //when
        memberService.join(member);
        Member findMember = memberService.findMember(1L);

        //then
        assertThat(findMember.getId()).isEqualTo(1L);
        assertThat(findMember.getName()).isEqualTo("memberA");
        assertThat(findMember.getGrade()).isEqualTo(Grade.VIP);

    }
}
