import os.path
from datetime import datetime
from pathlib import Path
import markdown
from starlette.templating import Jinja2Templates

def get_abs_path():
    current_file = Path(__file__)
    current_file_dir = current_file.parent
    project_root = current_file_dir.parent
    project_root_absolute = project_root.resolve()

    return project_root_absolute


def open_file(filename):
    if not Path(filename).is_absolute():
        filepath = os.path.join(get_abs_path(), f"pages/{filename}")
    else:
        filepath = filename

    with open(filepath, "r", encoding="utf-8") as input:
        page = input.read()

    return page


def markdown_to_html(filename: str):
    text = open_file(filename)

    return markdown.markdown(text)


def get_blog_posts():
    posts = {format_title(post): markdown.markdown(open_file(f"blog/{post}")) for post in
             os.listdir(os.path.join(get_abs_path(), "pages/blog"))
             if
             post.endswith(".md")}

    return posts


def format_title(title: str):
    date_and_title = datetime.strftime(datetime.strptime(title.split("_")[0], "%Y%M%d"), "%d/%M/%Y") + "|" + title

    return date_and_title


def get_template(templates: Jinja2Templates, template_name: str):
    return templates.get_template(template_name)
