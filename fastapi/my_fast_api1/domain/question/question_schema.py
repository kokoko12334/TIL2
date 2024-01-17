
import datetime
from pydantic import BaseModel, field_validator
from domain.answer.answer_schema import Answer
#만약 없애고 싶은 항목이 있으면 해당 항목만 제거
class Question(BaseModel):
    id: int
    subject: str | None = None  #subject는 필수항목이 아니면 | None = None
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []


class QuestionCreate(BaseModel):
    subject: str
    content: str

    @field_validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v