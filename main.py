from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
# import uvicorn


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


app = FastAPI()


@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {1, 2}}


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is create with title as {blog.title}'}


# if __name__ == "__main__":
#     uvicorn.run(app, host='127.0.0.1', port=8000)
