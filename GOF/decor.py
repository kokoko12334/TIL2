import functools

# 데코레이터 정의 (functools.wraps 사용)
def my_decorator(func):
    @functools.wraps(func)  # 메타데이터 보존
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

# 데코레이터를 적용한 함수 정의
@my_decorator
def say_hello(name):
    """Returns a greeting message."""
    return f"Hello, {name}"