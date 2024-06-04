import sys
sys.path.append('../sql')
from DBConnection import DBConnection


class StudentInfoTable:
    def insert_a_student(self,stu_id, name):
        command = "INSERT INTO student_info (stu_id,name) VALUES  ('{}','{}');".format(stu_id,name)    
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
    def den_id(self):
        command = 'SELECT MAX(stu_id) AS max_id FROM student_info;'      
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            rows = cursor.fetchall()
        return  [dict(row) for row in rows]
    def select_print(self):
        command = "SELECT * FROM student_info;"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()
        return [[row['stu_id'],row['name']] for row in record_from_db] 
    
    def select_a_student(self, name):
        command = "SELECT * FROM student_info WHERE name='{}';".format(name)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['stu_id'] for row in record_from_db]

    def delete_a_student(self, stu_id):
        command = "DELETE FROM student_info WHERE stu_id='{}';".format(stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update_a_student(self, stu_id, name):
        command = "UPDATE student_info SET name='{}' WHERE stu_id='{}';".format(name, stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
            
    def reset(self):
        command = "DELETE FROM student_info;"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()    