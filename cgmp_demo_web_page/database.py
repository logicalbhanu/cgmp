import sqlite3
class Database:
    table = 'expenses'
    def __init__(self,name="mydb.sqlite3"):
        self.con = sqlite3.connect(name)
        print('connected')
    def run(self,querry):  #function to execute the querry
        try:
            self.con.execute(querry)
            self.con.commit() #saves the changes
            
            return True
        except Exception as e:
            print('error')
            print(e)
            return False
        

    def create_table(self): # Capital letter in querry is to follow the convention and its not mandatory
        querry = """ 
            CREATE TABLE expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT,
                price DOUBLE

            )

        """
        return self.run(querry)

    def add(self,item,price):
        query = f"""
            INSERT INTO {self.table} VALUES(
                null, '{item}', {price}
            )
        """
        return self.run(query)
    def delete(self,id):
        querry = f""" 
            DELETE FROM {self.table} WHERE id = {id}
        """
        return self.run(querry)
    def view(self):
        query = f"SELECT * FROM {self.table}"
        try:
            result = self.con.execute(query)
            return result.fetchall()
        except Exception as e:
            print('error')
            print(e)

