"""professor.py: create a table named professors in the marist database"""
from db.server import db

class Professor(db.Model):
    __tablename__ = 'Professors'
    ProfessorID = db.Column(db.Integer,primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    email = db.Column(db.String(100))

    # create relationship with courses table. assoc table name = ProfessorCourse
    course = db.relationship('Courses', secondary = 'ProfessorCourse', back_populates = 'Professors')
    def __init__(self, first_name, last_name, email):
        # remove pass and then initialize attributes
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        # add text to the f-string
        return f"""
        ProfessorID: {self.ProfessorID}
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Email: {self.email}

        """
    
    def __repr__(self):
        return self.__repr__()