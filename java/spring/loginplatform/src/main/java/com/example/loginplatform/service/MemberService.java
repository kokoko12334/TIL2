package com.example.loginplatform.service;

import com.example.loginplatform.domain.Member;
import com.example.loginplatform.repository.MemberRespository;
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
    private final MemberRespository memberRespository;

    @Autowired
    public MemberService(MemberRespository memberRespository) {
        this.memberRespository = memberRespository;
    }

    public Long join(Member member) {
        Member joinedMember = memberRespository.save(member);
        return joinedMember.getId();
    }

    public boolean hasEmail(Member member) {
        return memberRespository.findByEmail(member.getEmail())
                .isEmpty(); //이메일이 존재하지 않으면 true, 이메일이 존재하면  false
    }

    public boolean validateEmail(Member member) {
        return EMAIL_PATTERN.matcher(member.getEmail())
                .matches();
    }

    public Optional<Member> findOne(Long id) {
        return memberRespository.findById(id);
    }

    public List<Member> findMembers() {
        return memberRespository.findAll();
    }

}
