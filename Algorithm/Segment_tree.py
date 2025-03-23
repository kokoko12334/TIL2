class SegmentTree:
    def __init__(self, data, func, default):
        """
        :param data: 원본 배열 (리스트)
        :param func: 두 값을 합칠 함수 (예: 덧셈, min, max 등)
        :param default: 구간 연산에 대한 항등원 (예: 합의 경우 0, 최소값의 경우 무한대)
        """
        self.n = len(data)
        self.func = func
        self.default = default

        # 세그먼트 트리의 배열은 2*n 크기로 구성 (리프는 인덱스 n부터 시작)
        self.tree = [default] * (2 * self.n)
        
        # 리프 노드 채우기
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        
        # 내부 노드 채우기 (리프부터 올라가며)
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])
    
    def update(self, index, value):
        """
        :param index: data의 index (0-based)
        :param value: 업데이트할 새로운 값
        """
        # 리프 노드 위치 계산
        index += self.n
        self.tree[index] = value
        
        # 부모 노드를 갱신 (상위 노드로 올라가며)
        while index > 1:
            index //= 2
            self.tree[index] = self.func(self.tree[2 * index], self.tree[2 * index + 1])
    
    def query(self, left, right):
        """
        구간 [left, right) (right는 포함하지 않음)에 대한 결과를 반환합니다.
        :param left: 구간 시작 index (포함)
        :param right: 구간 끝 index (미포함)
        :return: 지정 구간에 대해 func를 적용한 결과
        """
        result = self.default
        # 리프 노드 기준의 인덱스
        left += self.n
        right += self.n
        
        while left < right:
            # 만약 left가 홀수이면, 해당 노드를 결과에 반영하고 오른쪽으로 이동
            if left % 2:
                result = self.func(result, self.tree[left])
                left += 1
            # right가 홀수라면, 오른쪽 노드가 구간에 포함되므로 왼쪽 노드로 이동 후 반영
            if right % 2:
                right -= 1
                result = self.func(result, self.tree[right])
            left //= 2
            right //= 2
        
        return result

# 사용 예제
if __name__ == '__main__':
    
    data = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(data, lambda a, b: a + b, 0)
    
    # 구간 [1, 5) (즉, 인덱스 1~4)의 합을 구함
    print("Query [1, 5):", seg_tree.query(1, 5))  # 출력: 3 + 5 + 7 + 9 = 24
    
    # 인덱스 3의 값을 10으로 업데이트
    seg_tree.update(3, 10)
    
    # 업데이트 후 구간 [1, 5)의 합을 구함
    print("Query [1, 5) after update:", seg_tree.query(1, 5))  # 출력: 3 + 5 + 10 + 9 = 27
