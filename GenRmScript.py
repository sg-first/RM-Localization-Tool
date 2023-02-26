import pandas as pd

df = pd.read_excel('Localization.xls', 'Localization')

start = 136
end = 141

addPointSub = 1
pageSub = 0

def getShowDialogueTemplate():
    return {"code":101,"indent":0,"parameters":["",0,0,2]}

def getDialogueTemplate(content):
    return {"code":401,"indent":0,"parameters":['{'+str(content)+'}']}

newCode = []
for index, row in df.iterrows():
    if index >= start and index <= end:
        newCode.append(getShowDialogueTemplate())
        newCode.append(getDialogueTemplate(row['key']))

oldCode = '{"id":8,"name":"测试块","note":"","pages":[{"conditions":{"actorId":1,"actorValid":false,"itemId":1,"itemValid":false,"selfSwitchCh":"A","selfSwitchValid":false,"switch1Id":1,"switch1Valid":false,"switch2Id":1,"switch2Valid":false,"variableId":1,"variableValid":false,"variableValue":0},"directionFix":false,"image":{"characterIndex":0,"characterName":"","direction":2,"pattern":0,"tileId":0},"list":[{"code":101,"indent":0,"parameters":["",0,0,2]},{"code":401,"indent":0,"parameters":["啊啊"]},{"code":101,"indent":0,"parameters":["",0,0,2]},{"code":401,"indent":0,"parameters":["哦哦"]},{"code":0,"indent":0,"parameters":[]}],"moveFrequency":3,"moveRoute":{"list":[{"code":0,"parameters":[]}],"repeat":true,"skippable":false,"wait":false},"moveSpeed":3,"moveType":0,"priorityType":0,"stepAnime":false,"through":false,"trigger":0,"walkAnime":true}],"x":2,"y":7}'
import json
oldCodeObj = json.loads(oldCode)
oldList = oldCodeObj['pages'][pageSub]['list']
oldList1 = oldList[:addPointSub+1]
oldList2 = oldList[addPointSub+1:]
newList = oldList1 + newCode + oldList2
oldCodeObj['pages'][pageSub]['list'] = newList
print(json.dumps(oldCodeObj, ensure_ascii=False))