package hello.core;

import hello.core.member.MemberRepository;
import hello.core.member.MemberService;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class ComponentTest {
    public static void main(String[] args) {

        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);
        MemberService member = ac.getBean(MemberService.class);
        MemberService member2 = ac.getBean(MemberService.class);

        System.out.println(member);
        System.out.println(member2);


        MemberRepository memberRepository = ac.getBean("MemberRepository", MemberRepository.class);
        MemberRepository memberRepository2 = ac.getBean("MemberRepository2", MemberRepository.class);

        System.out.println(memberRepository);
        System.out.println(memberRepository2);
    }
}
