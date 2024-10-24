from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("email.template.txt")

def addhearts(text):
    return f"<3 {text} <3"

env.filters["addhearts"] = addhearts

data = {
    "name": "Bruno",
    "products": [
        {"name": "iphone", "price": 13000.320},
        {"name": "ferrari", "price": 900000.430},
    ],
    "special_customer": True
}

print(template.render(**data))