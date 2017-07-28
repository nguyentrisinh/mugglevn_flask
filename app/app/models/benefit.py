from . import db


class Benefit(db.Model):
    __tablename__ = 'benefits'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __unicode__(self):
        return self.name

    def init_benefit(self, name):
        self.name = name