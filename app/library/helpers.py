import os.path
from datetime import datetime
from pathlib import Path
import markdown


def open_file(filename):
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input:
        page = input.read()

    return page


def markdown_to_html(filename: str):
    text = open_file(filename)

    return markdown.markdown(text)


def get_blog_posts():
    posts = {format_title(post): markdown.markdown(open_file(f"blog/{post}")) for post in os.listdir("app/pages/blog")
             if
             post.endswith(".md")}

    return posts


def format_title(title: str):
    date_and_title = datetime.strftime(datetime.strptime(title.split("_")[0], "%Y%M%d"), "%d/%M/%Y") + "|" + title

    return date_and_title


def get_abs_path():
    current_file = Path(__file__)
    current_file_dir = current_file.parent
    project_root = current_file_dir.parent
    project_root_absolute = project_root.resolve()

    return project_root_absolute
