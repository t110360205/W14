from DBConnection import DBConnection


class StudentInfoTable:
    def insert_a_student(self, name):
        command = "INSERT INTO student_info (name) VALUES  ('{}');".format(name)
            
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
    def insert_a_subject(self, student_id, subject ,score):
        command = "INSERT INTO subject_info (stu_id, subject , score) VALUES  ('{}', '{}', '{}');".format(student_id ,subject ,score )
            
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()  

    def select_a_student(self, name):
        command = "SELECT * FROM student_info WHERE name='{}';".format(name)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['stu_id'] for row in record_from_db]
    
    def select_stu_id_column(self):
        command = "SELECT stu_id , name FROM student_info;"

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [(row['stu_id'], row['name']) for row in record_from_db]
    
    def select_stu_name_column(self, stu_id):
        command = "SELECT * FROM student_info WHERE stu_id='{}';".format(stu_id)


        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [ row['name'] for row in record_from_db]

    def select_subject_column(self):
        command = "SELECT stu_id , subject , score FROM subject_info;"

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [(row['stu_id'], row['subject'],row['score'] ) for row in record_from_db]

    def select_a_subject(self, name):
        command = "SELECT * FROM subject_info WHERE name='{}';".format(name)

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
    def delete_a_subject(self, stu_id):
        command = "DELETE FROM subject_info WHERE stu_id='{}';".format(stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update_a_subject(self, score, stu_id, subject ):
        command = "UPDATE subject_info SET score='{}' WHERE  stu_id='{}' AND subject='{}';".format(score, stu_id, subject)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
       