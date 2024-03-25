from cmd import Cmd
import uvicorn
from fastapi.templating import Jinja2Templates
import os
from application import *
import webbrowser
import multiprocessing
import time

cmd = Cmd()

port = 7316


def terminal_render(file_path):
    while True:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        file = get_file(file_path)
        file = markdown.markdown(file)
        file = html_to_ansi(file)
        print(file)


def start_web_server():
    uvicorn.run("application:app", host='localhost', port=port, reload=True)


if __name__ == "__main__":
    cmd.validate_arguments()
    file_path = get_file_path(cmd.parameters.file)

    if cmd.parameters.file is not None:
        if cmd.parameters.terminal:
            terminal_process = multiprocessing.Process(
                target=terminal_render, args=(file_path,))
            terminal_process.start()

        if cmd.parameters.web:
            web_process = multiprocessing.Process(
                target=start_web_server)
            web_process.start()
            time.sleep(1)
            webbrowser.open(f"http://localhost:{port}/?file=" + file_path)

    else:
        print("No file specified.")
