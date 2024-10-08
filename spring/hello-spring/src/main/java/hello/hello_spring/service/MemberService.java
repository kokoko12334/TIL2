package hello.hello_spring.service;

import hello.hello_spring.controller.MemberController;
import hello.hello_spring.domain.Member;
import hello.hello_spring.repository.MemberRepository;
import hello.hello_spring.repository.MemoryMemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
// 클래스에서 커서 -> 오른족위에 점 3개 -> 테스트생성 하면 junit테스트 자동생성

//@Service
public class MemberService {

    private final MemberRepository memberRepository;

//    @Autowired
    public MemberService(MemberRepository memberRepository){
        this.memberRepository = memberRepository;
        System.out.println("MemberRepository implementation class: " + memberRepository.getClass().getSimpleName());
    }

    public Long join(Member member){
        // alt-ctrl-m -> extracted method
        validateDuplicateMember(member);
        memberRepository.save(member);
        return member.getId();

    }

    private void validateDuplicateMember(Member member) {
        memberRepository.findByName(member.getName())
                .ifPresent(m ->{
                    throw new IllegalStateException("이미 존재함");
                });
    }

    public List<Member> findMembers(){
        return memberRepository.findAll();
    }

    public Optional<Member> findOne(Long memberId){
        return memberRepository.findById(memberId);
    }

}
