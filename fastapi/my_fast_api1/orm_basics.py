from models import Question,Answer
from datetime import datetime
from database import Session


#session 생성
s = Session()

#데이터 추가하고 commit
q = Question(subject='님들', content='오늘 날씨좀', create_date=datetime.now())
s.add(q)
s.commit()

#q.id를 자동생성하기 위해서 question=q
a = Answer(question=q, content='네이버에 나옵니다.', create_date=datetime.now())
s.add(a)
s.commit()
##조회

lst = s.query(Question).all() # select * from question

lst = s.query(Question).filter(Question.id==1).all() # select * from question where id = 1
lst = s.query(Question).filter(Question.subject.like("%님%")).all()

for q in lst:
    print(q.id)
    print(q.subject)
    print(q.content)


# filter는 여러개 일수 있으므로 반환객체가 List()이고
#get은 하나이므로 Question 객체를 바로 반환한다.
q = s.query(Question).get(1) # select * from question where id == 1
print(q.id)
print(q.subject)
print(q.content)



##수정
q = s.query(Question).get(1)
q.subject = "님들 제목 수정함"
s.commit()


##삭제
q = s.query(Question).get(1)
s.delete(q)
s.commit()


##역참조 설정
#기존에는 a => q로 연결되었는데
#models에서 question = relationship("Question", backref="answers")로 설정 했기 때문에
# q => a로 역참조 설정이 가능하다.


print(a.question)

print(q.answers[0].content) #하나의 질문에 여러개 이므로 List(models.Answer)로 반환


