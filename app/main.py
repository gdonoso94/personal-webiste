import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.library.helpers import *

PROJECT_ROOT = get_abs_path().parent
TEMPLATES_ROOT = os.path.join(PROJECT_ROOT, "templates")
PAGES_ROOT = os.path.join(get_abs_path(), "pages")
BLOG_ROOT = os.path.join(PAGES_ROOT, "blog")

app = FastAPI()

templates = Jinja2Templates(directory=os.path.join(TEMPLATES_ROOT))
app.mount("/static", StaticFiles(directory=os.path.join(PROJECT_ROOT, "static")), name="static")
# app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/resume", StaticFiles(directory=os.path.join(PROJECT_ROOT, "static/resume_cv")), name="resume")
# app.mount("/resume", StaticFiles(directory="static/resume_cv"), name="resume")
app.mount("/home", StaticFiles(directory=os.path.join(PROJECT_ROOT, "static/home")), name="home")
# app.mount("/home", StaticFiles(directory="static/home"), name="home")
app.mount("/blog", StaticFiles(directory=os.path.join(PROJECT_ROOT, "static/blog")), name="blog")


# app.mount("/blog", StaticFiles(directory="static/blog"), name="blog")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(get_template(templates, "home.html"), {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    data = {
        "data": markdown_to_html(os.path.join(PAGES_ROOT, "about_me.md"))
    }
    return templates.TemplateResponse(get_template(templates, "about.html"), {"request": request, "data": data})


@app.get("/cv", response_class=HTMLResponse)
async def cv(request: Request):
    return templates.TemplateResponse(get_template(templates, "/cv/me.html"), {"request": request})


@app.get("/personal", response_class=HTMLResponse)
async def personal():
    return RedirectResponse("https://unamotoyunbambu.wordpress.com/")


@app.get("/professional", response_class=HTMLResponse)
async def professional(request: Request):
    return templates.TemplateResponse(get_template(templates, "home_blog.html"),
                                      {"request": request, "data": get_blog_posts()})


@app.get("/blog_post/{blog_post}", response_class=HTMLResponse)
async def render_post(request: Request, blog_post: str):
    data = {
        "page": markdown_to_html(os.path.join(PAGES_ROOT, f"blog/{blog_post}.md"))
    }
    return templates.TemplateResponse(get_template(templates, "render_blog.html"), {"request": request, "data": data})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
