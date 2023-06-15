import json


class MysqlDatabases:
    def __init__(self):
        self.users = json.loads(open('users.json', mode='r', encoding='utf-8').read())
        self.cart = json.loads(open('cart.json', mode='r', encoding='utf-8').read())
        self.products = json.loads(open('products.json', mode='r', encoding='utf-8').read())

    # 检查登录
    def check_login(self, username, password):
        for user in self.users:
            if username == user['username']:
                if password == user['password']:
                    return True, '登陆成功'
                else:
                    return False, '登陆失败,密码错误'
        return False, '登录失败，用户不存在'

    def create_user(self, username, password):
        user = {'username': username, 'password': password}
        self.users.append(user)
        self.save_user()

    def add_product(self, name, price):
        product = {'name': name, 'price': float(price)}
        self.products.append(product)
        self.save_product()
        print(self.products)

    def save_user(self):
        with open('users.json', 'w') as f:
            json.dump(self.users, f)

    def save_product(self):
        with open('products.json', 'w') as f:
            json.dump(self.products, f)

    #将字典转化为列表
    def read_carts(self):
        return self.cart


    def read_products(self):
        return self.products

    def insert(self,product):
        self.cart.append(product)
        #print(self.cart)

    def remove(self,index):
        self.cart.pop(index)
        #print(self.cart)

    def dle(self,index):
        self.products.pop(index)
    def save_cart(self):
        with open('cart.json', 'w') as f:
            json.dump(self.cart,f)
            #print(self.cart)




db = MysqlDatabases()

if __name__ == '__main__':
    print(db.check_login('aa', 'aa'))
    print(db.read_carts())
    print(db.read_products())
