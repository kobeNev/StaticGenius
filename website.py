from omzetten import JSONToDict
from jinja2 import Environment, FileSystemLoader

def UpdateListBrowser(folder, content, template, contentHeader=""):
    data = JSONToDict(f"{folder}/{content}.JSON")
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template(template)

    if (contentHeader == ""):
        contentHeader = content
        
    with open(f"{folder}/{content}.html", mode="w", encoding="utf-8") as message:
        message.write(template.render(
            data = data.values(),
            header = contentHeader,
            title = contentHeader
            )) 

def Initialize():
    types = {"links": [{"name":"pages", "folder": "pages"}, {"name":"posts", "folder": "posts"}]}
    
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("home.html")
    
    with open("_site/home.html", mode="w", encoding="utf-8") as home:
        home.write(template.render(
            title = "home"
            ))

    for type in types["links"]:
        UpdateListBrowser(type["folder"], type["name"], f'{type["name"]}_template.html')


