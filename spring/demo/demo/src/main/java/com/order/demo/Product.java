package com.order.demo;

public class Product {
    protected final String name;
    protected final int price;
    protected final DiscountPolicy discountPolicy;
    private Long id;

    public Product(String name, int price, DiscountPolicy discountPolicy) {
        this.name = name;
        this.price = price;
        this.discountPolicy = discountPolicy;
    }

    public void assignId(Long aLong) {
        this.id = id;
    }

    public Long getId() {
        return id;
    }
}
