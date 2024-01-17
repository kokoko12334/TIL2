from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Question
from domain.question import question_schema, question_crud
from starlette import status

router = APIRouter(
    prefix="/api/question",
)

# depends는  contextmanager자동설정이라 이 부분을 지워야함.
@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):

    _question_list = question_crud.get_question_list(db)
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    # with get_db() as db:
    #     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()

    return _question_list

@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question_by_id(db, question_id=question_id)
    return question

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)