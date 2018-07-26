#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from tkinter import *
from PIL import Image, ImageTk
def get_ewm():
    url = 'http://www.wwei.cn/qrcode-wwei_create.html'
    strs = entry.get()
    dat = {}
    html = requests.post(url, data=dat).json()
    img_url = html['png_url']
    with open('123.png', 'wb') as f:
        f.write(requests.get(img_url).content)
    load = Image.open('123.png')
    iml = ImageTk.PhotoImage(load)
    label = Label(tk, image=iml, compound='bottom')
    label.img = iml
    label.grid(row=2, columnspan=6)

if __name__ == '__main__':
    tk = Tk()
    tk.title('二维码生成器')
    tk.geometry('640x600+200+20')
    entry = Entry(tk, font=('微软雅黑'), width=60)
    entry.grid(row=1, column=4)
    str_b = Button(tk, text='生成二维码',command=get_ewm)
    str_b.grid(row=1, column=5)
    tk.mainloop()



