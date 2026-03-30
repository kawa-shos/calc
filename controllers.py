from fastapi import FastAPI, Depends, HTTPException  # new
from fastapi.security import HTTPBasic, HTTPBasicCredentials  # new
security = HTTPBasic()



from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED  # new

from calculation import calc_simple
import hashlib  # new
from pydantic import BaseModel

import re  # new 
app = FastAPI(
    title='calc',
    description='slang for calculator',
    version='0.1 beta'
)


# new テンプレート関連の設定 (jinja2)
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env  # Jinja2.Environment : filterやglobalの設定用

class Expression(BaseModel):
    expression: str

@app.post("/calc")
async def calc(expression: Expression):
    print("==========="+expression.expression+"============")
    return eval(expression.expression)

# async def calc_simple(request: Request):
#     if request.method =='GET':
#         return templates.TemplateResponse('calc.html', {'request': request})
#     if request.method == 'POST':
#         data = await request.form()
#         a = data.get('a')
#         b = data.get('b')
#         operator = data.get('operator')

#         error = []

#         calc_result = calc_simple(float(a), float(b), str(operator))

#         return templates.TemplateResponse('calc_results.html', {'request': request, 'calc_result': calc_result})

def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
        