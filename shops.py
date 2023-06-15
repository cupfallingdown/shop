import tkinter as tk
from db import db


class Main1:
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.title('三乐购物商城')
        self.root.geometry('800x500')

        self.product = tk.StringVar()
        self.price = tk.StringVar()
        self.status = tk.StringVar()

        # 商品列表
        self.create_products_list()
        # 添加商品
        tk.Label(self.root, text='商品').pack(side=tk.LEFT,pady=10)
        tk.Entry(self.root,textvariable=self.product).pack(side=tk.LEFT)

        #价格
        tk.Label(self.root, text='价格').pack(side=tk.LEFT)
        tk.Entry(self.root,textvariable=self.price).pack(side=tk.LEFT)

        #刷新商品按钮
        tk.Button(self.root, text="刷新商品", command=self.show_product_list).pack(side=tk.RIGHT,padx=20)

        #添加商品按钮
        tk.Button(self.root, text='添加',command=self.add_to_products).pack(side=tk.LEFT ,padx=20)
        tk.Label(self.root, textvariable=self.status).pack(side=tk.LEFT)

        #删除商品按钮
        tk.Button(self.root, text='删除',command=self.dle_to_products).pack(side=tk.LEFT ,padx=20)

    def create_products_list(self):
        self.products_list = tk.Listbox(self.root, width=100)
        for product in db.products:
            self.products_list.insert(tk.END, product['name'] + " 价格：" + str(product['price']))
        self.products_list.pack(fill=tk.BOTH, expand=True)

    # 添加商品
    def add_to_products(self):
        product = self.product.get()
        price = self.price.get()
        db.add_product(product, price)
        self.status.set('添加成功')

    # 刷新商品列表
    def show_product_list(self):
        # 删除旧的
        for item in db.products:
            self.products_list.delete(tk.END)

        db.read_products()
        for item in db.products:
            self.products_list.insert(tk.END, item["name"] + " 价格：" + str(item["price"]))
        self.products_list.pack(fill=tk.BOTH, expand=True)

    #删除商品
    def dle_to_products(self):
        selection = self.products_list.curselection()
        if selection:
            index = selection[0]
            db.dle(index)
            self.products_list.delete(index)
            db.save_product()




if __name__ == '__main__':
    root = tk.Tk()
    Main1(root)
    root.mainloop()
