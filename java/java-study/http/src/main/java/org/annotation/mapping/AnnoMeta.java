package org.annotation.mapping;

import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME) //실행 시점에도 이 어노테이션 생존
@Target({ElementType.METHOD, ElementType.TYPE}) // 이 어노테이션은 메소드 ,클래스(타입)에 적용가능
@Documented // 자바 docs 만들 때 같이 붙어서 작성가능
public @interface AnnoMeta {
}
