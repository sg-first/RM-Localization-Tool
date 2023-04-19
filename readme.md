RmLocalizationTool
=========
RMMV对话本地化工具链

GenRmScript
------------
### 准备
该脚本会将对话事件加入到一个特定的事件块。然后手动将其复制到想要的事件中。目前的特定事件块是`vox房间`的`(0,0)`位置。如果想要换为其它事件块，需要到json文件中复制该事件块，并替换代码中的`oldCode`变量

该特定事件块建议先加两条对话文本。然后脚本生成的对话事件会加在这两条文本中间

### 生成对话事件
* 找到目前游戏里要生成的一段连续对话。将脚本中的`start`和`end`改为该段对话第一条和最后一条文本对应的数字ID
* 运行脚本，得到修改后的事件块json对象。将该对象覆盖地图json文件中原先的事件块
* 重启RM，进入该特定事件块，查看是否生成正确
* 将事件复制到该在的地方