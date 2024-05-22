import io
import sys
#改变标准输出的默认编码
sys.stdout= io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

import tkinter as tk
import tkinter.filedialog

# 创建并隐藏主窗口
tk.Tk().withdraw()

dirPaths = tkinter.filedialog.askdirectory()

if(len(dirPaths) == 0):
  print('None')
else:
  print(dirPaths)