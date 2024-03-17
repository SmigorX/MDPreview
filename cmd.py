import argparse
import os


class Cmd:
    def __init__(self):
        self.argument_parser = argparse.ArgumentParser(description="MD preview",
                                                       formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.argument_parser.add_argument("-f", "--file", help="File to preview")
        self.argument_parser.add_argument("-t", "--terminal", help="Render in terminal", action="store_true")
        self.argument_parser.add_argument("-w", "--web", help="Render in web browser", action="store_true")
        self.argument_parser.usage = "mdprev.py [-h for help]"
        self.parameters = self.argument_parser.parse_args()

    def validate_arguments(self):
        self.check_help()
        self.check_file_exists()
        return self.argument_parser.parse_args()

    def check_file_exists(self):
        if self.argument_parser.parse_args().file is not None:
            if not os.path.isfile(self.argument_parser.parse_args().file):
                print("File not found")
        if self.argument_parser.parse_args().file is None:
            print("No file specified")

    def check_help(self):
        if 'help' in self.parameters or len(os.sys.argv) == 1:
            self.argument_parser.print_help()
            exit()
