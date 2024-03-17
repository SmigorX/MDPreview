from fastapi import FastAPI
from cmd import Cmd
import os
import markdown
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
cmd = Cmd()

directory = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=directory)


def html_to_ansi(text):
    styles = {
        "h1": "\033[1m\033[4m",  # Bold and underline
        "h2": "\033[1m",  # Bold
        "h3": "\033[4m",  # Underline
        "ul": "",  # Removes
        "li": "○ ",  # Starts list elements with ○
        "p": "",  # Removes
        "b": "\033[1m",  # Bold
        "u": "\033[4m",  # Underline
        "i": "\033[3m",  # Italic (not widely supported)
        "reset": "\033[0m"  # Reset all attributes
    }

    for tag, code in styles.items():
        text = text.replace(f"<{tag}>", code).replace(
            f"</{tag}>", styles["reset"])

    return text


def get_file_path(file):
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, file)
    return file_path


def get_file(file_path):
    try:
        with open(file_path, "r") as f:
            file_content = f.read()
        return file_content
    except FileNotFoundError:
        return "File not found"


@app.get("/")
async def web_render(file: str):
    file = get_file(file)
    print(directory)
    file = markdown.markdown(file)

    html_response = HTMLResponse(content=file)
    html_response.headers["Cache-Control"] = "no-cache"

    return html_response
