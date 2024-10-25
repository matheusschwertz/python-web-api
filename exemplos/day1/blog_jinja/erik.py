from jinja2 import Environment, FileSystemLoader

class Erik:
    def __init__(self, template_folder="templates"):
        self.url_map = []
        self.template_folder = template_folder
        self.env = Environment(loader=FileSystemLoader(template_folder))