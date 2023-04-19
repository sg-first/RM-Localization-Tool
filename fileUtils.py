import os, shutil
import os.path
import codecs
import stat

# 获取目录下后缀为postfix的文件
def GetFiles(path, postfix):
    return [os.path.join(r,file) for r,d,f in os.walk(path) for file in f if file.endswith(postfix)]