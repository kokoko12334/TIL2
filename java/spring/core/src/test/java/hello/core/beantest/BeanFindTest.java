package hello.core.beantest;

import hello.core.member.MemberRepository;
import hello.core.member.MemoryMemberRepository;
import org.junit.jupiter.api.Test;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

public class BeanFindTest {

     AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(TempBeanConfig.class);

    @Test
    void findBean() {
//        MemberRepository bean = ac.getBean(MemberRepository.class); // 클래스가 두개 인데 이름으로 특정해서 지정안하면 에러
        MemberRepository bean2 = ac.getBean("memberRepository1", MemberRepository.class);
    }


    @Configuration
    static class TempBeanConfig {
        @Bean
        public MemberRepository memberRepository1() {
            return new MemoryMemberRepository();
        }

        @Bean
        public MemberRepository memberRepository2() {
            return new MemoryMemberRepository();
        }
    }
}
