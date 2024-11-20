package com.order.demo;

import org.springframework.util.Assert;

public record AddProductRequest(String name, int price, DiscountPolicy discountPolicy) {
    public AddProductRequest {
        Assert.hasText(name, "상풍명은 필수");
        Assert.isTrue(price > 0, "상품가격은 0보다 커야");
        Assert.notNull(discountPolicy, "할인 정책은 필수");
    }
}
