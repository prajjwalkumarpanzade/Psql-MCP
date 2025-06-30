from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from query import query_and_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ask")
def ask(question: str = Query(...)):
    answer = query_and_answer(question)
    return {"answer": answer}
