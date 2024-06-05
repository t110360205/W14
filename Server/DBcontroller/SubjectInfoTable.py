from DBcontroller.DBConnection import DBConnection

class SubjectInfoTable:
    def insert_a_student(self, index, subject, score):
        command = "INSERT INTO subject_info (stu_id, subject, score) VALUES  ({}, '{}', {});".format(index, subject, score)
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def select_a_student(self, index):
        command = "SELECT * FROM subject_info WHERE stu_id='{}';".format(index)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return dict((row["subject"], row["score"]) for row in record_from_db)

    def delete_a_student(self, stu_id):
        command = "DELETE FROM subject_info WHERE stu_id='{}';".format(stu_id)
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update_a_student(self, score, index, subject):
        command = "UPDATE subject_info SET score={} WHERE stu_id={} AND subject='{}';".format(score, index, subject)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
       