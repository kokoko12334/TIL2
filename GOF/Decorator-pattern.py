from abc import ABC, abstractmethod
#데코레이터 패턴은 기존 객체에 추가적인 책임을 동적으로 부여하는 구조적 패턴
# 원래기능 + 부가기능을 부여
# 1. 기본 컴포넌트 인터페이스
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# 2. 기본 컴포넌트 클래스
class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent operation"

# 3. 데코레이터 베이스 클래스
class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component

    def operation(self):
        return self._component.operation()

# 4. 구체적인 데코레이터 클래스 (로그 기록을 추가)
class LoggingDecorator(Decorator):
    def operation(self):
        # 로그 기록 추가
        log_entry = f"LoggingDecorator: {self._component.operation()}"
        print(f"Log: {log_entry}")
        return log_entry

# 사용 예제
if __name__ == "__main__":
    # 기본 컴포넌트 생성
    component = ConcreteComponent()
    
    # 데코레이터를 통해 기능 확장
    decorated_component = LoggingDecorator(component)
    
    # 확장된 기능 사용
    result = decorated_component.operation()
    print(f"Result: {result}")
