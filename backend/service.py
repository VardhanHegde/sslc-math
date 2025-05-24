from fastapi import FastAPI, HTTPException
import random
import math

from questionDB import questions

app = FastAPI()

<<<<<<< HEAD
total_questions = len(questions)
=======
a = "question"
b = "answer"
c=a+"2"
d=b+"2"
questions = [[a,b],[c,d]]
>>>>>>> 08fa3a637f0cd7d34a97b6dcabdc6bc0d9164518

@app.get(
    "/questions",
    summary="Gets random Question from database"
)
def read_root():
    loc = math.floor(random.randint(0, total_questions-1))
    return  questions[loc][0], loc

@app.post(
    "/checkanswer/{question_no}",
    summary="Find answer for the Question No. provided"
)
def chec_ans(question_no:int):
    if question_no >= total_questions:
        raise HTTPException(status_code=404, detail="The question no. is out of range")
    return {f"answer is: {questions[question_no-1][1]}"}
