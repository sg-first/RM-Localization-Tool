f = open('text.txt', "r", encoding="utf-8", errors="ignore")
allText = f.readlines()
for i in range(len(allText)):
    allText[i] = allText[i].replace('\n', '')
    allText[i] = allText[i].replace('  ', '')
    allText[i] = allText[i].replace('： ', '：')
    allText[i] = allText[i].replace('】 ', '】')

textMap = {}
hashVal = 917

def parseDialogue(t):
    keyEndSub = t.find('：')
    tipSub = t.find('【')  # 【】只在前面出现，需要去掉（不放在key里）
    if tipSub != -1:
        keyEndSub = tipSub

    keyArea = t[:keyEndSub]
    expressionSub = keyArea.find('（')  # （）在前后都有可能，但只有前面的才是表情（需要放在key里）
    if expressionSub != -1:
        nameEndSub = expressionSub
    else:
        nameEndSub = keyEndSub

    name = keyArea[:nameEndSub]

    global hashVal
    key = keyArea + str(hashVal)
    hashVal += 1
    dialogueContent = t.split('：')[1]
    value = name+'：\\n'+dialogueContent
    textMap[key] = value

i = 0
while i < len(allText):
    t = allText[i]

    if '：' in t:
        if t[-1]=='：' or t[-1]=='】': # 把下一行连过来
            i += 1
            t += allText[i]
        parseDialogue(t)
    elif '【' in t:
        pass
    elif t == '':
        pass
    else:
        textMap[str(hashVal)] = t
        hashVal += 1

    i += 1

print('key,cn')
for k,v in textMap.items():
    print(k+','+v)