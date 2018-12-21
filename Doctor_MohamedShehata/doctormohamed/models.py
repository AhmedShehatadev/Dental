## Our data base model for now
## To be updated based on buisness req
from datetime import datetime
from doctormohamed import db


class Patient(db.Model):
    # primary_key patient id
    id = db.Column(db.Integer,primary_key=True)
    # name
    username = db.Column(db.String(20),unique=True,nullable=False)

    #Email
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(25),nullable=False,default='default.jpg')

    #password
    password = db.Column(db.String(60),nullable=False)

    #PatienVisits
    patientvisits = db.relationship('PatientVisits',backref='patientvisit',lazy=True)

    def __repr__(self):
        return f"Patient('{self.username}', '{self.email}', '{self.image_file}')"

class PatientVisits(db.Model):
      visit_id = db.Column(db.Integer,primary_key=True)
      visit_title  = db.Column(db.String(100), nullable=False)
      visit_reason = db.Column(db.Text, nullable=False)
      visit_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
      user_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)

      def __repr__(self):
        return f"PatientVisits('{self.visit_title}', '{self.visit_date}')"
