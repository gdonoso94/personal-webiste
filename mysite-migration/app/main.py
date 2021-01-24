from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .library.helpers import *

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/resume", StaticFiles(directory="static/resume_cv"), name="resume")
app.mount("/home", StaticFiles(directory="static/home"), name="home")
app.mount("/blog", StaticFiles(directory="static/blog"), name="blog")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    data = {
        "data": markdown_to_html("about_me.md")
    }
    return templates.TemplateResponse("about.html", {"request": request, "data": data})


@app.get("/cv", response_class=HTMLResponse)
async def cv(request: Request):
    return templates.TemplateResponse("/cv/me.html", {"request": request})


@app.get("/personal", response_class=HTMLResponse)
async def personal():
    return RedirectResponse("https://unamotoyunbambu.wordpress.com/")


@app.get("/professional", response_class=HTMLResponse)
async def professional(request: Request):
    return templates.TemplateResponse("home_blog.html", {"request": request, "data": get_blog_posts()})


@app.get("/blog_post/{blog_post}", response_class=HTMLResponse)
async def render_post(request: Request, blog_post: str):
    data = {
        "page":  markdown_to_html(f"blog/{blog_post}.md")
    }
    return templates.TemplateResponse("render_blog.html", {"request": request, "data": data})
