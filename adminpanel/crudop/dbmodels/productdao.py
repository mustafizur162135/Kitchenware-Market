from .dbfactory import DBFactory
from .product import Product

class ProductDAO:

    def getDBCursor(self):
        c=DBFactory.getInstance().getDBCursor()
        return c

    def upload(self, p):
        dbcursor=self.getDBCursor()
        try:
            dbcursor.execute("INSERT INTO product VALUES('',%s,%s,%s,%s,%s)", [p.getName(),p.getPrice(),p.getQnt(),p.getUpldate(),p.getImgpath()])
        except:
            raise Exception('data insertion error')
        finally:
            dbcursor.close()

    def showall(self):
        dbcursor=self.getDBCursor()
        try:
            dbcursor.execute("SELECT * FROM product")
            result=dbcursor.fetchall()
            productlist=[]
            for row in result:
                prod=Product(row[0],row[1],row[2],row[3],row[4],row[5])
                productlist.append(prod)
            return productlist
        except:
            raise Exception('data insertion error')
        finally:
            dbcursor.close()

    def update(self, p):
        dbcursor=self.getDBCursor()
        try:
            dbcursor.execute("UPDATE product SET name=%s, price=%s, qnt=%s, upldate=%s WHERE id=%s", [p.getName(),p.getPrice(),p.getQnt(),p.getUpldate(),p.getId()])
        except:
            raise Exception('data insertion error')
        finally:
            dbcursor.close()

    def findprod(self, id):
        dbcursor=self.getDBCursor()
        try:
            dbcursor.execute("SELECT * FROM product WHERE id=%s",[id])
            item=dbcursor.fetchall()[0]

            prodobj=Product(item[0],item[1],item[2],item[3],item[4],item[5])
            return prodobj
        except:
            raise Exception('data insertion error')
        finally:
            dbcursor.close()

    def delete(self, pid):
        dbcursor=self.getDBCursor()
        try:
            dbcursor.execute("DELETE FROM product WHERE id=%s", [pid])
        except:
            raise Exception('data insertion error')
        finally:
            dbcursor.close()


    def cartall(self):
        dbcursor=self.getDBCursor()
        try:
            dbcursor.execute("SELECT * FROM product")
            result=dbcursor.fetchall()
            productlist=[]
            for row in result:

                prod=Product(row[0],row[1],row[2],row[3],row[4],row[5])
                productlist.append(prod)
            return productlist
        except:
            raise Exception('data insertion error')
        finally:
            dbcursor.close()
