from fastapi import FastAPI
from models import QueryRequest, QueryResponse
from services import get_answer

app = FastAPI()

@app.post("/ask", response_model=QueryResponse)
def ask(req: QueryRequest):
    results = get_answer(req.question, req.k)
    return QueryResponse(results=results)
