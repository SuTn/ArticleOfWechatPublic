import tkinter as tk
import time
import tkinter.messagebox
import pyttsx3
import random

window = tk.Tk()
# 设置主窗口大小
window.geometry('500x300')
# 设置主窗口标题
window.title('万圣节快乐！')



# 按键内容设计
longtext = ["不给糖，就别想走！","竟然不给糖，\n你个大坏蛋！","不给糖就搞怪,哼！"]
# print(longtext[random.randint(0,len(longtext)-1)])
def closeWindow():
    engine = pyttsx3.init()
    texts=longtext[random.randint(0,len(longtext)-1)]
    engine.say(texts)
    engine.runAndWait()
    tkinter.messagebox.showerror(title="警告",message =texts )
    
    return

window.protocol('WM_DELETE_WINDOW', closeWindow)
# 点击给糖的操作
def Yes():
    yes = tk.Toplevel(window)
    yes.geometry('300x200')
    yes.title("")

    text1 = "谢谢你，万圣节要开心噢！"

    engine = pyttsx3.init()
    engine.say(text1)
    engine.runAndWait()

    lable = tk.Label(yes,text=text1, font=("Arial", 18))
    btn = tk.Button(yes, text="确定")
    btn.config(command=lambda :closeyes(yes))
    lable.pack()

    yes.protocol('WM_DELETE_WINDOW', closeall)
    btn.pack()

# 点击不给糖的操作
def No():
    no = tk.Toplevel(window)
    no.geometry('300x200')

    text1 = longtext[random.randint(0,len(longtext)-1)]
    #"再考虑考虑呗"

    engine = pyttsx3.init()
    engine.say(text1)
    engine.runAndWait()

    no.title(text1)
    lable = tk.Label(no,text=text1, font=("Arial", 24))
    btn = tk.Button(no, text="确定")
    btn.config(command=lambda :closeno(no))
    lable.pack()
    btn.pack()
# 子窗口关闭操作
def closeall(): 
    window.destroy()

def closeyes(yes):
    window.destroy()
    yes.destroy()

def closeno(no):
    no.destroy()

## 主界面设计
canvas = tk.Canvas(window, width=500,height=300,bd=0, highlightthickness=0)
photo = tk.PhotoImage(file='./timg.gif')
#`image = canvas.create_image(10, 10, anchor='nw', #image=image_file)`里面的参数`10,10`就是图片放入画布的坐标，
canvas.create_image(0, 0,  anchor='nw',image=photo)
canvas.pack()


lable1 = tk.Label(window, text="万圣节快乐，给糖吃吗？",font=("华文行楷",20))
# 设置按钮
btn1 = tk.Button(window, text="给你")
btn2 = tk.Button(window, text="偏偏不给你")
btn1.config(command=Yes)
btn2.config(command=No)

canvas.create_window(250, 50,window=lable1)
canvas.create_window(190, 150, width=100, height=20,window=btn1)
canvas.create_window(300, 150, width=100, height=20,window=btn2)


window.mainloop()