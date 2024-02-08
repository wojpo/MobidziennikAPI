from fastapi import FastAPI
from routes.lessonPlan import lesson_plan
from routes.lastMessage import last_message

app = FastAPI()


@app.get("/lessonPlan")
async def root():
    return await lesson_plan()


@app.get("/lastMessage")
async def root():
    return await last_message()
