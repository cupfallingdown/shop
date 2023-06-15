import tkinter as tk
from about import AboutFrame, IndexFrame,  CartFrame




class Main:
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.title('三乐购物商城')
        self.root.geometry('800x500')
        self.menu()

    def menu(self):
        self.about_frame = AboutFrame(self.root)
        self.cart_frame = CartFrame(self.root)
        self.index_frame = IndexFrame(self.root)


        menubar = tk.Menu(self.root)
        menubar.add_command(label='首页', command=self.show_index)
        menubar.add_command(label='购物车', command=self.show_cart)
        menubar.add_command(label='关于', command=self.show_about)

        self.root['menu'] = menubar

    def show_about(self):
        self.about_frame.pack()
        self.index_frame.pack_forget()
        self.cart_frame.pack_forget()

    def show_cart(self):
        self.cart_frame.pack()
        self.about_frame.pack_forget()
        self.index_frame.pack_forget()


    def show_index(self):
        self.index_frame.pack()
        self.about_frame.pack_forget()
        self.cart_frame.pack_forget()


if __name__ == '__main__':
    root = tk.Tk()
    Main(root)
    root.mainloop()
