import tkinter as tk
from tkinter import messagebox
from db import db
from PIL import Image, ImageTk
from main import Main
from shops import Main1


class LoginPage:
    def __init__(self, master: tk.Tk):
        self.login = master
        self.login.geometry('800x500')
        self.login.title('登录')

        self.username = tk.StringVar()
        self.password = tk.StringVar()


        self.show_image('store.jpg')


        tk.Label(self.login, text='账户').place(x=350,y=120)
        tk.Entry(self.login, textvariable=self.username).place(x=400,y=120)

        tk.Label(self.login, text='密码').place(x=350,y=170)
        tk.Entry(self.login, textvariable=self.password,show='*').place(x=400,y=170)

        tk.Button(self.login, text='登录', command=self.checklogin).place(x=350,y=220,width=200)
        tk.Button(self.login, text='注册', command=self.register_window).place(x=350,y=270,width=200)
        tk.Button(self.login, text='退出', command=self.login.quit).place(x=350,y=320,width=200)


    def checklogin(self):
        name = self.username.get()
        pwd = self.password.get()
        flag, message = db.check_login(name, pwd)
        if flag:
            print('登陆成功')
            self.login.destroy()  # 销毁当前页面
            for user in db.users:
                if name == user['username']:
                    if user['id'] == 1:
                        root1 = tk.Tk()
                        Main1(root1)  # 打开新的页面
                    else:
                        root = tk.Tk()
                        Main(root)  # 打开新的页面
        else:
            messagebox.showinfo(title='警告', message=message)

    def show_image(self, file):
        photo = ImageTk.PhotoImage(Image.open(file))  # 得到内存里一个图片
        self.label = tk.Label(self.login, image=photo, width=268, height=271)
        self.label.image = photo  # 不能省去
        self.label.place(x=50,y=100)

    def register_window(self):
        def register_user():
            username = username_entry.get()
            password = password_entry.get()
            db.create_user(username, password)
            register_window.destroy()

        register_window = tk.Toplevel(self.login)
        register_window.title("注册")
        register_window.geometry("400x400")

        username_label = tk.Label(register_window, text="用户名")
        username_label.pack(pady=10)
        username_entry = tk.Entry(register_window)
        username_entry.pack(pady=5)

        password_label = tk.Label(register_window, text="密码")
        password_label.pack(pady=10)
        password_entry = tk.Entry(register_window, show='*')
        password_entry.pack(pady=5)

        register_button = tk.Button(register_window, text="注册", width=10, command=register_user)
        register_button.pack(pady=10)


if __name__ == '__main__':
    login = tk.Tk()
    root = tk.Tk()
    LoginPage(login)
    login.mainloop()


