import pandas as pd
import fileUtils
from PIL import Image

df = pd.read_excel('Localization.xls', 'Localization')

start = 0
end = 3

addPointSub = 1
pageSub = 0

def getShowDialogueTemplate():
    return {"code":101,"indent":0,"parameters":["",0,0,2]}

def getDialogueTemplate(content):
    return {"code":401,"indent":0,"parameters":['{'+str(content)+'}']}

picPath = 'D:\\Localization Demo\\img\\pictures\\'
allPicWithPath = fileUtils.GetFiles(picPath, ".png")
allPicSize = {}
allPic = []
for i in allPicWithPath:
    img = Image.open(i)
    picName = i.split('\\')[-1]
    picName = picName.replace('.png', '')
    picName = picName.lower()
    allPicSize[picName] = img.size
    allPic.append(picName)

def getShowPicTemplate(picName, x, y):
    picX, picY = allPicSize[picName]
    return {"code":231,"indent":0,"parameters":[10, picName, 0, 0, x - picX, y - picY,100,100,255,0]}

def getHidePicTemplate():
    return {"code":235, "indent":0, "parameters":[10]}

def keyToPicName(key:str):
    if not isinstance(key, str):
        return None
    key = key.lower()
    if key.find('（') != -1:
        endSub = key.find('）')
        picName = key[:endSub]
        return picName
    else:
        endSub = 0
        while not key[endSub].isdigit():
            endSub += 1
        picName = key[:endSub]
        # 检查图片是否存在
        if picName in allPic:
            return picName
        else:
            return None

newCode = []
for index, row in df.iterrows():
    if index >= start and index <= end:
        key = row['key']
        if key != '' and (not pd.isnull(key)) and (not pd.isna(key)):
            picName = keyToPicName(key)
            if not (picName is None):
                newCode.append(getShowPicTemplate(picName, 1280, 540))
            newCode.append(getShowDialogueTemplate())
            newCode.append(getDialogueTemplate(key))
            if not (picName is None):
                newCode.append(getHidePicTemplate())

oldCode = '{"id":10,"name":"测试块","note":"","pages":[{"conditions":{"actorId":1,"actorValid":false,"itemId":1,"itemValid":false,"selfSwitchCh":"A","selfSwitchValid":false,"switch1Id":1,"switch1Valid":false,"switch2Id":1,"switch2Valid":false,"variableId":1,"variableValid":false,"variableValue":0},"directionFix":false,"image":{"characterIndex":0,"characterName":"","direction":2,"pattern":0,"tileId":0},"list":[{"code":101,"indent":0,"parameters":["",0,0,2]},{"code":401,"indent":0,"parameters":["啊啊"]},{"code":101,"indent":0,"parameters":["",0,0,2]},{"code":401,"indent":0,"parameters":["哦哦"]},{"code":0,"indent":0,"parameters":[]}],"moveFrequency":3,"moveRoute":{"list":[{"code":0,"parameters":[]}],"repeat":true,"skippable":false,"wait":false},"moveSpeed":3,"moveType":0,"priorityType":0,"stepAnime":false,"through":false,"trigger":0,"walkAnime":true}],"x":0,"y":0}'
import json
oldCodeObj = json.loads(oldCode)
oldList = oldCodeObj['pages'][pageSub]['list']
oldList1 = oldList[:addPointSub+1]
oldList2 = oldList[addPointSub+1:]
newList = oldList1 + newCode + oldList2
oldCodeObj['pages'][pageSub]['list'] = newList
print(json.dumps(oldCodeObj, ensure_ascii=False))