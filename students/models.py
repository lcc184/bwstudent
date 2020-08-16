from students import db
class Student(db.Model):

    __tablename__ = "st_student"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    English = db.Column(db.Float(20),nullable=False)
    Python = db.Column(db.Float(20),nullable=False)
    C = db.Column(db.Float(20),nullable=False)
    Grade_num = db.Column(db.Float(20),nullable=False)

    def __str__(self):
        return '{id:%s,name:%s,English:%s,Python:%s,C:%s,Grade_num:%s}' % (self.id, self.name, self.English,self.Python,self.C,self.Grade_num)