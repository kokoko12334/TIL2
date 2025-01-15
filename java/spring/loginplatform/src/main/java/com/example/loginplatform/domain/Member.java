package com.example.loginplatform.domain;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
public class Member extends BaseEntity{

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name")
    private String name;

    @Column(name = "email", unique = true)
    private String email;

    @Column(name = "encrypted-password")
    private String encryptedPassword;

    @Column(name = "phone")
    private String phone;

    @Column(name = "address")
    private String address;

    @Enumerated(EnumType.STRING)
    private AccountType type;


    public Member() {}

    public Member(Long id, String name, String email, String encryptedPassword, String phone, String address) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.encryptedPassword = encryptedPassword;
        this.phone = phone;
        this.address = address;
    }
}
