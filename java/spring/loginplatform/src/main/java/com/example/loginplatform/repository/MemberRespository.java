package com.example.loginplatform.repository;

import com.example.loginplatform.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberRespository {

    Member save(Member member);
    Optional<Member> findById(Long id);
    Optional<Member> findByEmail(String email);
    List<Member> findAll();
}
