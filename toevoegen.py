from omzetten import ParseToHTML, GetYamlData, JSONToDict
from website import UpdateListBrowser, Initialize
from jinja2 import Environment, FileSystemLoader
import json
import os

def toevoegen(markdownFile):
    try: 
        inhoud = ParseToHTML(markdownFile)
    except:
        print(f"Bestand {markdownFile} niet gevonden.")
    else:
        page_name = markdownFile.replace(".md", "")
        page_list = JSONToDict("pages/pages.JSON")

        if page_name not in page_list:
            page_list[page_name] = ""

        page_data = GetYamlData(markdownFile)
        page_data.update({"fileName": page_name, "content": inhoud, "author": page_data.get("author", "anonymous")})
        page_list[page_name] = page_data

        with open(f"pages/{page_name}.html", mode="w", encoding="utf-8") as f:
            f.write(Environment(loader=FileSystemLoader("templates/")).get_template("page_temp.html").render(
                page_data
            ))

        with open(f"pages/{markdownFile.replace('md', 'JSON')}", "w") as f:
            json.dump(page_data, f, default=str)

        with open("pages/pages.JSON", "w") as f:
            json.dump(page_list, f, default=str)

        print(f"Pagina {page_name} van {markdownFile} is toegevoegd")

        UpdateListBrowser("pages", "pages", "pages_template.html")
        Initialize()


def delete(fileName):
    try:
        os.remove(f"pages/{fileName}.html")
        os.remove(f"pages/{fileName}.JSON")
    except:
        print(f"Bestand {fileName} niet gevonden.")
    else:
        page_list = JSONToDict("pages/pages.JSON")
        del page_list[fileName]

        with open("pages/pages.JSON", "w") as f:
            json.dump(page_list, f, default=str)

        print(f"Page {fileName} was deleted successfully")

        UpdateListBrowser("pages", "pages", "pages_template.html")
        Initialize()

