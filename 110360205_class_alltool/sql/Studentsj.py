import sys
sys.path.append('../sql')
from DBConnection import DBConnection


class Studentsj:
    def insert_a_student(self,stu_id, subject,score):
        command = "INSERT INTO subject_info (stu_id,subject,score) VALUES  ('{}','{}','{}');".format(stu_id,subject,score)
            
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
    def select_print(self, subject):
        command = "SELECT * FROM subject_info;"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            rows = cursor.fetchall()
        return  [dict(row) for row in rows]
    
    def select_a_student(self, subject):
        command = "SELECT * FROM subject_info WHERE stu_id='{}';".format(subject)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()
        return [[row['subject'] ,row['score']]for row in record_from_db]

    def delete_a_student(self, stu_id):
        command = "DELETE FROM subject_info WHERE stu_id='{}';".format(stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update_a_student(self, stu_id, subject,score):
        command = "UPDATE subject_info SET subject='{}' , score='{}' WHERE stu_id='{}';".format(subject,score, stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def reset(self):
        command = "DELETE FROM subject_info;"
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
             