from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()

template = Jinja2Templates(directory='templates')



@app.get('/')
async def homepage(request: Request):
    return template.TemplateResponse('dashboard.html', {
        'request': request
    })


