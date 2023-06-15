import tkinter as tk
from db import db



class AboutFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        tk.Label(self, text='关于本作品由tkinter制作').pack()
        tk.Label(self, text='作者：2135  2137').pack()

class IndexFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.status = tk.StringVar()
        self.create_products_list()
        # 添加到购物车按钮
        add_button = tk.Button(self, text="添加到购物车", command=self.add_to_cart)
        add_button.pack(side=tk.BOTTOM, padx=10, pady=10)
        tk.Label(self, textvariable=self.status).pack()

    # 创建商品列表
    def create_products_list(self):
        self.products_list = tk.Listbox(self, width=100)
        for product in db.products:
            self.products_list.insert(tk.END, product['name'] + " 价格：" + str(product['price']))

        self.products_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # 添加到购物车
    def add_to_cart(self):
        selection = self.products_list.curselection()
        if selection:
            selected_product = db.products[selection[0]]
            # 插入
            db.insert(selected_product)
            # 保存到json
            db.save_cart()
            self.status.set('添加成功')



class CartFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.tprice = tk.DoubleVar()
        self.cart_list = tk.Listbox(self, width=100)
        self.show_cart_list()

        # 删除按钮
        remove_button = tk.Button(self, text="从购物车删除", command=self.remove_from_cart)
        remove_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.price_label = tk.Label(self, textvariable=self.tprice)
        self.price_label.pack(side=tk.RIGHT,padx=10, pady=2)

        # 刷新购物车按钮
        refresh_button = tk.Button(self, text="刷新购物车", command=self.show_cart_list).pack(side=tk.LEFT)



    # 创建购物车清单
    def show_cart_list(self):
        # 删除旧的
        for item in db.cart:
            self.cart_list.delete(tk.END)

        db.read_carts()
        for item in db.cart:
            self.cart_list.insert(tk.END, item["name"] + " 价格：" + str(item["price"]))
        self.cart_list.pack(fill=tk.BOTH, expand=True)
        # 总价钱
        total_price = self.get_total_price()
        self.tprice.set("$%.2f" % total_price)

    # 删除
    def remove_from_cart(self):
        selection = self.cart_list.curselection()
        if selection:
            index = selection[0]
            db.remove(index)
            self.cart_list.delete(index)
            db.save_cart()

    # 计算总价
    def get_total_price(self):
        total = 0
        for item in db.cart:
            total += item["price"]
        return total
