package hello.core.discount;

import hello.core.member.Grade;
import hello.core.member.Member;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class FixDiscountTest {

    DiscountPolicy discountPolicy = new FixDiscountPolicy();

    @Test
    void discountTest() {
        //given
        Member member = new Member(1L, "member1", Grade.VIP);
        int price = 5000;

        //when
        int discounted = discountPolicy.discount(member, price);

        //then
        assertThat(discounted).isEqualTo(1000);
    }
}
