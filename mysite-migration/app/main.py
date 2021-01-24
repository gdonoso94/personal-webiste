from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .library.helpers import *

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/resume", StaticFiles(directory="static/resume_cv"), name="resume")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    data = open_file("about_me.md")
    return templates.TemplateResponse("about.html", {"request": request, "data": data})


@app.get("/cv", response_class=HTMLResponse)
async def cv(request: Request):
    return templates.TemplateResponse("/cv/me.html", {"request": request})


@app.get("/personal", response_class=HTMLResponse)
async def personal(request: Request):
    return RedirectResponse("https://unamotoyunbambu.wordpress.com/")

@app.get("/professional", response_class=HTMLResponse)
async def professional(request: Request):
    data = {
        "posts": [i[:-3] for i in get_blog_posts()]
    }
    #TODO: render content
    return templates.TemplateResponse("blog.html", {"request": request, "data": data})

@app.get("/blog/{blog_post}", response_class=HTMLResponse)
async def render_post(request: Request, blog_post: str):
    data = open_file(f"blog/{blog_post}.md")
    return templates.TemplateResponse("render_blog.html", {"request": request, "data": data})
