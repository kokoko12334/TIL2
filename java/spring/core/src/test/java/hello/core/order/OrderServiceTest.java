package hello.core.order;

import hello.core.member.Grade;
import hello.core.member.Member;

import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class OrderServiceTest {

    MemberService memberService = new MemberServiceImpl();
    OrderService orderService = new OrderServiceImpl();

    @Test
    void createOrderTest() {
        Member member = new Member(1L, "member1", Grade.VIP);
        memberService.join(member);
        String itemName = "cola";
        int itemPrice = 1000;

        Order order = orderService.createOrder(member.getId(), itemName, itemPrice);

        assertThat(order.getMemberId()).isEqualTo(1L);
        assertThat(order.getItemName()).isEqualTo(itemName);
        assertThat(order.getItemPrice()).isEqualTo(itemPrice);
        assertThat(order.getDiscount()).isEqualTo(1000);

    }
}
