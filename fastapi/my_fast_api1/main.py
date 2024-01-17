from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from domain.question import question_router
from domain.answer import answer_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

templates = Jinja2Templates(directory="templates")

origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)
app.include_router(answer_router.router)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):

    context = {"request": request, "message": "Hello, FastAPI with Jinja2!"}
    
    return templates.TemplateResponse("index.html", {"request": request, **context})


@app.get("/hello")
def hello():
    return {"msg": "hello"}


