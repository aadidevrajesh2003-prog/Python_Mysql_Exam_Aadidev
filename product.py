import mysql.connector

class ProductManager:
    def __init__(self):
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aadidev@123",
            database="shop_db"
        )
        self.cursor=self.conn.cursor()

    def get(self):
        query="select * from product"
        self.cursor.execute(query)
        records=self.cursor.fetchall()

    def get_object(self,id):
        query="select * from product where id=%s"
        self.cursor.execute(query,(id,))
        return self.cursor.fetchone()

    def post(self,**kwargs):
        query=""""insert into product(name,category,price,quantity,manufacturer)
              values(%s,%s,%s,%s,%s)"""

        values=[
            ("bat","sports",300,1,"Nike"),
            ("football","sports",700,2,"Adidas")
        ]
        self.cursor.execute(query,values)
        self.conn.commit()
        print("Product added successfully")



