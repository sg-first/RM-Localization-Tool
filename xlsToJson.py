import pandas as pd

df = pd.read_excel('Localization.xls', 'Localization')
wrapNum = 44

start = 0
end = 932
col = 'cn'

def addQuotes(s):
    return '\"'+str(s)+'\"'

def changeNameStyle(s:str):
    if s.find('：\\n') != -1:
        s = '\\\\n<' + s
        s = s.replace('：\\n', '>')
    return s

def autoWrap(s:str):
    s = s.replace('\\C', '\\\\C')
    lines = s.split('\\n\\!')
    for i in range(len(lines)):
        line = lines[i]
        finishedSub = wrapNum
        while len(line) > finishedSub:
            line = line[:finishedSub] + '\\n' + line[finishedSub:]
            finishedSub += 1+wrapNum
        lines[i] = line

    s = lines[0]
    for i in range(1, len(lines)):
        s += '\\\\n\\\\!' + lines[i]
    return s

for index, row in df.iterrows():
    if index >= start and index <= end:
        if row[col] != '' and (not pd.isnull(row[col])) and (not pd.isna(row[col])):
            row[col] = changeNameStyle(row[col])
            row[col] = autoWrap(row[col])
            print(addQuotes(row['key']) + ':' + addQuotes(row[col]) + ',')