from tkinter import *
from tkinter import ttk
import shutil
import configparser
import os

root = Tk()
root.title('DICOM Image Moves')

class tools():

    def init():
        pass

    def main():
        # frame 
        frame = ttk.Frame(root,padding=10)
        frame.grid()

        driveList = ["D:/","E:/","F:/"]

        v = StringVar()
        cb = ttk.Combobox(
            frame,
            textvariable=v,
            values=driveList,
            width=10    
        )

        # リストボックス
        cb.set(driveList[0])
        cb.bind(
            '<<ComboboxSelected>>',
            lambda e: print('v=%s' % v.get()))
        cb.grid(row=0, column=0)

        # 決定ボタン
        button1 = ttk.Button(
            frame,
            text="ok",
            command=lambda:call_message(v)
        )
        button1.grid(row=0,column=1)

        # プログレスバー
        progress = ttk.Progressbar(frame,value=50)
        progress.grid(row=1,column=0,columnspan=2)

        root.mainloop()

    def call_message(message):
        print('v=%s',message.get())

    def move_directory(path):
        before = 'hoge'
        after  = 'fuga'
        before_size = get_size(before)
        after_size  = get_size(after)
        shutil.copytree(before,after)

    # directory か fileを判断
    def get_size(path='.'):
        if os.path.isfile(path):
            return os.path.getsize(path)
        elif os.path.isdir(path):
            return get_dir_size(path)
        
    # directoryの容量を取得
    def get_dir_size(path='.'):
        total = 0
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += get_dir_size(entry.path)
        return total

t = tools()
tools.main()


