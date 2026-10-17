import psycopg
import os
from dotenv import load_dotenv

load_dotenv()
class Database:
    def __init__(self):
        self.connection=psycopg.connect(
            host=os.getenv("your_host"),
            dbname=os.getenv("your_dbname"),
            port=5432,
            password=os.getenv("password"),
            user="postgres"
        )
        self.cursor=self.connection.cursor()

    def get_task(self):
        try:
            self.cursor.execute(
                "select * from tasks" \
                " order by task_id"
            )
            return self.cursor.fetchall()
        except psycopg.Error as e:
            print(e)
            return None
    
    def add_task(self,task):
        try:
            self.cursor.execute(
                "insert into tasks(title)" \
                " values(%s)",(task.title,)
            )
            self.connection.commit()
            return True
        except psycopg.Error as e:
            self.connection.rollback()
            print(e)
            return False

    def update_task(self,task_id,title):
        try:
            self.cursor.execute(
                "update tasks" \
                " set title=%s where task_id=%s returning task_id",(title,task_id)
            )
            row=self.cursor.fetchone()
            if row is None:
                return None
            return True
        except psycopg.Error as e:
            self.connection.rollback()
            print(e)
            return False

    def delete_task(self,task_id):
        try:
            self.cursor.execute(
                "delete from tasks" \
                " where task_id=%s returning task_id",(task_id,)
            )
            row=self.cursor.fetchone()
            if row is None:
                return None
            return True
        except psycopg.Error as e:
            self.connection.rollback()
            print(e)
            return False

    def complete_tasks(self,task_id):
        try:
            self.cursor.execute(
                "update tasks" \
                " set status='complete' where task_id=%s returning task_id",(task_id,)  
            )
            row=self.cursor.fetchone()
            if row is None:
                return None
            return True
        except psycopg.Error as e:
            self.connection.rollback()
            print(e)
            return False
        
            
