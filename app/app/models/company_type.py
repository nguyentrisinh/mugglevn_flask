from . import db


class CompanyType(db.Model):
    __tablename__ = 'company_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __unicode__(self):
        return self.name

    def init_company_type(self, name):
        self.name = name
