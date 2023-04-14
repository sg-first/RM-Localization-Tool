import pandas as pd

df = pd.read_excel('Localization.xls', 'Localization')
wrapNum = {'cn':44, 'en': 89}

start = 0
end = 951
col = 'cn'

def addQuotes(s):
    return '\"'+str(s)+'\"'

def changeNameStyle(s:str):
    if s.find('：\\n') != -1:
        s = '\\\\n<' + s
        s = s.replace('：\\n', '>')
    return s, s.find('>')

def autoWrap(s:str, nameEndSub:int):
    name = s[:nameEndSub+1]  # 把名字截下来
    s = s[nameEndSub+1:]
    s = s.replace('\\C', '\\\\C')
    lines = s.split('\\n\\!')
    for i in range(len(lines)):
        line = lines[i]
        finishedSub = wrapNum[col]
        while len(line) > finishedSub:
            line = line[:finishedSub] + '\\n' + line[finishedSub:]
            finishedSub += 1+wrapNum[col]
        lines[i] = line

    s = lines[0]
    for i in range(1, len(lines)):
        s += '\\n\\\\!' + lines[i]
    return name + s

for index, row in df.iterrows():
    if index >= start and index <= end:
        if row[col] != '' and (not pd.isnull(row[col])) and (not pd.isna(row[col])):
            row[col], nameEndSub = changeNameStyle(row[col])
            row[col] = autoWrap(row[col], nameEndSub)
            print(addQuotes(row['key']) + ':' + addQuotes(row[col]) + ',')