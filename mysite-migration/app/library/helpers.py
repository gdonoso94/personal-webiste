import os.path
import markdown


def open_file(filename):
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input:
        page = input.read()

    html = markdown.markdown(page)

    data = {
        "page": html
    }

    return data

def get_blog_posts():
    return os.listdir("app/pages/blog")
