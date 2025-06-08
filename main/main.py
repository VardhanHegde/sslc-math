from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import random
import math

from questionDB import rnq1, rnq2, rnq3, rnq4, rnq5, rnq6

app = FastAPI()

total_rnq1 = len(rnq1)
total_rnq2 = len(rnq2)
total_rnq3 = len(rnq3)
total_rnq4 = len(rnq4)
total_rnq5 = len(rnq5)
total_rnq6 = len(rnq6)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/test/", response_class=HTMLResponse,)
def index(request: Request):
    loc_rnq1 = math.floor(random.randint(0, total_rnq1-1))
    loc_rnq2 = math.floor(random.randint(0, total_rnq2-1))
    loc_rnq3 = math.floor(random.randint(0, total_rnq3-1))
    loc_rnq4 = math.floor(random.randint(0, total_rnq4-1))
    loc_rnq5 = math.floor(random.randint(0, total_rnq5-1))
    loc_rnq6 = math.floor(random.randint(0, total_rnq6-1))
    context_rnqp = {'request': request,'rnq1': rnq1, 'loc_rnq1':loc_rnq1,'rnq2': rnq2, 'loc_rnq2':loc_rnq2,'rnq3': rnq3, 'loc_rnq3':loc_rnq3,'rnq4': rnq4, 'loc_rnq4':loc_rnq4,'rnq5': rnq5, 'loc_rnq5':loc_rnq5,'rnq6': rnq6, 'loc_rnq6':loc_rnq6}
    return  templates.TemplateResponse("test_rn.html", context_rnqp) 
    

@app.get("/index/", response_class=HTMLResponse)
def index(request: Request):   
    context = {'request': request}
    return templates.TemplateResponse("chapters.html", context)
