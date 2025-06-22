from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import random
import math

from questionDB import rnq1, rnq2, rnq3, rnq4, rnq5, rnq6, pq1, pq2, pq3, pq4, pq5, leq1, leq2, leq3, leq4, leq5

app = FastAPI()

total_rnq1 = len(rnq1)
total_rnq2 = len(rnq2)
total_rnq3 = len(rnq3)
total_rnq4 = len(rnq4)
total_rnq5 = len(rnq5)
total_rnq6 = len(rnq6)

total_pq1 = len(pq1)
total_pq2 = len(pq2)
total_pq3 = len(pq3)
total_pq4 = len(pq4)
total_pq5 = len(pq5)

total_leq1 = len(leq1)
total_leq2 = len(leq2)
total_leq3 = len(leq3)
total_leq4 = len(leq4)
total_leq5 = len(leq5)


templates = Jinja2Templates(directory="templates")

@app.get("/test1/", response_class=HTMLResponse,)
def index(request: Request):
    loc_rnq1 = math.floor(random.randint(0, total_rnq1-1))
    loc_rnq2 = math.floor(random.randint(0, total_rnq2-1))
    loc_rnq3 = math.floor(random.randint(0, total_rnq3-1))
    loc_rnq4 = math.floor(random.randint(0, total_rnq4-1))
    loc_rnq5 = math.floor(random.randint(0, total_rnq5-1))
    loc_rnq6 = math.floor(random.randint(0, total_rnq6-1))

    context_rnqp = {'request': request,'rnq1': rnq1, 'loc_rnq1':loc_rnq1,'rnq2': rnq2, 'loc_rnq2':loc_rnq2,'rnq3': rnq3, 'loc_rnq3':loc_rnq3,'rnq4': rnq4, 'loc_rnq4':loc_rnq4,'rnq5': rnq5, 'loc_rnq5':loc_rnq5,'rnq6': rnq6, 'loc_rnq6':loc_rnq6}
    return  templates.TemplateResponse("test_rn.html", context_rnqp) 

@app.get("/test2/", response_class=HTMLResponse,)
def index(request: Request):
    loc_pq1 = math.floor(random.randint(0, total_pq1-1))
    loc_pq2 = math.floor(random.randint(0, total_pq2-1))
    loc_pq3 = math.floor(random.randint(0, total_pq3-1))
    loc_pq4 = math.floor(random.randint(0, total_pq4-1))
    loc_pq5 = math.floor(random.randint(0, total_pq5-1))

    context_pqp = {'request': request,'pq1': pq1, 'loc_pq1':loc_pq1,'pq2': pq2, 'loc_pq2':loc_pq2,'pq3': pq3, 'loc_pq3':loc_pq3,'pq4': pq4, 'loc_pq4':loc_pq4,'pq5': pq5, 'loc_pq5':loc_pq5}
    return  templates.TemplateResponse("test_p.html", context_pqp) 

@app.get("/test3/", response_class=HTMLResponse,)
def index(request: Request):
    loc_leq1 = math.floor(random.randint(0, total_leq1-1))
    loc_leq2 = math.floor(random.randint(0, total_leq2-1))
    loc_leq3 = math.floor(random.randint(0, total_leq3-1))
    loc_leq4 = math.floor(random.randint(0, total_leq4-1))
    loc_leq5 = math.floor(random.randint(0, total_leq5-1))

    context_leqp = {'request': request,'leq1': leq1, 'loc_leq1':loc_leq1,'leq2': leq2, 'loc_leq2':loc_leq2,'leq3': leq3, 'loc_leq3':loc_leq3,'leq4': leq4, 'loc_leq4':loc_leq4,'leq5': leq5, 'loc_leq5':loc_leq5}
    return  templates.TemplateResponse("test_le.html", context_leqp) 
    

@app.get("/index/", response_class=HTMLResponse)
def index(request: Request):   
    context = {'request': request}
    return templates.TemplateResponse("chapters.html", context)
