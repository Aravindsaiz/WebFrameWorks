from fastapi import FastAPI,Response,status
from pydantic import BaseModel
from typing import Optional
from random import randrange
# from fastapi import Body

app = FastAPI()

class CreatePost(BaseModel):
    title : str
    description : Optional[str] = None
    content : str
    published : bool

posts_data = [
    {
      "title": "Top Restuarants near Hyd",
      "description": "post on good restuarants in Hyderabad",
      "content": "the very one place you can visit are 1. Shadab, 2. Paradise, 3. Coalspark, 4. Mandi King",
      "published": True,
      "id": 12
    },
    {
      "title": "Daily Routine of foo_x a boo_x Software Engineet",
      "description": "",
      "content": "He wakes at 5:00, goes for excercise for 2 hrs. light healthy Breakfast, a fun & dedicated 8-9 hrs of work, comeback to home aroound 9, games extra stuff till 10 & sleep. continues",
      "published": True,
      "id": 18
    }
  ]

@app.get("/")
def hello():
    return {"msg":"Welcome!!"}

@app.get("/posts")
def get_posts():
    return {"data":posts_data}

@app.get("/posts/{id}")
def get_post(id:int, response:Response):
    """ returns a single post with id present """
    print(f"checking for post with id {id}")
    for post in posts_data:
        if post["id"] == int(id):
            return post
    
    response.status_code = status.HTTP_404_NOT_FOUND
    
    return "404 not found"


@app.post("/createpost")
def create_post(post_payload : CreatePost):
    data = post_payload.model_dump()
    data["id"] = randrange(0,100000)
    posts_data.append(data)
    print(data["id"], "created")
    return {"successfully added" : data }