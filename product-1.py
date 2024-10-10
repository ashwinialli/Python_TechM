class Product:
    data = []
    def add(self,pid,pname, price, category):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.category = category
        temp = []
        for i in (pid,pname,price,category):
            temp.append(i)
        self.data.append(temp)
        print(self.data)
    def update_Name(self,old_name,new_name):
        for i in self.data:
            if i[1]==old_name:
                i[1]=new_name
    def update_Price(self,old_price,new_price):
        for i in self.data:
            for i in self.data:
                if i[2]==old_price:
                    i[1]=new_price
    def update_Category(self,old_category,new_category):
        for i in self.data:
            if self.data[3] == old_category:
                self.data[3] = new_category
    def deleteby_Id(self,id):
        for i in self.data:
            if i[0]==id:
                self.data.remove(i)
    def deleteby_Name(self,name):
        for i in self.data:
            if i[1]==name:
                self.data.remove(i)
    def getProduct_id(self,name):
        for i in self.data:
            if i[1]==name:
                print(self.data[i][0])
    def getDetailsof_all_Products(self):
        for i in self.data:
            print(self.data[i])
    def get_productby_category(self,category):
        for i in self.data:
            if self.data[3]==category:
                print(self.data[i])
if __name__ == '__main__':
    product = Product()
    while True:
        product_count = len(Product.data)
        print("Choose your choice:")
        choice = int(input("""What do you want to do?
            1. Add Product
            2. Update Product
            3. Delete Product
            4. Get id by product name
            5. Get all products
            6. Get Produts by category
            7. Get products between prices
            8. Exit\n""")) 
        if choice not in range(1,8):
            print("Enter valid choice")
        if choice==1:
            id = input("Enter id:")
            name = input("Enter name of the product:")
            price = input("Enter price of the product:")
            cat = input("Enter category:")
            product.add(id,name,price,cat)
        elif choice==2:
            update = int(input("""
                What do you want to update?
                1. Name
                2. Price
                3. Category
                """))
            if update == 1:
                old_name = input("Enter old name:")
                new_name = input("Enter new name:")
                product.update_Name(old_name,new_name)
            elif update == 2:
                old_price = input("Enter old Price")
                new_price = input("Enter new Price:")
                product.update_Price(old_price,new_price)
            elif update==3:
                old_category = input("Enter old Category")
                new_category = input("Enter new Category:")
                product.update_Category(old_category,new_category)
        elif choice==3:
                delete= int(input("""What do u want to delete by
                                   1.id
                                   2.Name
                                   3.Category|n
                                   """))
                if delete == 1:
                    id = input("Enter the product ID:")
                    product.deleteby_Id(id)
                elif delete==2:
                    name = input("Enter name of the product:")
                    product.deleteby_Name(name)
        elif choice==4:
            name = input("Enter the name of the product:")
            product.getProduct_id(name)
        elif choice==5:
            product.getDetailsof_all_Products()
        elif choice==6:
            cat = input("Enter the category of the product:")
            product.get_productby_category()
        elif choice==7:
            start,end = int(input().split())
            product.get_produts_between_prices(start,end)
        elif choice == 8:
            break
        