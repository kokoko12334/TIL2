package com.example.loginplatform.service;

import com.example.loginplatform.domain.Member;
import com.example.loginplatform.repository.MemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;
import java.util.regex.Pattern;

@Service
@Transactional
public class MemberService {

    private static final Pattern EMAIL_PATTERN = Pattern.compile("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");
    private final MemberRepository memberRepository;

    @Autowired
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    public Long join(Member member) {

        if (!validateEmail(member)) {
            return -1L;
        }

        if (!hasEmail(member)) {
            return -1L;
        }

        Member joinedMember = memberRepository.save(member);
        return joinedMember.getId();
    }

    private boolean hasEmail(Member member) {
        return memberRepository.findByEmail(member.getEmail())
                .isEmpty(); //이메일이 존재하지 않으면 true, 이메일이 존재하면  false
    }

    private boolean validateEmail(Member member) {
        return EMAIL_PATTERN.matcher(member.getEmail())
                .matches();
    }

    public Optional<Member> findMemberById(Long id) {
        return memberRepository.findById(id);
    }

    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

}
