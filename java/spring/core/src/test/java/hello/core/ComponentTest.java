package hello.core;

import hello.core.member.MemberServiceImpl;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class ComponentTest {
    public static void main(String[] args) {

        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AutoAppConfig.class);

        MemberServiceImpl member = ac.getBean(MemberServiceImpl.class);
        MemberServiceImpl member2 = ac.getBean(MemberServiceImpl.class);

        System.out.println(member);
        System.out.println(member2);
    }
}
