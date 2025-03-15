package org.annotation.inherited;

import java.lang.annotation.Inherited;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Inherited //클래스 상속시 자식도 어노테이션 적용 즉, 이노테이션을 쓰는 클래스를 상속하는 클래스도 자동으로 이 어노테이션 사용 단, 인터페이스는 구현한것은 아님.
@Retention(RetentionPolicy.RUNTIME)
public @interface InheritiedAnnotation {
}
