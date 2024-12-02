package hello.core.order;

import hello.core.AppConfig;
import hello.core.member.Grade;
import hello.core.member.Member;

import hello.core.member.MemberService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class OrderServiceTest {

    MemberService memberService;
    OrderService orderService;

    @BeforeEach
    public void setUp() {
        AppConfig appConfig = new AppConfig();
        memberService = appConfig.memberService();
        orderService = appConfig.orderService();
    }

    @Test
    void createOrderTest() {
        //given
        Member member = new Member(1L, "member1", Grade.VIP);
        String itemName = "cola";
        int itemPrice = 1000;

        //when
        memberService.join(member);
        Order order = orderService.createOrder(member.getId(), itemName, itemPrice);

        //then
        assertThat(order.getMemberId()).isEqualTo(1L);
        assertThat(order.getItemName()).isEqualTo(itemName);
        assertThat(order.getItemPrice()).isEqualTo(itemPrice);
        assertThat(order.getDiscount()).isEqualTo(100);

    }
}
