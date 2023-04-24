from toevoegen import toevoegen, delete
from omzetten import JSONToDict
import os
from datetime import date

def AddPostOrPage(type, fileList):
    addFunction = toevoegen if type == "page" else toevoegen
    for file in fileList:
        addFunction(file)

def DelPostOrPage(type, fileList):
    delFunction = delete if type == "page" else delete
    for file in fileList:
        delFunction(file)

def FillPrefab(templateName, number=1, type="post"):
    if os.path.isfile(f"templates/prefabs/{templateName}.md"):
        for i in range(number):
            data = FillDataDict(JSONToDict(f"templates/prefabs/{templateName}.JSON"))
            while True:
                fileName = input("what do you want this file to be called? ")
                if " " in fileName or "/" in fileName or fileName in JSONToDict(f"{type}s/{type}s.JSON"):
                    print("please pick a valid name")
                else:
                    break
    else:
        print(f"template {templateName} not found")

def FillDataDict(emptyDict):
    filledDict = emptyDict.copy()
    for item in emptyDict:
        if item == "date":
            filledDict[item] = str(date.today())
        elif isinstance(emptyDict[item], list):
            if len(emptyDict[item]) == 0:
                print(f"time to add a list of {item} [answer 'stop' to stop]")
                filledDict[item] = FillDataList(emptyDict[item])
            else:
                print(f"next, i want you to add {len(emptyDict[item])} {item}:")
                filledDict[item] = FillDataList(emptyDict[item])
        elif not isinstance(emptyDict[item], str):
            try:
                answer = input(f"give me a {item}: ")
                filledDict[item] = type(emptyDict[item])(answer)
            except ValueError:
                print(f"cannot parse string to {type(emptyDict[item])}")
        else:
            filledDict[item] = input(f"give me a {item}: ")
    return filledDict

def FillDataList(emptyList):
    filledList = emptyList.copy()
    for i in range(len(emptyList)):
        if isinstance(emptyList[i], dict):
            filledList[i] = FillDataDict(emptyList[i])
        elif not isinstance(emptyList[i], str):
            try:
                answer = input(f"{i+1}: ")
                filledList[i] = type(emptyList[i])(answer)
            except:
                print(f"cannot parse string to {type(emptyList[i])}")
        else:
            filledList[i] = input(f"{i+1}: ")
    return filledList
