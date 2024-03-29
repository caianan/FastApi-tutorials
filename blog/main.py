from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str


@app.post('/blog')
def blog(request: Blog):
    return {'data': 'You have created a new blog'}
