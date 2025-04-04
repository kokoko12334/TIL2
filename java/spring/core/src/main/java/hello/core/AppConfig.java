package hello.core;

import hello.core.discount.DiscountPolicy;
import hello.core.discount.FixDiscountPolicy;
import hello.core.discount.RateDiscountPolicy;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import hello.core.member.MemoryMemberRepository;
import hello.core.order.OrderService;
import hello.core.order.OrderServiceImpl;
import org.springframework.context.annotation.Bean;

//@Configuration
public class AppConfig {

    @Bean
    public DiscountPolicy ratecountPolicy() {
        return new RateDiscountPolicy();
    }

    @Bean
    public DiscountPolicy fixcountPolicy() {
        return new FixDiscountPolicy();
    }

    @Bean
    public MemoryMemberRepository MemberRepository() {
        return new MemoryMemberRepository();
    }

    @Bean
    public MemoryMemberRepository MemberRepository2() {
        return MemberRepository();
    }

    @Bean
    public MemberService memberService() {
        return new MemberServiceImpl(MemberRepository());
    }

    @Bean
    public OrderService orderService() {
        return new OrderServiceImpl(MemberRepository(), ratecountPolicy());
    }
}
