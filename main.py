from fastapi import FastAPI, HTTPException, Request
from database import create_table, insert_url, get_url
from utils import generate_short_code

api = FastAPI()
create_table()


@api.post("/shorten")
async def shorten(request = Request):
    body = await request.json()
    url = body.get("url")
    if not url:
        raise HTTPException(status_code=400, detail ="URL is required in order for this to work")
    
    
    code = generate_short_code(url)
    insert_url(code,url)
    return {"New short Url": f"http://localhost:8000/{code}"}


@api.get("/{code}")
def redirect(code: str):
    original = get_url(code)

    if not original:
        raise HTTPException(status_code=404, detail="Url was not found")
    return {"Original URL": original}