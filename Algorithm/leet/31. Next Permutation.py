import time
import sys
from io import StringIO

# 입력 데이터를 모킹하기 위해 StringIO 사용
test_data = "a" * 10000000  # 9000개의 'a'로 구성된 문자열 생성

# Mock sys.stdin to simulate the input for testing
sys.stdin = StringIO(test_data)

# Measure input() performance
print("Testing input() performance...")
start_time = time.time()
data = input()
end_time = time.time()
input_time = end_time - start_time
print(f"Time taken with input(): {input_time} seconds")

# Mock sys.stdin again for sys.stdin.readline()
sys.stdin = StringIO(test_data)

# Measure sys.stdin.readline() performance
print("Testing sys.stdin.readline() performance...")
start_time = time.time()
data = sys.stdin.readline()  # 개행 문자 제거 필요
end_time = time.time()
readline_time = end_time - start_time
print(f"Time taken with sys.stdin.readline(): {readline_time} seconds")