package com.example.loginplatform.domain;

import jakarta.persistence.*;

@Entity
public class Member {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(unique = true)
    private String email;
    private String encryptedPassword;

    @Enumerated(EnumType.STRING)
    private AccountType type;

    public Member(Long id, String email, String encryptedPassword, AccountType type) {
        this.id = id;
        this.email = email;
        this.encryptedPassword = encryptedPassword;
        this.type = type;
    }

    public Long getId() {
        return id;
    }

    public String getEmail() {
        return email;
    }
}
