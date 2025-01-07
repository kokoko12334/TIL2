class Node:
    def __init__(self, data, key):
        self.data = data  # 데이터 값
        self.key = key  # 고유 키
        self.pre = None  # 이전 노드
        self.next = None  # 다음 노드

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity  # 캐시의 최대 용량
        self.tail = Node('tail', -1)  # 더미 테일 노드
        self.head = Node('head', -1)  # 더미 헤드 노드
        self.head.next = self.tail  # 헤드와 테일 연결
        self.tail.pre = self.head  # 헤드와 테일 연결
        self.hash = {}  # 캐시를 저장할 해시맵
        self.count = 0  # 현재 캐시의 아이템 수

    def get(self, key: int) -> int:
        """캐시에서 값을 가져옵니다. 없으면 -1을 반환"""
        if key not in self.hash:
            return -1  # 캐시에 존재하지 않으면 -1 반환
        
        node = self.hash[key]  # 해당 키에 해당하는 노드
        # 해당 노드를 최근 사용된 노드로 이동
        self._remove_node(node)  # 기존 위치에서 제거
        self._add_node_to_head(node)  # 헤드로 이동시킴
        return node.data  # 데이터 반환

    def put(self, key: int, value: int) -> None:
        """캐시에 데이터를 추가합니다. 만약 캐시가 꽉 차면 가장 오래된 데이터를 삭제"""
        if key in self.hash:
            node = self.hash[key]  # 이미 존재하는 키라면
            node.data = value  # 값을 업데이트
            self._remove_node(node)  # 기존 위치에서 제거
            self._add_node_to_head(node)  # 헤드로 이동시킴
        else:
            if self.count >= self.cap:  # 캐시가 꽉 찼다면
                self._remove_lru()  # 가장 오래된 노드를 제거
            
            node = Node(value, key)  # 새 노드를 생성
            self._add_node_to_head(node)  # 새 노드를 헤드에 추가
            self.hash[key] = node  # 해시맵에 저장
            self.count += 1  # 캐시 아이템 수 증가

    def _remove_node(self, node: Node) -> None:
        """주어진 노드를 리스트에서 제거하는 함수"""
        prev_node = node.pre
        next_node = node.next
        prev_node.next = next_node
        next_node.pre = prev_node

    def _add_node_to_head(self, node: Node) -> None:
        """노드를 헤드 위치에 추가하는 함수"""
        next_node = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = next_node
        next_node.pre = node

    def _remove_lru(self) -> None:
        """가장 오래된 노드를 제거하는 함수 (tail 바로 앞의 노드)"""
        lru_node = self.tail.pre  # 가장 오래된 노드
        self._remove_node(lru_node)  # 노드를 리스트에서 제거
        del self.hash[lru_node.key]  # 해시맵에서 삭제
        self.count -= 1  # 캐시 아이템 수 감소
