from fastapi import FastAPI
import random
import math

app = FastAPI()

a = "question"
b = "answer"
c=a+"2"
d=b+"2"
questions = [[a,b],[c,d]]

@app.get("/")
def read_root():
    length = len(questions)
    loc = math.floor(random.randint(0, length-1))
    return  questions[loc][0], loc

@app.get("/checkanswer/{question_no}")
def chec_ans(question_no:int):
    return {f"answer is: {questions[question_no-1][1]}"}

@app.post('/')
def show():
    pass

@app.delete('/')
def show():
    pass

@app.put('/')
def show():
    pass