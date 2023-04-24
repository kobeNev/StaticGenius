import markdown
import yaml
from yaml.loader import SafeLoader
import json

def MarkdownToHTML(markdown):
    tempHtml = markdown.markdown(markdown)
    return tempHtml

def YamlToDict(yamlText):
    data = yaml.safe_load(yamlText.replace("---", ""))
    return data

def ParseToHTML(markdownFile):
    with open(markdownFile, 'r') as f:
        tempMd= f.read()

    split = tempMd.rfind("---") + 3
    partMarkdown = tempMd[split+1:]
    return MarkdownToHTML(partMarkdown)

def GetYamlData(markdownFile):
    with open(markdownFile, 'r') as f:
        tempMd= f.read()
    split = tempMd.rfind("---") + 3
    partYaml = tempMd[:split]
    return YamlToDict(partYaml)

def JSONToDict(JSON):
    dict = {}
    try:
        with open(JSON) as f:
            dict = json.load(f)
    except:
        dict = dict
    return dict