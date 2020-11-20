import mysql.connector
from sba_api_exam.ext.db import config

class Dao:
    
    def __init__(self):
        self.connector  = mysql.connector.connect(**config)
        self.cursor = self.connector.cursor(dictionary=True)


    def select_items(self):
        cur = self.cursor
        con = self.connector
        rows = []

        try:
            cur.execute('select * from food',)
            rows = cur.fetchall()
            for row in cur:
                print(f'price is : {str(row["price"])}')

            cur.close()
        except:
            print('Exception ...')

        finally:
            if con is not None:
                con.close()
        return rows


print('---2---')
dao = Dao()
dao.select_items()
    