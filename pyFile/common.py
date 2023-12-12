# -*- 公共方法 -*-
import tkinter as tk
from tkinter import filedialog,messagebox as msgbox

import os
import sys
import pandas as pd
import datetime

json_text = pd.DataFrame()  # 配置json文件数据
base_path = ''  # 基础路径
save_path = ''  # 保存路径


class MyClass:
    def __init__(self):
        global json_text
        global base_path
        global save_path

        base_path = os.path.dirname(os.path.realpath(sys.argv[0]))

        try:
            json_text = pd.read_json(os.path.join(base_path, 'config.json'))
        except Exception:
            # 如果文件不存在，则提供自定义的错误提示
            show_message('配置文件不存在 或 格式不正确', 0)
            sys.exit()

        save_path = [os.path.join(base_path, '保税好件', 'Excel', datetime.date.today().strftime('%Y-%m-%d')),
                     os.path.join(base_path, '保税好件', 'Html', datetime.date.today().strftime('%Y-%m-%d'))]
        create_folder_if_not_exists(save_path)


"""
   检查文件夹是否存在，如果不存在则创建。
   :param folder_path_list: 文件夹路径
   """


def create_folder_if_not_exists(folder_path_lest):
    for folder_path in folder_path_lest:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


"""
    打开文件资源管理器，选择文件后，返回文件路径
    :param  prompt_message: 提示信息
"""


def select_excel_file(prompt_message):
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[(prompt_message, '*.xlsx')])

    if file_path:
        return os.path.abspath(file_path)
    else:
        show_message('没有选择文件', 0)
        return None


def show_message(message, x):
    if x == 0:
        msgbox.showerror('错误提示', message)
    else:
        msgbox.showinfo('温馨提示', message)
