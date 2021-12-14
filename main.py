from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 利用post请求来创建一个博客


@app.get('/blog')
def index(sublime=10, unpublished: bool = True, sort: Optional[str] = None):
    if unpublished:
        return {'data': f'show {sublime} unpublished  bolg list'}
    else:
        return {'data': f'show {sublime} unpublish  bolg list'}

# 利用post请求来创建一个博客
# post请求需要发送一个请求体,发送请求体的时候需要创建一个类,这个类继承基础类,也即是BaseModel


class Blog(BaseModel):
    # 在类中定义请求体的参数名和参数类型
    title: str
    body: str
    unpublished: Optional[bool]
# 在这个函数中传入之前创建的Blog类
# blog: Blog 表示传入的类型是Blog,blog表示传入的参数名,这个参数名可以随便起,request也可以


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'you have created {blog.title} blog'}
