package hello.core.discount;

import hello.core.member.Grade;
import hello.core.member.Member;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class RateDiscountTest {

    DiscountPolicy discountPolicy = new RateDiscountPolicy();

    @Test
    void discountTest() {

        Member member = new Member(1L, "memberVIP", Grade.VIP);

        int discounted = discountPolicy.discount(member, 10000);

        assertThat(discounted).isEqualTo(1000);

    }

    @Test
    void discountNotTest() {

        Member member = new Member(1L, "memberVIP", Grade.BASIC);

        int discounted = discountPolicy.discount(member, 10000);

        assertThat(discounted).isEqualTo(0);

    }
}
