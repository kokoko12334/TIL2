package org.annotation.mapping;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

// annotation은 주석이라고 보면됨 즉, jvm이 정확한 기능으로 보지는 않음.
// 일반적인 주석과 달리, 컴파일러나 런타임에 해석될 수 있는 메타데이터형태
@Retention(RetentionPolicy.RUNTIME)
public @interface SimpleMapping {
    String value();
}


/***
 * RetentionPolicy -> 어노테이션 생존시간
 * RUNTIME -> 런타임 시점에도 생존
 * SOURCE -> 소스코드에서만 생존
 * CLASS -> 컴파일 후 CLASS 파일까지는 남음 단, 자바 실행 시점에 제거(기본 값)
 */
