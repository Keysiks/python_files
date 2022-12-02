import sqlite3
import json


class Quiz:
    def __init__(self):
        self.connection = sqlite3.connect('base_for_quiz23.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS quiz(  
           place_id INT PRIMARY KEY,
           data JSON); 
        """)
        self.connection.commit()

    def add_quiz(self, place_id, name):
        data = {'name': name, 'quizes': []}
        self.cursor.execute("INSERT INTO quiz VALUES(?, ?);", (place_id, json.dumps(data)))
        self.connection.commit()

    def add_question(self, place_id, ques_list):
        new_data = self.cursor.execute(f"SELECT * FROM quiz WHERE place_id={place_id}").fetchone()
        a = json.loads(new_data[1])
        data = {'name': a['name'], 'quizes': ques_list}
        self.cursor.execute(f'DELETE FROM quiz WHERE place_id={place_id}')
        self.cursor.execute("INSERT INTO quiz VALUES(?, ?);", (place_id, json.dumps(data)))
        self.connection.commit()

    def get_quiz(self, place_id):
        new_data = self.cursor.execute(f"SELECT * FROM quiz WHERE place_id={place_id}").fetchone()
        return json.loads(new_data[1])

    def delall(self):
        self.cursor.execute("DELETE FROM quiz")
        self.connection.commit()